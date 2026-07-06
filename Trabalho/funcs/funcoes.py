#Libs: Pyautogui, time e PIL
import pyautogui as pag
from time import sleep
from PIL import Image, ImageDraw, ImageFont

#Função para abrir o navegador
def AbrirNavegador():

    #Pegando o navegador que o usuário vai querer usar
    navegador = pag.prompt("Digite o navegador que deseja abrir").lower()
    
    #Verificando se o usuario usa perfil no navegador
    perfil = pag.prompt("Você possui perfis no navegador? (s/n)").lower()

    #Array com os navegadores - IA listou pra mim 
    arrayNavegadores = ['chrome', 'firefox', 'edge', 'opera', 'safari', 'brave', 'vivaldi', 'tor', 'chromium', 'opera gx']
    
    #Verifica se o navegador digitado existe, se não ele para a execução da função e avisa
    if navegador not in arrayNavegadores:
        pag.alert("Navegador não encontrado")
        return
    
    #Verifica se há perfis
    if perfil in ['s', 'sim']:

        #Acessando area de trabalho e abrindo o menu iniciar
        pag.hotkey("win", "d")
        sleep(0.1)
        pag.press("win")
        sleep(0.1)

        #Escreve o nome do navegador e abre o primeiro perfil
        pag.write(navegador, interval=0.1)
        pag.press("enter")
        sleep(3)
        pag.press("tab")
        sleep(0.1)
        pag.press("enter")
        sleep(3)

    #Verifica se não há perfil
    elif perfil in ['n', 'não', 'nao']:

        #Acessando area de trabalho e abrindo o menu iniciar
        pag.hotkey("win", "d")
        sleep(0.1)
        pag.press("win")
        sleep(1)

        #Escreve o nome do navegador e abre o mesmo
        pag.write(navegador, interval=0.1)
        sleep(1)
        pag.press("enter")
        sleep(3)

    #Caso usuario tenha escrito outra coisa
    else:
        pag.alert("Opção inválida")
        return
    
    #Atalho para deixar em tela cheia, não faz nada se ja estiver
    pag.hotkey("alt", "space")
    pag.press("x")
    sleep(1)

    try:
        coords = pag.locateCenterOnScreen("assets/pag/apps.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de Apps")
        return
    
    pag.click(coords)
    sleep(3)

    #Tenta localizar o botão do Google Apps
    try:
        coords = pag.locateCenterOnScreen("assets/pag/docs.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão do Google Docs")
        return
    
    pag.click(coords)
    sleep(3)

    #Tenta localizar o botão de criar novo documento, se não conseguir para a execução da função
    try:
        coords = pag.locateCenterOnScreen("assets/pag/criar.png", confidence=0.8)
    except:
        pag.alert("Não foi possivel localizar o botão de criar")
        return

    pag.click(coords)
    sleep(3)

#Função para subir as imagens dos cartazes 
def UploadCartaz(dirExecucao, nome):
    #Tenta localizar o botão de inserir, se não conseguir para a execução da função
    try:
        coords = pag.locateCenterOnScreen("assets/pag/inserir.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de inserir")
        return
    
    pag.click(coords)
    sleep(1)

    #Tenta localizar o botão de adicionar imagem, se não conseguir para a execução da função
    try:
        coords = pag.locateCenterOnScreen("assets/pag/imagem.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de adicionar imagem")
        return
    
    pag.moveTo(coords)
    sleep(1)

    #Tenta localizar o botão de upload do computador, se não conseguir para a execução da função
    try:
        coords = pag.locateCenterOnScreen("assets/pag/upload.png", confidence=0.6)
        print(coords)
    except:
        pag.alert("Não foi possível localizar o botão de upload")
        return
        
    pag.click(coords)
    sleep(1)

    #Escreve o caminho do arquivo usando o dirExecucao e entrando em subdiretorios, transformado em string
    pag.write(str(dirExecucao / "assets" / "pill" / f"{nome}.png"), interval=0.01)
    pag.press("enter")
    sleep(1)

#Função pra salvar o cartaz
def SalvarCartaz():

    #Tenta localizar o botão de arquivo, se não conseguir para a execução da função
    try:
        coords = pag.locateCenterOnScreen("assets/pag/arquivo.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de arquivo")
        return
        
    pag.click(coords)
    sleep(1)

    #Tenta localizar o botão de baixar, se não conseguir para a execução da função
    try:
        coords = pag.locateCenterOnScreen("assets/pag/baixar.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de baixar")
        return

    pag.moveTo(coords)
    sleep(1)

    #Tenta localizar o botão de baixar como PDF, se não conseguir para a execução da função
    try:
        coords = pag.locateCenterOnScreen("assets/pag/pdf.png", confidence=0.8)
    except:
        pag.alert("Não foi possível localizar o botão de baixar PDF")
        return

    pag.click(coords)
    sleep(1)

#Função auxiliar para centralizar texto - IA sugeriu
def Centralizado(draw, img, texto, y, fonte, cor="white"):

    #Caixa delimitadora do texto
    bbox = draw.textbbox((0, 0), texto, font=fonte)

    #bbox é uma tupla de 4 indexes, esquerda, cima, direta e baixo, subtrai direita de esquerda
    largura = bbox[2] - bbox[0]

    #Atribui a x a metade da diferença entre o tamanho da imagem e a largura
    x = (img.width - largura) / 2

    #
    draw.text((x, y), texto, fill=cor, font=fonte)

#Função para gerar cartazes, recebendo do script principal o nome, crime, recompensa e dirExecucao
def GerarCartaz(nome, crime, recompensa, dirExecucao):

    #tratamento de erro float is not a string
    nome = str(nome)
    crime = str(crime)
    recompensa = str(recompensa)

    #Abre a img de modelo
    img = Image.open("assets/pill/modelo.png")
    draw = ImageDraw.Draw(img)

    #Fontes diferentes para cada tipo de escrita 
    fontNome = ImageFont.truetype("assets/font/Anton-Regular.ttf", 80)
    fontCrime = ImageFont.truetype("assets/font/Anton-Regular.ttf", 40)
    fontRecompensa = ImageFont.truetype("assets/font/Anton-Regular.ttf", 60)

    #Escreve o nome, crime e recompensa na imagem
    Centralizado(draw, img, nome, 200, fontNome, "white")
    Centralizado(draw, img, crime, 600, fontCrime, "white")
    Centralizado(draw, img, f"Recompensa: R${recompensa}", 700, fontRecompensa, "white")

    #Salva imagem no subdiretorio assets/pill 
    img.save(f"{dirExecucao}/assets/pill/{nome}.png", "PNG")

