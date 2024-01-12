from datetime import date
import tkinter as tk
import pandas as pd
from tkinter import messagebox

var1 = 1
var2 = 0

notas = " "

data_atual = date.today()

# BA02 corresponde à nota de referência

nomes_arquivos = ["nimagem_filial2","igtech_matriz","dstech_matriz","cptech_filial2","cptech_matriz","sm_matriz","gtech_matriz","rnccz_matriz","glcase_filial3","deco_matriz","gsp_filial3","gsp_matriz","dsprime_filial3","dsblack_matriz","decoskin_filial","nimagem_filial5"]

for i in range(len(nomes_arquivos)):
    select_arquivo = nomes_arquivos[i] + ".xlsx"
    nome = nomes_arquivos[i]

    itens = pd.read_excel(f"C:/Users/Usuário/Desktop/devolucao iwill/{select_arquivo}")
    for i in range(1):
        cnpj = str(itens.loc[i,'cnpj'])
        razao = str(itens.loc[i,'razão'])
        insc_estadual = str(itens.loc[i,'inscrição'])
        endereco = str(itens.loc[i,'endereço'])
        numero = str(itens.loc[i,'número'])
        cod_municipal = str(itens.loc[i,'código municipal'])
        bairro = str(itens.loc[i,'bairro'])
        cidade = str(itens.loc[i,'municipio'])
        estado = str(itens.loc[i,'estado'])
        cep = str(itens.loc[i,'cep'])        
        complemento = str(itens.loc[i,'complemento'])
        notas = notas + str(itens.loc[i,'ref']) + ","

        cabecalho_nota = f"""NOTA FISCAL|1
A|4.00|NFe
B|35|00400180|Remessa para conserto/ou Reparo|55|1|999|{data_atual}T14:00:00-00:00|{data_atual}T14:00:00-00:00|1|2|{cod_municipal}|1|1|2|1|4|0|0||3|4.01_sebrae_b043|||
BA|
BA02||
C|{razao}||{insc_estadual}||||1
C02|{cnpj}
C05|{endereco}|{numero}|{complemento}|{bairro}|{cod_municipal}|{cidade}|{estado}|04551000|1058|BRASIL|
E|IWILL BRASIL IMPORTADORA E COMERCIO DE ARTIGOS DE INFORM|1|256475199||||
E02|14028224000116|
E05|RUA PERNAMBUCO|340||ESTADOS|4202008|Balneario Camboriu|SC|00000000|1058|BRASIL|||
    """

    arquivo = open(f'C:/Users/Usuário/Desktop/test/{nome}.txt','w+')
    arquivo.writelines(cabecalho_nota)
   

    for i, produto in enumerate(itens['código']):
        codigo_produto = str(itens.loc[i,'sku'])        
        desc_produto = str(itens.loc[i,'produto'])
        ncm_produto = str(itens.loc[i,'ncm'])       
        cfop = str(itens.loc[i,'cfop'])
        qtd_produto = float(itens.loc[i,'qtd'])
        valor_un_produto = float(itens.loc[i,'preço um'])
        valor_total_produto = float(itens.loc[i,'valor total'])
        base_icms_produto = float(itens.loc[i,'base icms'])        
        aliquota_icms = float(itens.loc[i,'aliquota icms'])
        valor_icms = float(itens.loc[i,'valor icms'])

        base_ipi_produto = float(itens.loc[i,'base ipi'])                             
        aliquota_ipi = float(itens.loc[i,'aliquota ipi'])
        valor_ipi = float(itens.loc[i,'valor ipi'])

        total_nf = float(itens['valor total'].sum())
        total_icms = float(itens['valor icms'].sum())
        total_ipi = float(itens['valor ipi'].sum())

        descricao_item = f"""H|{i+1}|
    I|{codigo_produto}|{produto}||{desc_produto}|{ncm_produto}||6915|UN|{qtd_produto:.2f}|{valor_un_produto}|{valor_total_produto:.2f}|{produto}||un|{qtd_produto:.2f}|{valor_un_produto:.2f}|||||1|||||||

    M
    N
    """

        calculo_icmsipi = f"""N10h|1|900|3|{base_icms_produto:.2f}|0.00|{aliquota_icms:.2f}|{valor_icms:.2f}||||||
    O||||999
    O07|49|0.00
    O10|{base_ipi_produto:.2f}|{aliquota_ipi:.2f}|||{valor_ipi:.2f}|
    Q|
    """

    #     calculo_ipi = f"""O||||999
        
    # O07|49|{valor_ipi_produto}
    # O10|{base_ipi_produto}|{aliquota_ipi}"""


        calculo_pis = f"""Q05|98|0.00
    Q07|0.00|0.00
    S
    """

        calculo_cofins = f"""S05|98|0.00
    S07|0.00|0.00
    """

        arquivo.writelines(descricao_item)
        arquivo.writelines(calculo_icmsipi)
        
        
        arquivo.writelines(calculo_pis)
        arquivo.writelines(calculo_cofins)



    totais_nota = f"""W
    W02|{total_nf:.2f}|{total_icms:.2f}|0.00|0.00|0.00|0.00|0.00|{total_nf:.2f}|0.00||||0.00|0.00|0.00|0.00|0.00|0.00|{total_nf:.2f}
    W04c|0.00
    W04e|0.00
    W04g|0.00
    X|9|

    YA
    YA01||90||0.00|    
    """

    info_adicionais = f"""Z||Devolução referente a nf {notas} Código da Autorização de Postagem: 2676066725 - Endereço de Entrega: IWILL BRASIL IMPORTADORA E COMERCIO DE ARTIGOS DE INFORMATICA, Rodovia BR-101 - 131 Galpão 5B - Trade Park, Várzea do Ranchinho (Monte Alegre), Camboriú - SC, CEP: 88349-175|"""


    arquivo.writelines(totais_nota)

    arquivo.writelines(info_adicionais)

    messagebox.showinfo(message="Arquivo de devolução gerado!")
        
            