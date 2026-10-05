from .config import Config
from ..services.downdetector import check_all_services
from .incident_monitor import IncidentMonitor
from .types import ServiceName


def create_monitors():
    monitors = {}
    for service_name in ServiceName:
        monitors[service_name.value] = IncidentMonitor()
    return monitors

MONITORS = create_monitors()

def check_all():
    results = check_all_services()
    
    for service in results:
        handler = MONITORS.get(service['name'])
        if handler:
            handler.handle(service)
            