import time
from playwright.sync_api import sync_playwright

url = str(input("URL do Vídeo: "))
viewsdesejo = int(input("Quantas views deseja: "))
views = 0
while views <= viewsdesejo:
    with sync_playwright() as p:
        navega = p.chromium.launch(headless=False, slow_mo=50)
        pagina = navega.new_page()
        pagina.goto(f'{url}')
        time.sleep(3)
        pagina.keyboard.press("k")
        time.sleep(60)
        views = views + 1
