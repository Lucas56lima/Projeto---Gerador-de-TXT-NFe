# import numpy as np
from tkinter import *
import tkinter as tk

preco_gato = int(1500)
preco_papagaio = int(2000)
preco_cachorro = int(150)

def retorna_label_desconto(label,valor):    
    label.config(text=f'O Valor total com desconto de 10% é:{valor:.2f}')     

def retorna_label_acrescimo(label,valor):
    label.config(text=f'O Valor total com acréscimo de 5% é :{valor:.2f}')     

def calcular_desconto(preco):
    desconto = preco * 0.1  # Calculando o desconto de 10%
    preco_com_desconto = preco - desconto  # Calculando o preço com desconto
    return preco_com_desconto

def calcular_acrescimo(preco):
    acrescimo = preco * 0.05  # Calculando o acréscimo de 5%
    preco_com_desconto = preco + acrescimo  # Calculando o preço com desconto
    return preco_com_desconto  


def gato():
    tela_gato = tk.Tk()    
    tela_gato.title('PetShop') #NOME QUE SE MOSTRARÁ EM JANELA 
    tela_gato.geometry("600x400")
    textoInicial1 = tk.Label(tela_gato, text='Pagamento') #Label é onde você vai colocar o texto em sua PÁGINA
    textoInicial1.grid(column=2) #Com ele você vai exibir o texto e definir em que posição ele irá aparecer
    valor_total = calcular_desconto(preco_gato)
    valor_acrescimo = calcular_acrescimo(preco_gato)
    label_total = tk.Label(tela_gato)
    label_total.grid(column=2,row=6)
    botao1 = tk.Button(tela_gato, text="Pix com 10% de desconto", command=lambda:retorna_label_desconto(label_total,valor_total))
    botao1.grid(column=2, row=1)
    botao1 = tk.Button(tela_gato, text="Débito",command=lambda:retorna_label_desconto(label_total,preco_gato))
    botao1.grid(column=2, row=2)
    botao1 = tk.Button(tela_gato, text="Crédito com 5% de acréscimo",command=lambda:retorna_label_acrescimo(label_total,valor_acrescimo))
    botao1.grid(column=2, row=3)
    botaoVol=tk.Button(tela_gato, text='Voltar', command=tela_gato.destroy)
    botaoVol.grid()



    
def cachorro():
    tela_cachorro = tk.Tk()
    tela_cachorro.title('PetShop') #NOME QUE SE MOSTRARÁ EM JANELA 
    tela_cachorro.geometry("600x400")
    textoInicial2 = tk.Label(tela_cachorro, text='Pagamento') #Label é onde você vai colocar o texto em sua PÁGINA
    textoInicial2.grid(column=2) #Com ele você vai exibir o texto e definir em que posição ele irá aparecer
    valor_desconto = calcular_desconto(preco_cachorro)
    valor_acrescimo = calcular_acrescimo(preco_cachorro) 
    label_total = tk.Label(tela_cachorro)
    label_total.grid(column=2,row=6)

    botao2 = tk.Button(tela_cachorro, text="Pix com 10% de desconto", command=lambda:retorna_label_desconto(label_total,valor_desconto))
    botao2.grid(column=2, row=1)
    botao2 = tk.Button(tela_cachorro, text="Débito",command=lambda:retorna_label_desconto(label_total,preco_cachorro))
    botao2.grid(column=2, row=2)
    botao2 = tk.Button(tela_cachorro, text="Crédito com 5% de acréscimo",command=lambda:retorna_label_acrescimo(label_total,valor_acrescimo))
    botao2.grid(column=2, row=3)
    botaoVo2=tk.Button(tela_cachorro, text='Voltar', command=tela_cachorro.destroy)
    botaoVo2.grid()
     
    
    
def papagaio():
    tela_papagaio = tk.Tk()
    tela_papagaio.title('PetShop') #NOME QUE SE MOSTRARÁ EM JANELA 
    tela_papagaio.geometry("600x400")
    textoInicial3 = tk.Label(tela_papagaio, text='Pagamento') #Label é onde você vai colocar o texto em sua PÁGINA
    textoInicial3.grid(column=2) #Com ele você vai exibir o texto e definir em que posição ele irá aparecer 
    valor_desconto = calcular_desconto(preco_papagaio)
    valor_acrescimo = calcular_acrescimo(preco_papagaio)
    label_total = tk.Label(tela_papagaio)
    label_total.grid(column=2,row=6) 

    botao3 = tk.Button(tela_papagaio, text="Pix com 10% de desconto", command=lambda:retorna_label_desconto(label_total,valor_desconto))
    botao3.grid(column=2, row=1)
    botao3 = tk.Button(tela_papagaio, text="Débito",command=lambda:retorna_label_desconto(label_total,valor_desconto))
    botao3.grid(column=2, row=2)
    botao3 = tk.Button(tela_papagaio, text="Crédito com 5% de acréscimo",command=lambda:retorna_label_acrescimo(label_total,valor_acrescimo))
    botao3.grid(column=2, row=3)
    botaoVo3=tk.Button(tela_papagaio, text='Voltar', command=tela_papagaio.destroy)
    botaoVo3.grid()      
    
  

    
janela = tk.Tk() #1º PASSO: PARA REALIZAR JANELA. sempre Tkinter inicia com esse comando e finaliza com mainloop 
janela.title('PetShop') #NOME QUE SE MOSTRARÁ EM JANELA 
janela.geometry("200x140")#LARGURA E COMPRIMENTO DA JANELA

textoInicial = tk.Label(janela, text='Escolha um animal:') #Label é onde você vai colocar o texto em sua PÁGINA
textoInicial.grid(column=2, pady=10) #Com ele você vai exibir o texto e definir em que posição ele irá aparecer 

botao = tk.Button(janela, text="Gato R$1500,00",command=gato)
botao.grid(column=2, row=1)
botao = tk.Button(janela, text="Cachorro R$2000,00", command=cachorro)
botao.grid(column=2, row=2)
botao = tk.Button(janela, text="Papagaio R$150,00", command=papagaio)
botao.grid(column=2, row=3) 

janela.mainloop() 