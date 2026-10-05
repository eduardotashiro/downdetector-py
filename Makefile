-include .env
export

run:
		@echo "ativa ambiente e roda scraper"
		@.venv/bin/python -m src.jobs.monitoring.py

test:
		@echo "rodando teste de envio de mensagens para os slack"
		@.venv/bin/python -m src.scripts.test_slack_alert

