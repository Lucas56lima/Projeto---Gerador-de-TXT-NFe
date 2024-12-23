from datetime import date
import tkinter as tk
import pandas as pd
from tkinter import messagebox

notas = " "

data_atual = date.today()

info_principal = pd.read_excel("Z:/FISCAL/Emitir notas pelo gratuito/layout_dev.xlsb",sheet_name="principal")

grouped_by_cnpj = info_principal.groupby("cnpj")
nomes_arquivos = []

for cnpj, group in grouped_by_cnpj:
    cnpj = str(group.iloc[0]["cnpj"])   
    if len(cnpj) < 14:
        cnpj = "0" + cnpj

    id_cnpj = cnpj[11]
    nome_loja = str(group.iloc[0]["razão"]).split()  # Juntar palavras com underscore
    if id_cnpj == "1":
        nome_abrev = nome_loja[0].lower() + " " + nome_loja[1].lower()
        arquivo_excel = f"{nome_abrev}_matriz.xlsx"
        nomes_arquivos.append(arquivo_excel)
    else:
        nome_abrev = nome_loja[0].lower() + " " + nome_loja[1].lower()
        arquivo_excel = f"{nome_abrev}_filial{id_cnpj}.xlsx"
        nomes_arquivos.append(arquivo_excel)

    group.to_excel(f"Z:/FISCAL/Emitir notas pelo gratuito/Arquivos Excel - Devolução/{arquivo_excel}",index=False)
# Dados do destinario
info_destinatario = pd.read_excel("Z:/FISCAL/Emitir notas pelo gratuito/layout_dev.xlsb",sheet_name="base")
cnpj_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.CNPJ"])
razao_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.xNome"])
insc_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.IE"])
logadouro_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.xLgr"])
bairro_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.xBairro"])
cod_municipal_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.cMun"])
municipio_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.xMun"])
estado_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.UF"])
cep_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.CEP"])
numero_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.nro"])
compl_destinatario = str(info_destinatario.loc[1,"NFe.infNFe.emit.enderEmit.xCpl"])

if numero_destinatario == "0":
    numero_destinatario = "S/N"

if len(cep_destinatario) < 8:
    cep_destinatario = "0" + cep_destinatario

if len(cnpj_destinatario) < 14:
    cnpj_destinatario = "0" + cnpj_destinatario

# nomes_arquivos = ["gl case filial3.xlsx","deco skin filial.xlsx","ds black matriz.xlsx","dsmg matriz.xlsx","bramport filial8.xlsx","ds prime matriz.xlsx" ]
for i in range(len(nomes_arquivos)):
    select_arquivo = nomes_arquivos[i]
    nome = nomes_arquivos[i]

    itens = pd.read_excel(f"Z:/FISCAL/Emitir notas pelo gratuito/Arquivos Excel - Devolução/{select_arquivo}")
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
        codigo_estadual = str(itens.loc[i,'código estadual'])
        if len(cep) < 8:
            cep = "0" + cep

        if len(cnpj) < 14:
            cnpj = "0" + cnpj       
        complemento = str(itens.loc[i,'complemento'])        
        notas = notas + str(itens.loc[i,'ref']) + ","        
        cabecalho_nota = f"""NOTA FISCAL|1
A|4.00|NFe
B|{codigo_estadual}|00400180|Remessa para Conserto|55|1|999|{data_atual}T12:00:00-00:00|{data_atual}T12:00:00-00:00|1|1|{cod_municipal}|1|1|2|1|1|0|0||3|4.01_sebrae_b043|||
 """
    arquivo = open(f'C:/Users/Usuário/Desktop/test/{nome.replace(".xlsx","")}.txt','w+')
    arquivo.writelines(cabecalho_nota)
    nota_referencia = ""
    for i, produto in enumerate(itens['produto']):
        nota_ref = str(itens.loc[i,'chave'])                  
        if nota_ref != "":

# BA02 corresponde à nota de referência
            nota_referencia = f"""
BA|
BA02|{nota_ref}|"""
        arquivo.writelines(nota_referencia)
        

    cabecalho_nota2 = f"""
C|{razao}||{insc_estadual}||||1
C02|{cnpj}
C05|{endereco}|{numero}|{complemento}|{bairro}|{cod_municipal}|{cidade}|{estado}|{cep
}|1058|BRASIL|
E|{razao_destinatario}|1|{insc_destinatario}||||
E02|{cnpj_destinatario}|
E05|{logadouro_destinatario}|{numero_destinatario}|{compl_destinatario}|{bairro_destinatario}|{cod_municipal_destinatario}|{municipio_destinatario}|{estado_destinatario}|{cep_destinatario}|1058|BRASIL|||
"""

    arquivo.writelines(cabecalho_nota2)   

    for i, produto in enumerate(itens['código']):
        codigo_produto = str(itens.loc[i,'sku'])        
        desc_produto = str(itens.loc[i,'produto'])
        ncm_produto = str(itens.loc[i,'ncm'])
        unidade_medida = str(itens.loc[i,'unidade'])       
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
I|{codigo_produto}|{produto}||{desc_produto}|{ncm_produto}||{cfop}|{unidade_medida}|{qtd_produto:.2f}|{valor_un_produto}|{valor_total_produto:.2f}|{produto}||{unidade_medida}|{qtd_produto:.2f}|{valor_un_produto:.2f}|||||1|||||||
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

    info_adicionais = f"""Z||Devolução referente a nf {notas} |"""


    arquivo.writelines(totais_nota)

    arquivo.writelines(info_adicionais)
    
messagebox.showinfo(message="Arquivos de devolução gerados!")
    
        