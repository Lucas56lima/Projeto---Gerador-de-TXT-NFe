import pyautogui as pg
import pygetwindow
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

lojas_df = pd.read_excel("C:/Users/Usuário/Desktop/lojas_dre.xlsx",sheet_name="Planilha2")
# time.sleep(3)
# print(pg.position())

resolucao_x_padrao = int(1600)
resolucao_y_padrao = int(900)

time.sleep(3)
print(pg.position())

def automatizar_dre():
    messagebox.showinfo(message="Lembre-se, antes de apertar ok, certifique-se de que o presence foi iniciado!")    
    try:
        resolucao_x = int(text_x.get())
        resolucao_y = int(text_y.get())
    except ValueError:
        messagebox.showerror(message="Os valores precisam ser do tipo Numérico!")    
    
    if resolucao_x <= resolucao_y:
        messagebox.showerror(message="Por gentileza insira valores válidos!")
    else:
        try:
            time.sleep(1) 
            window = pygetwindow.getWindowsWithTitle('(Remoto)')[0]
            time.sleep(1)      
            window.activate()
            # Entrar na página do DRE
            time.sleep(2)
            x = ((517 * 100) / resolucao_x_padrao)
            y = ((170 * 100) / resolucao_y_padrao)
            result_x = (x/100) * resolucao_x
            result_y = (y/100) * resolucao_y
        
            pg.click(x=result_x, y=result_y)

            time.sleep(2)         

            for i,lojas in enumerate(lojas_df['loja']):
                filiais = str(lojas_df.loc[i,'loja'])
                descricao = str(lojas_df.loc[i,'descricao'])
                if lojas != " ":
                    # clica para selecionar as lojas    
                    x = ((796 * 100) / resolucao_x_padrao)
                    y = ((328 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x, y=result_y)
                    time.sleep(2)

                    # insere a configuração do layout
                    x = ((632 * 100) / resolucao_x_padrao)
                    y = ((348 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x, y=result_y)
                    time.sleep(1)
                    pg.write("4")
                    time.sleep(1)
                    pg.press("enter")

                    time.sleep(1)
                    x = ((658 * 100) / resolucao_x_padrao)
                    y = ((514 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(result_x, result_y)
                    time.sleep(1)
                    x = ((672 * 100) / resolucao_x_padrao)
                    y = ((301 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x, y=result_y)
                    time.sleep(2)

                    # clica para filtrar as lojas
                    x = ((632 * 100) / resolucao_x_padrao)
                    y = ((337 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.doubleClick(x=result_x, y=result_y)
                    time.sleep(1)            
                    x = ((803 * 100) / resolucao_x_padrao)
                    y = ((404 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y  
                    pg.doubleClick(x=result_x, y=result_y)
                    time.sleep(1)
                    # insere os valores das filiais   
                    if len(str(filiais)) < 2:               
                        pg.write('0' + filiais)
                    else:
                        pg.write(filiais)
                        time.sleep(1)
                        
                    x = ((832 * 100) / resolucao_x_padrao)
                    y = ((523 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x, y=result_y)
                        
                    time.sleep(1)
                    x = ((616 * 100) / resolucao_x_padrao)
                    y = ((323 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x, y=result_y)
                    time.sleep(1)                    

                    time.sleep(1)
                    # clica para consultar
                    x = ((891 * 100) / resolucao_x_padrao)
                    y = ((275 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x, y=result_y)
                    time.sleep(1)
                    x = ((957 * 100) / resolucao_x_padrao)
                    y = ((319 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y        
                    pg.click(x=result_x, y=result_y)
                    time.sleep(15)
                    x = ((371 * 100) / resolucao_x_padrao)
                    y = ((64 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x,y=result_y)
                    time.sleep(1)
                    x = ((400 * 100) / resolucao_x_padrao)
                    y = ((105 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x,y=result_y)
                    time.sleep(1)
                    # clica para salvar o arquivo                    
                    x = ((397 * 100) / resolucao_x_padrao)
                    y = ((103 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=397, y=103)

                    time.sleep(1)
                    x = ((296 * 100) / resolucao_x_padrao)
                    y = ((64 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.click(x=result_x, y=result_y)
                    time.sleep(1)

                    x = ((528 * 100) / resolucao_x_padrao)
                    y = ((465 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y

                    # seleciona o local    
                    pg.doubleClick(x=result_x, y=result_y)          
                    time.sleep(1)
                    x = ((1104 * 100) / resolucao_x_padrao)
                    y = ((514 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y

                    pg.click(x=result_x, y=result_y)
                    time.sleep(1)
                    pg.click(x=result_x, y=result_y)           
                    time.sleep(1)
                    pg.click(x=result_x, y=result_y)           
                    time.sleep(1)
                    x = ((665 * 100) / resolucao_x_padrao)
                    y = ((486 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.doubleClick(x=result_x, y=result_y)
                    time.sleep(1)
                    x = ((630 * 100) / resolucao_x_padrao)
                    y = ((355 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y    
                    #seleciona a pasta padrão
                    pg.doubleClick(x=result_x, y=result_y)
                    time.sleep(1)
                    x = ((646 * 100) / resolucao_x_padrao)
                    y = ((244 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    pg.doubleClick(x=result_x, y=result_y)

                    time.sleep(1)
                    x = ((689 * 100) / resolucao_x_padrao)
                    y = ((540 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    # insere o nome da planilha
                    pg.click(x=result_x, y=result_y)
                    time.sleep(1)
                    pg.write(descricao)
                    time.sleep(1)
                    x = ((1073 * 100) / resolucao_x_padrao)
                    y = ((542 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y
                    # confirma o salvamento
                    pg.click(x=result_x, y=result_y)
                    time.sleep(1)
                    pg.press("enter")

                    # retorna para o filtro
                    time.sleep(1)
                    x = ((416 * 100) / resolucao_x_padrao)
                    y = ((66 * 100) / resolucao_y_padrao)
                    result_x = (x/100) * resolucao_x
                    result_y = (y/100) * resolucao_y    
                    pg.click(x=result_x, y=result_y)

                    for i in range(lojas_df["loja"].count()):
                        bar['value'] = i + 1
                                
        except IndexError:
            messagebox.showerror(message="O Presence não foi iniciado")
    
 
janela = tk.Tk()
janela.geometry('200x200')
janela.configure(background="#FFFAFA")
janela.title("Automação DRE")
label_x = tk.Label(janela,text="Insira o primeiro valor da resolução: ")
text_x = tk.Entry(janela)
label_y = tk.Label(janela,text="Insira o segundo valor da resolução: ")
text_y = tk.Entry(janela)
label_progress = tk.Label(janela,text="Progresso")
bar = ttk.Progressbar(janela,length=150,cursor='spider',mode='determinate',orient=tk.HORIZONTAL)


label_x.grid(column=2,row=0)
text_x.grid(column=2, row=2, padx=0, pady=0)
text_x.config(width=30)
label_y.grid(column=2,row=3)
text_y.config(width=30)
text_y.grid(column=2,row=4,padx=0,pady=0)


botao = tk.Button(janela,default='normal', text="Iniciar automação", command=automatizar_dre)
botao.grid(column=2,row=6)
bar.grid(column= 2,row=9,pady=10)
label_progress.grid(column=2,row=8,pady=10)


janela.mainloop()            

# automatizar_dre()
