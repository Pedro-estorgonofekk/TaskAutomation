#Gerador de cartaz de procurado
#Foi um bom codigo, fiz ali no dia, gostei, conhecia já a biblioteca PILLOW e deu pra fazer algo bacana com os ensinamentos em sala de aula
#Libs: Path, pandas, time, pyautogui, e funcoes.py para modulação
from pathlib import Path
import pandas as pd
import pyautogui as pag
from time import sleep
from funcs.funcoes import AbrirNavegador, GerarCartaz, SalvarCartaz, UploadCartaz

#Importando planilha de procurados
procurados = pd.read_excel('procurados.xlsx')

#Pegando o caminho do diretório de execução do script - Solução de IA
dirExecucao = Path(__file__).resolve().parent

#Abrindo navegador 
AbrirNavegador()
sleep(0.5)

#Alerta de indicação que está gerando os cartazes
pag.alert("Gerando cartazes, pressione OK para continuar")

#Loop pra iterar em cada linha da planilha e atribuir os dados, _ é variavel de descarte, n vai usar ela
for _, row in procurados.iterrows():
    
    #Para cada linha do excel, busca o dado e atribui à variavel adequada 
    nome = row['Nome']
    crime = row['Crime']
    recompensa = row['Recompensa']

    #Chama a função para gerar os cartazes, passnado os parametros necessarios
    GerarCartaz(nome, crime, recompensa, dirExecucao)
    sleep(0.5)

    #Chama a função para fazer os uploads dos cartazes no documento do docs, passando os parametros necessarios
    UploadCartaz(dirExecucao, nome)

#Chama a função para baixar o cartaz em PDF
SalvarCartaz()

#Alerta para indicar o fim do programa
pag.alert("Automação concluída! Pressione OK para sair")