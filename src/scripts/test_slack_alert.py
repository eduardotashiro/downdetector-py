#!/usr/bin/env python3
from src.slack.incident_monitor import IncidentMonitor
from src.slack.types import ServiceStatus, ServiceName, ServiceURL
from ..slack.incident_monitor import IncidentMonitor

import time

def test_slack_alert():
    print("test envio de alerta no Slack...")

    # monitor = {}
    monitor = IncidentMonitor()

    service_danger = {
        "name": ServiceName.PIX,  
        "url": ServiceURL.PIX,    
        "outage": ServiceStatus.DANGER
    }
    
    monitor.handle(service_danger)

    print("\n")
    print("... ... ... ... ... ...  loading")
    print("... ... ... ... ...  loading ...")
    print("... ... ... ... loading ... ....")
    print("... ... ... loading ... .... ...")
    print("... ... loading ... ... .... ...")
    print("... loading ... ... ... .... ...")
    print("loading ... ... ... ... .... ...")
    print("\n")

    time.sleep(10)

    service_success = {
        "name": ServiceName.PIX,
        "url": ServiceURL.PIX,
        "outage": ServiceStatus.SUCCESS
    }

    monitor.handle(service_success)

if __name__ == "__main__":
    test_slack_alert()