-include .env
export

localrun:
		@echo "ativando ambiente e roda scraper"
		@.venv/bin/python -m src.jobs.monitoring

dockerrun:
		@echo "iniciando RR"
		@python -m src.jobs.monitoring

test:
		@echo "testando envio de msg p o slack"
		@.venv/bin/python -m src.scripts.test_slack_alert
