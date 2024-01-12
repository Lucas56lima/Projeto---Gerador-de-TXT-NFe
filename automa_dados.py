from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import pyautogui as pg

def dados_covid_estado(navegador):
    time.sleep(4)
    pg.click(x=484,y=371)
    time.sleep(1)
    pg.press('f3')
    time.sleep(1)
    pg.write("SP")
    time.sleep(1)
    pg.press('Enter')              
    pg.scroll(y= -5)
    botao_elements = navegador.find_element(By.ID,'btEstado').click()

    totais_elements = navegador.find_elements(By.CLASS_NAME,'ng-scope')[178].text

    estados_elements = navegador.find_elements(By.CLASS_NAME,'ng-scope')[204:490:19]
    # print(estados_elements)
    lista_estados = []
    lista_estados.append(totais_elements)

    for estado in estados_elements:
        estado = estado.text
        lista_estados.append(estado)
        
            

navegador = webdriver.Chrome()

url = 'https://infoms.saude.gov.br/extensions/covid-19_html/covid-19_html.html'

navegador.get(url=url)

while len(navegador.find_elements(By.ID,"qs-chart-tooltip")) < 1:
    time.sleep(1)

dados_covid_estado(navegador)
