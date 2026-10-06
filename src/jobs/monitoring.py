import time
import random

from ..slack.notification_orchestrator import check_all

def run():
    try:
        print(f"Monitoramento iniciado: {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())}")
        check_all()
        print(f"Monitoramento finalizado: {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())}\n")
    except Exception as e:
        print(f"Erro no monitoramento: {e}")

def start_scheduler():
    cont = 0
    run()
    
    while True:
        # Aleatório entre 60s e 180s
        delay = random.randint(60, 180)
        print(f"Próxima verificação em {delay//60} minutos...")
        time.sleep(delay)
        run()

start_scheduler()