import pyautogui as pg
import pygetwindow
import time
import pandas as pd
from tkinter import *
from tkinter import messagebox


# pg.press('win')
# time.sleep(1)
# pg.write('relatorio.xlsx')
# pg.press('backspace')
# pg.press('enter')
# time.sleep(2)

# windowSystem = pygetwindow.getWindowsWithTitle('Remoto')[0]
# windowSystem.activate()

# time.sleep(1)

# class Network(object):
    
#     def __init__(self,sizes):
#         self.num_layers = len(sizes)
#         self.sizes = sizes
#         self.biases = [np.random.randn(y,1) for y in sizes[1:]]
#         self.weights = [np.random.randn(y,x) for x, y in zip(sizes[:-1],sizes[1:])]

lojas_df = pd.read_excel('C:/Users/Usuário/Desktop/empresas-para-relatorio.xlsx')

lojas_df.head()

time.sleep(3)

pg.click(x=108, y=413)
time.sleep(2)
pg.click(x=135, y=236)

pg.click(x=135, y=236)
time.sleep(2)

pg.doubleClick(x=708, y=229)

data = '01/11/2023'
time.sleep(2)
pg.write(data)

time.sleep(2)

pg.click(x=728, y=560)

# time.sleep(2)
# print(pg.position())

for i, lojas in enumerate(lojas_df['empresas']):
    filiais = str(lojas_df.loc[i,'empresas'])
    if lojas != " ":        
        pg.click(x=670, y=175)
        pg.press('backspace')
        if len(str(filiais)) < 2:               
            pg.write('0' + filiais)
        else:
            pg.write(filiais)
        time.sleep(1)
        pg.press('enter')         
        pg.click(x=955, y=164)
        time.sleep(2)
        pg.hotkey('ctrl','a')
        time.sleep(2)
        pg.hotkey('ctrl','c')
        time.sleep(2)
        windowExcel = pygetwindow.getWindowsWithTitle('relatorio.xlsx')[0]
        windowExcel.activate()
        time.sleep(2)
        # pg.click(x=54, y=233)
        pg.hotkey('ctrl','v')
        time.sleep(2)       

        pg.click(x=54, y=233)
        pg.hotkey('ctrl','down')
        time.sleep(2)
        pg.press('enter')        
        time.sleep(2)        
        windowSystem = pygetwindow.getWindowsWithTitle('Remoto')[0]
        windowSystem.activate()
        time.sleep(2)
        pg.click(x=438, y=45)
    else: 
        break

# janela = Tk()
# janela.geometry('500x300')
# janela.configure(background="#FFFAFA")
# janela.title("Automação Relatório")
# # texto.grid(column=0, row=0, padx=0, pady=0)
# botao = Button(janela,default='normal', text="Enviar mensagem", command=lambda: envia_mensagem(upload_arquivo,inserir_mensagem))
# botao.place(x=10,y=230,width=120,height=30)



# janela.mainloop()

    



