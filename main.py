import time
from playwright.sync_api import sync_playwright

url = str(input("URL do Vídeo: ")) #Pede a URL do Vídeo
viewsdesejo = int(input("Quantas views deseja: ")) #Peede a quantia de views necessárias
views = 0 #Define no numero de views pra 0 
while views <= viewsdesejo: #Codigo pra repetir o processo varias vezes
    with sync_playwright() as p: #Pra iniciar o Playwright
        navega = p.chromium.launch(headless=False, slow_mo=50) #iniciar o navegador
        pagina = navega.new_page() #Aba uma pagina vazia
        pagina.goto(f'{url}') #Vai para a url do video
        time.sleep(3) #Espera 3 segundos para o vídeo carregar
        pagina.keyboard.press("k") #Aperta para o video começar a rodar
        time.sleep(60) #Espera 1 minuto para contar a view
        views = views + 1 #Adiciona mais uma view a variavel
        pagina = pagina.close() #fecha a pagina
        #E assim se repete a o numero de views for igual ao numero que você pediu
