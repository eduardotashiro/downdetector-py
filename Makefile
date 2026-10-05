-include .env
export

localrun:
		@echo "ativa ambiente e roda scraper"
		@.venv/bin/python -m src.jobs.monitoring

dockerrun:
		@echo "roda em container"
		@python -m src.jobs.monitoring

test:
		@echo "rodando teste de envio de mensagens para os slack"
		@.venv/bin/python -m src.scripts.test_slack_alert

