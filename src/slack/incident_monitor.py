import time
from datetime import datetime
from zoneinfo import ZoneInfo
from .message_formatter import MessageFormatter
from .notifier import send_slack_notification
from .types import ServiceStatus


BRASIL_TZ = ZoneInfo('America/Sao_Paulo')


class IncidentMonitor:
    def __init__(self):
        self.incident = None

    def handle(self, service: dict):
        name = service['name']
        url = service['url']
        status = service['outage']
        
        service_name = name.value if hasattr(name, 'value') else name
        service_url = url.value if hasattr(url, 'value') else url
        
        message_formatter = MessageFormatter(service_name=service_name,status=status,service_url=service_url)

        if status == ServiceStatus.DANGER and not self.incident:
            self.incident = {
                "started_at": time.time(),
                "level": status,
                "alert_sent": False
            }
            
            payload = message_formatter.format_alert_danger()
            send_slack_notification(payload)

            self.incident["alert_sent"] = True
            print(f"🔴 STATUS DANGER PARA {service_name} ENVIADO NO SLACK !")
            return
        
        if status == ServiceStatus.SUCCESS and self.incident and self.incident.get("alert_sent"):
            duration = time.time() - self.incident["started_at"]
            minutes = int(duration // 60)
            hours = int(minutes // 60)
            minutes_remaining = int(minutes % 60)
            
            time_text = f"{hours}h {minutes_remaining}min" if hours > 0 else f"{minutes}min"
            incident_start = datetime.fromtimestamp(self.incident["started_at"], BRASIL_TZ).strftime('%d/%m/%Y às %H:%M:%S')
            end_incident = datetime.now(BRASIL_TZ).strftime('%d/%m/%Y às %H:%M:%S')

            payload = message_formatter.format_alert_resolved(incident_start, end_incident, time_text)
            send_slack_notification(payload)

            print(f"✅ INCIDENTE NO {service_name} RESOLVIDO ! DURAÇÃO: {time_text}")
            self.incident = None
            return
        
        if status == ServiceStatus.WARNING:
            print(f"⚠️ {service_name}: possíveis problemas (warning)")
            return
        
        if status == ServiceStatus.DANGER and self.incident:
            print(f"INCIDENTE EM {service_name} | STATUS: {status}, AINDA ATIVO...")
            return
        
        if status == ServiceStatus.SUCCESS and not self.incident:
            print(f"{service_name} 🟢")