from datetime import date
import tkinter as tk
import pandas as pd
from tkinter import messagebox

# Função para gerar o cabeçalho da nota fiscal
def gerar_cabecalho(itens, data_atual):
    cnpj = str(itens.loc[1, "ns1:CNPJ"]).zfill(14)
    razao = itens.loc[1, "ns1:xNome"]
    inscricao = str(itens.loc[1, "ns1:IE"])
    fantasia = itens.loc[1, "ns1:xFant"]
    bairro = itens.loc[1, "ns1:xBairro"]
    numero = itens.loc[1, "ns1:nro"]
    logradouro = itens.loc[1, "ns1:xLgr"]
    cep = str(itens.loc[1, "ns1:CEP"]).zfill(8)
    fornecedor = itens.loc[1, "ns1:xNome2"]
    log_fornecedor = itens.loc[1, "ns1:xLgr3"]
    cod_fornecedor = itens.loc[1, "ns1:cPais10"]
    bairro_fornecedor = itens.loc[1, "ns1:xBairro5"]
    pais_fornecedor = itens.loc[1, "ns1:xPais11"]

    return f"""NOTA FISCAL|1
A|4.00|NFe
B|35||IMPORTACAO|55|1|999|{data_atual}T00:00:00-03:00|{data_atual}T00:00:00-03:00|0|3|3550308|1|1||1|1|0|0||0|4.01_sebrae_b043||
C|{razao}|{fantasia}|{inscricao}||||1
C02|{cnpj}
C05|{logradouro}|{numero}||{bairro}|3550308|SAO PAULO|SP|04551000|1058|BRASIL|1125033310
E|{fornecedor}|9||||
E05|{log_fornecedor}|.|{bairro_fornecedor}|.|9999999|Exterior|EX|00000000|{cod_fornecedor}|{pais_fornecedor}|

"""

# Função para processar itens
def processar_itens(itens, arquivo, data_atual):
    for i, produto in enumerate(itens['ns1:cProd']):
        # Extração de dados
        codigo_produto = str(itens.loc[i, 'ns1:cProd'])
        desc_produto = str(itens.loc[i, 'ns1:xProd'])
        ncm_produto = str(itens.loc[i, 'ns1:NCM'])
        un_produto = str(itens.loc[i, 'ns1:uCom'])
        qtd_produto = float(itens.loc[i, 'ns1:qCom'])
        valor_un_produto = float(itens.loc[i, 'ns1:vUnCom'])
        valor_total_produto = float(itens.loc[i, 'ns1:vProd'])
        base_icms_produto = float(itens.loc[i, 'ns1:vBC'])
        valor_icms_produto = float(itens.loc[i, 'ns1:vICMS'])
        aliquota_icms = float(itens.loc[i, 'ns1:pICMS'])
        
        # Descrição do item
        descricao_item = f"""H|{i + 1}|
I|{codigo_produto}|||{desc_produto}|{ncm_produto}||3102|{un_produto}|{qtd_produto:.2f}|{valor_un_produto:.2f}|{valor_total_produto:.2f}|||{un_produto}|{qtd_produto:.2f}|{valor_un_produto:.2f}||||1||
"""
        calculo_icms = f"""N10h|1|900|3|{base_icms_produto:.2f}|0.00|{aliquota_icms:.2f}|{valor_icms_produto:.2f}||||||
"""
        # Escrevendo no arquivo
        arquivo.writelines(descricao_item)
        arquivo.writelines(calculo_icms)

# Função principal
def gerar_arquivo_importacao():
    data_atual = date.today()
    caminho_entrada = "Z:/FISCAL/Emitir notas pelo gratuito/layout_imp.xlsx"
    caminho_saida = "C:/Users/Usuário/Desktop/importacao.txt"

    # Carregando os dados do Excel
    itens = pd.read_excel(caminho_entrada, sheet_name="Planilha2")
    
    # Criando e escrevendo o arquivo
    with open(caminho_saida, 'w') as arquivo:
        # Cabeçalho
        cabecalho = gerar_cabecalho(itens, data_atual)
        arquivo.writelines(cabecalho)

        # Itens
        processar_itens(itens, arquivo, data_atual)

    # Exibindo mensagem de sucesso
    messagebox.showinfo(message="Arquivo de importação gerado com sucesso!")

# Execução do programa
if __name__ == "__main__":
    gerar_arquivo_importacao()
