import tkinter as tk
from tkinter import *
from tkinter import messagebox

#------------------------- Tela Pagamentos -----------------------------------------------------
lista_total = []
lista_pay = [" ","Cartão de Débito","Cartão de Crédito","Pix","Dinheiro"]

def mensagem_compra():
     messagebox.showinfo(message="Compra confirmada, muito obrigado pela prefência!")
    
def confirmar_compra():
    select = int(label_pay.get())
    
    if lista_pay[select] != " " and lista_pay[select] == "Cartão de Débito" or lista_pay[select] == "Pix":       
        valor_total = lista_total[0] - lista_total[0] * 0.05
        messagebox.showinfo(message=f"O valor total é {valor_total:.2f} com 5% de desconto")    

    elif lista_pay[select] != " " and lista_pay[select] == "Dinheiro":        
        valor_total = lista_total[0] - lista_total[0] * 0.08
        messagebox.showinfo(message=f"O valor total é {valor_total:.2f} com 8% de desconto")

    else:
        valor_total = lista_total[0] + lista_total[0] * 0.05
        messagebox.showinfo(message=f"O valor total é {valor_total:.2f} com 5% de acréscimo")  

# ------------------------ Adiciona Quantidade de animais pelo Entry epelo Botão ----------------
def adiciona_qtd_animal(label): 
    soma_qtd = int(label.get()) 
    soma_qtd = soma_qtd + 1
    label.delete(0,tk.END) 
    label.insert(0,f"{soma_qtd}")
#------------------------ Remove quantidade pelo botão --------------------------------------------------------------
def remove_qtd_animal(label): 
    soma_qtd = int(label.get())
    if soma_qtd > 0: 
        soma_qtd = soma_qtd - 1
        label.delete(0,tk.END) 
        label.insert(0,f"{soma_qtd}")
#--------------------------------------------------------------------------------------------

def carrinho_soma():
    cachorro = int(label_qtd.get()) * 100
    gato = int(label_qtd2.get()) * 20
    tubarao = int(label_qtd3.get()) * 500
    dragao = int(label_qtd4.get()) * 600
    leviatan = int(label_qtd5.get()) * 1000
    resultado = int(cachorro + gato + tubarao + dragao + leviatan)  
    label_carrinho.config(text=f"Total: {resultado:.2f}")
    lista_total.append(resultado) 

tela = tk.Tk()
tela.title("Mercado clandestino de animais")
tela.geometry("500x300")
nome_janela = tk.Label(tela, text = "MERCADO CLANDESTINO DE ANIMAIS")

label_animal1 = tk.Label(tela,text=f"Cachorro = R$100")
label_animal2 = tk.Label(tela,text=f"Gato = R$200")
label_animal3 = tk.Label(tela,text=f"Tubarão = R$500")

label_animal4 = tk.Label(tela,text=f"Dragão = R$600")
label_animal5 = tk.Label(tela,text=f"Leviathan = R$1000")
label_carrinho = tk.Label(tela,text=f"total")

#----------------------------- Inputs -------------------------------------------------
label_qtd = tk.Entry(tela)
label_qtd.insert(0,"0")
label_qtd2 = tk.Entry(tela)
label_qtd2.insert(0,"0")
label_qtd3 = tk.Entry(tela)
label_qtd3.insert(0,"0")
label_qtd4 = tk.Entry(tela)
label_qtd4.insert(0,"0")
label_qtd5 = tk.Entry(tela)
label_qtd5.insert(0,"0")

btn_mais = tk.Button(tela, text="+",command=lambda:adiciona_qtd_animal(label_qtd))
btn_menos = tk.Button(tela, text="-",command=lambda:remove_qtd_animal(label_qtd))
btn_mais2 = tk.Button(tela, text="+",command=lambda:adiciona_qtd_animal(label_qtd2))
btn_menos2 = tk.Button(tela, text="-",command=lambda:remove_qtd_animal(label_qtd2))
btn_mais3 = tk.Button(tela, text="+",command=lambda:adiciona_qtd_animal(label_qtd3))
btn_menos3 = tk.Button(tela, text="-",command=lambda:remove_qtd_animal(label_qtd3))
btn_mais4 = tk.Button(tela, text="+",command=lambda:adiciona_qtd_animal(label_qtd4))
btn_menos4 = tk.Button(tela, text="-",command=lambda:remove_qtd_animal(label_qtd4))
btn_mais5 = tk.Button(tela, text="+",command=lambda:adiciona_qtd_animal(label_qtd5))
btn_menos5 = tk.Button(tela, text="-",command=lambda:remove_qtd_animal(label_qtd5))
btn_carrinho = tk.Button(tela,text="Adicionar ao Carrinho",command=carrinho_soma)
btn_comprar = tk.Button(tela, text="Ir para Pagamento",command=tela.destroy)

#--------------------------- Posicionamento dos elementos -------------------------------
btn_comprar.grid(row=12,column=9)
btn_mais.grid(row=1,column=11)
btn_menos.grid(row=1,column=10)
btn_mais2.grid(row=2,column=11)
btn_menos2.grid(row=2,column=10)
btn_mais3.grid(row=3,column=11)
btn_menos3.grid(row=3,column=10)
btn_mais4.grid(row=4,column=11)
btn_menos4.grid(row=4,column=10)
btn_mais5.grid(row=5,column=11)
btn_menos5.grid(row=5,column=10)
btn_carrinho.grid(row=10,column=9)
label_qtd.grid(row=1,column=9)
label_qtd2.grid(row=2,column=9)
label_qtd3.grid(row=3,column=9)
label_qtd4.grid(row=4,column=9)
label_qtd5.grid(row=5,column=9)
nome_janela.grid(row=0,column=9)
label_animal1.grid(row=1,column=8)
label_animal2.grid(row=2,column=8)
label_animal3.grid(row=3,column=8)
label_animal4.grid(row=4,column=8)
label_animal5.grid(row=5,column=8)

label_carrinho.grid(row=11,column=9)

tela.mainloop()

tela_pagamento = tk.Tk()

tela_pagamento.title("Pagamento")
tela_pagamento.geometry("500x300")
label_debito = tk.Label(tela_pagamento,text="1 - Cartão de Débito")
label_debito.grid(row=0,column=2,padx=200,pady=10)
label_credito = tk.Label(tela_pagamento,text="2 - Cartão de Crédito")
label_credito.grid(row=2,column=2,padx=200,pady=10)
label_pix = tk.Label(tela_pagamento,text="3 - Pix")
label_pix.grid(row=4,column=2,padx=200,pady=10)
label_dinheiro = tk.Label(tela_pagamento,text=f"4 - Dinheiro")
label_dinheiro.grid(row=6,column=2,padx=200,pady=10)
label_pay = tk.Entry(tela_pagamento)
label_pay.grid(row=8,column=2,padx=200,pady=10)
label_total = tk.Label(tela_pagamento,text=f"total:")
label_total.grid(row=10, column=2,padx=200,pady=10)   
label_pay = tk.Entry(tela_pagamento)
label_pay.insert(0,"0")
label_pay.grid(row=8,column=2,padx=200,pady=10)   

btn_total = tk.Button(tela_pagamento,text="Selecionar Pagamento",command=confirmar_compra)    
btn_total.grid(row=12,column=2)
btn_confirm = tk.Button(tela_pagamento,text="Confirmar Compra",command=mensagem_compra)    
btn_confirm.grid(row=14,column=2)         
    
tela_pagamento.mainloop()