from enum import Enum
from enum import Flag

class ServiceStatus(str, Enum):
    SUCCESS = "success"
    DANGER = "danger"
    WARNING = "warning" 

class ServiceName(str, Enum):
    BANCO_DO_BRASIL = "Banco do Brasil"
    BRADESCO = "Bradesco"
    SANTANDER = "Santander"
    PIX = "Pix"
    PICPAY = "Pic Pay"
    ITAU = "Banco Itaú"
    NUBANK = "Nubank"
    MERCADO_PAGO = "Mercado Pago"
    CIELO = "Cielo"

class ServiceURL(str, Enum):
    BANCO_DO_BRASIL = "https://downdetector.com.br/fora-do-ar/banco-do-brasil/"
    BRADESCO = "https://downdetector.com.br/fora-do-ar/bradesco/"
    SANTANDER = "https://downdetector.com.br/fora-do-ar/santander/"
    PIX = "https://downdetector.com.br/fora-do-ar/pix/"
    PICPAY = "https://downdetector.com.br/fora-do-ar/picpay/"
    ITAU = "https://downdetector.com.br/fora-do-ar/banco-itau/"
    NUBANK = "https://downdetector.com.br/fora-do-ar/nubank/"
    MERCADO_PAGO = "https://downdetector.com.br/fora-do-ar/mercadopago/"
    CIELO = "https://downdetector.com.br/fora-do-ar/cielo/"

class StatusMap(str, Enum):
    success = ServiceStatus.SUCCESS
    warning = ServiceStatus.WARNING
    danger = ServiceStatus.DANGER


# class StatusIcon():
#     ServiceStatus.SUCCESS = "🟢",
#     ServiceStatus.WARNING = "⚠️",
#     ServiceStatus.DANGER = "🔴"
    
