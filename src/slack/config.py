import os

class Config:
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")