from .types import ServiceStatus,ServiceName,ServiceURL,Enum
from datetime import datetime
from zoneinfo import ZoneInfo


BRASIL_TZ = ZoneInfo('America/Sao_Paulo')


class MessageFormatter:
    def __init__(self, service_name: ServiceName, status: ServiceStatus, service_url: ServiceURL):
        self.service_name = service_name
        self.status = status
        self.service_url = service_url

    def format_alert_danger(self):
            return {"text":
                f":alert: *Nível Crítico - {self.service_name}*\n\n"
                f"• *Status:* `critic`\n"
                f"• *Detectado em:* {datetime.now(BRASIL_TZ).strftime('%d/%m/%Y às %H:%M:%S')}\n\n"
                f"<{self.service_url} | Ver no Downdetector>"
            }

    def format_alert_resolved(self,incident_start,end_incident,time_text):
        return {"text":
            f":white_check_mark: *Normalizado* - *{self.service_name}*\n\n"
            f"• *Status:* `resolved`\n"
            f"• *Detectado em:* {incident_start}\n"
            f"• *Fim:* {end_incident}\n"
            f"• *Duração:* {time_text}\n\n"
            f"<{self.service_url} | Ver no Downdetector>"
        }      