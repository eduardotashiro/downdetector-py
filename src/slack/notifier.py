import json
import urllib.request
from .config import Config 

def send_slack_notification(message):
    slack_webhook_url = Config.SLACK_WEBHOOK_URL
    if not slack_webhook_url:
        raise ValueError("environment variable is missing bro")

    data = json.dumps(message).encode("utf-8")
    req = urllib.request.Request(slack_webhook_url, data = data, headers = {"Content-Type":"application/json"})

    try:
        with urllib.request.urlopen(req) as response:
            print("slack notification sent successfully")
            return response.status
    except Exception as e:
        print(f"failed to send message to slack bro: {e}")
        return None
                                                                      