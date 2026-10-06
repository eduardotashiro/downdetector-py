from camoufox.sync_api import Camoufox
import time
import random
from typing import Optional, List, Dict

from ..slack.types import ServiceName, ServiceURL, ServiceStatus

SERVICES = [
    {"name": ServiceName.PICPAY, "url": ServiceURL.PICPAY},
    {"name": ServiceName.NUBANK, "url": ServiceURL.NUBANK},
    {"name": ServiceName.PIX, "url": ServiceURL.PIX},
    {"name": ServiceName.SANTANDER, "url": ServiceURL.SANTANDER},
    {"name": ServiceName.ITAU, "url": ServiceURL.ITAU},
    {"name": ServiceName.BRADESCO, "url": ServiceURL.BRADESCO},
    {"name": ServiceName.BANCO_DO_BRASIL, "url": ServiceURL.BANCO_DO_BRASIL},
    {"name": ServiceName.MERCADO_PAGO, "url": ServiceURL.MERCADO_PAGO},
    {"name": ServiceName.CIELO, "url": ServiceURL.CIELO}
]

# def force_close_browser(browser):
#     if browser


def wait_for_real_content(page, service_name: str, max_wait: int = 15) -> bool:

    deadline = time.time() + max_wait
    
    while time.time() < deadline:
        try:
            body = page.evaluate("() => document.body?.innerText?.toLowerCase() || ''")
        except:
            body = ""
        
        if any(x in body for x in ["relatos dos usuários", "relatos de usuáriosa"]):
            return True
        
        if any(x in body for x in ["verificando", "segurança", "confirme que é humano"]):
            time.sleep(2)
            continue
        
        time.sleep(1)
    
    return False

def detect_status(page) -> Optional[str]:
    try:
        body = page.evaluate("() => document.body?.innerText?.toLowerCase() || ''")
        
        if "não mostram problemas" in body or "no current problems" in body:
            return ServiceStatus.SUCCESS
        if "possíveis problemas" in body or "possible problems" in body:
            return ServiceStatus.WARNING
        if "mostram problemas" in body or "show problems with" in body:
            return ServiceStatus.DANGER
        
        return None
    except:
        return None

def check_single_service(browser, service: Dict) -> Optional[str]:
    name = service['name'].value 
    url = service['url'].value
    
    page = None
    try:
        print(f"{name}...", end="", flush=True)
        
        page = browser.new_page()
        page.set_extra_http_headers({ "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"})
        page.goto(url, wait_until="domcontentloaded")
        
        if wait_for_real_content(page, name, max_wait=15):
            status = detect_status(page)
            if status == ServiceStatus.SUCCESS:
                print("✅")
            elif status == ServiceStatus.WARNING:
                print("⚠️")
            elif status == ServiceStatus.DANGER:
                print("🔴")
                
            return status
        else:
            print("❌")
            return None
            
    except Exception as e:
        print(f"❌ ({str(e)[:30]})")
        return None
    finally:
        if page:
            try:
                page.close()
            except:
                pass

def check_all_services() -> List[Dict]:
    results = []
    start_total = time.time()
    
    services_to_check = SERVICES.copy()
    random.shuffle(services_to_check)
    
    with Camoufox(
        headless="virtual",
        os="linux",
        humanize=True,
        geoip=True,
        block_webrtc=True,
        window=[1920, 1080],
    ) as browser:
        
        for i, service in enumerate(services_to_check):
            name = service['name'].value 
            
            status = check_single_service(browser, service)
            
            if not status:
                time.sleep(1.5)
                status = check_single_service(browser, service)
            
            if status:
                results.append({
                    "name": service['name'],
                    "url": service['url'],
                    "outage": status
                })
            
            if i < len(services_to_check) - 1:
                time.sleep(random.uniform(1.3, 3))
    
    total_time = round(time.time() - start_total, 1)
    print(f"\n{len(results)}/{len(SERVICES)} serviços | {total_time}s")
    
    return results