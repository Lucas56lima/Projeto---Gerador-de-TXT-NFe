import pyautogui as pg
import pygetwindow
import time
import pandas as pd
from tkinter import *
from tkinter import messagebox

lojas_df = pd.read_excel('C:/Users/Usuário/Desktop/devolução_cellution/rfs_matriz.xlsx')

lojas_df.head()

time.sleep(3)
# pg.doubleClick(x=239, y=126)

# time.sleep(2)

# pg.click(x=75, y=180)
#time.sleep(1)
# pg.doubleClick(x=112, y=254)
# time.sleep(1)
# pg.click(x=41, y=812)
# time.sleep(1)
# pg.click(x=24, y=35)
# time.sleep(1)
# pg.click(x=50, y=54)


# ======== Inserir Itens ==================

# Inserir Descrição


# print(pg.position())



for i, itens in enumerate(lojas_df['código']):
    skus = str(lojas_df.loc[i,'sku'])
    quantidade = str(lojas_df.loc[i,'qtd'])
    preco_un = str(lojas_df.loc[i,'preço um'])
    valor_total = str(lojas_df.loc[i,'valor total'])
    base_icms = str(lojas_df.loc[i,'base icms'])
    aliquota_icms = str(lojas_df.loc[i,'aliquota icms'])
    base_ipi = str(lojas_df.loc[i,'base ipi'])
    aliquota_ipi = str(lojas_df.loc[i,'aliquota ipi'])
    ncm_itens = str(lojas_df.loc[i,'ncm'])
    descricao = str(lojas_df.loc[i,'produto'])  

    time.sleep(1)
    pg.click(x=333, y=163)
    time.sleep(1)
    pg.click(x=69, y=750)
    time.sleep(1)     
   
    # Inserir sku
    pg.click(x=187, y=111)
    pg.write(skus)
    pg.click(x=192, y=138)
    pg.write(descricao)

    # Inserir NCM
    pg.click(x=234, y=163)
    time.sleep(1)
    pg.write(ncm_itens)

    # Inserir CFOP
    time.sleep(1)
    pg.click(x=480, y=189)
    pg.write('6202')
    pg.press('enter')

    # inserir Un comercial
    time.sleep(1)
    pg.click(x=183, y=218)
    time.sleep(1)
    pg.write('UN')
    time.sleep(1)
    pg.click(x=216, y=245)
    pg.write('UN')

    #Inserir Quantidade
    time.sleep(1)
    pg.click(x=489, y=220)
    time.sleep(1)
    pg.write(quantidade)
    time.sleep(1)
    pg.click(x=546, y=243)
    time.sleep(1)
    pg.write(quantidade)

    # Inserir Valor un
    time.sleep(1)
    pg.click(x=832, y=217)
    time.sleep(1)
    pg.write(preco_un)
    time.sleep(1)
    pg.click(x=862, y=244)
    time.sleep(1)
    pg.write(preco_un)


    # Inserir Valor total
    time.sleep(1)
    pg.click(x=285, y=341)
    time.sleep(1)
    pg.write(valor_total)

    # ======== Inserir Tributos ================

    time.sleep(1)
    pg.click(x=100, y=81)

    # inserir ICMS
    time.sleep(1)
    pg.click(x=237, y=251)
    pg.write('9')
    time.sleep(1)
    pg.press('enter')
    pg.click(x=229, y=269)
    pg.write('2')
    pg.press('enter')


    time.sleep(1)
    pg.click(x=372, y=360)
    pg.write('v')
    pg.press('enter')

    # Inserir Base ICMS
    time.sleep(1)
    pg.click(x=386, y=402)
    time.sleep(1)
    pg.write(base_icms)

    # Inserir Alíquota ICMS
    time.sleep(1)
    pg.click(x=407, y=422)
    time.sleep(1)
    pg.write(aliquota_icms)

    # Inserir IPI
    time.sleep(1)
    pg.click(x=87, y=185)

    time.sleep(1)
    pg.click(x=353, y=210)
    pg.press('end')
    time.sleep(1)
    pg.press('enter')

    time.sleep(1)
    pg.click(x=340, y=234)
    time.sleep(1)
    pg.write('999')

    time.sleep(1)
    pg.click(x=354, y=324)

    time.sleep(1)
    pg.click(x=333, y=355)

    # Inserir Base IPI
    time.sleep(1)
    pg.click(x=375, y=343)
    time.sleep(1)
    pg.write(base_ipi)

    # Inserir Alíquota IPI
    time.sleep(1)
    pg.click(x=358, y=367)
    time.sleep(1)
    pg.write(aliquota_ipi)
    pg.press('tab')

    time.sleep(1)
    pg.click(x=47, y=823)

#==============================================================================
# print(pg.position())

# pg.write()




# pg.click(x=108, y=413)
# time.sleep(2)


# pg.click(x=117, y=275)

# time.sleep(1)

# pg.click(x=123, y=93)

# time.sleep(1)

# pg.click(x=230, y=96)

# time.sleep(1)

# pg.click(x=337, y=93)

# time.sleep(1)

# pg.doubleClick(x=751, y=95)

# data = '01/10/2023'

# pg.write(data)

# time.sleep(1)

# # time.sleep(2)
# # print(pg.position())

# for i, lojas in enumerate(lojas_df['empresas']):
#     filiais = str(lojas_df.loc[i,'empresas'])
    
#     if lojas != " ":        
#         pg.click(x=27, y=57)
#         time.sleep(1)
#         pg.press('backspace')        
#         time.sleep(1)
#         if len(str(filiais)) < 2:               
#             pg.write('0' + filiais)
#         else:
#             pg.write(filiais)
#         time.sleep(2)
#         pg.press('enter')
#         time.sleep(2)         
#         pg.click(x=929, y=89)
#         time.sleep(50)
#         pg.click(x=729, y=200)
#         time.sleep(2)
#         pg.hotkey('ctrl','a')
#         time.sleep(1)
#         pg.hotkey('ctrl','c')
#         time.sleep(1)
#         windowExcel = pygetwindow.getWindowsWithTitle('relatorio-fora.xlsx')[0]
#         windowExcel.activate()
#         time.sleep(1)
#         # pg.click(x=54, y=233)
#         pg.hotkey('ctrl','v')
#         time.sleep(1)       
#         pg.press('left')
#         # pg.click(x=54, y=233)
#         pg.write('loja')
#         pg.press('enter')
#         time.sleep(1)
#         pg.write(filiais)      
#         time.sleep(1)               
#         pg.hotkey('ctrl','down')                
#         pg.press('enter')
#         pg.press('left')
#         pg.hotkey('ctrl','b')
#         time.sleep(1)
#         windowSystem = pygetwindow.getWindowsWithTitle('Remoto')[0]
#         windowSystem.activate()
#         time.sleep(1)
#         pg.click(x=438, y=45)
#         messagebox.showinfo("Relatório da loja" + filiais + " foi importado!")
#     else: 
#         break
