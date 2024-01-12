from datetime import date
import tkinter as tk
import pandas as pd
from tkinter import messagebox

var1 = 1
var2 = 0

def emite_nota(check_box1,check_box2,cnpj):
    data_atual = date.today()
    if check_box1 == 1 and check_box2 == 0:
        cabecalho_nota = f"""NOTA FISCAL|1
        A|4.00|NFe
        B|35||IMPORTACAO|55|1|999|{data_atual}T00:00:00-03:00|{data_atual}T00:00:00-03:00|0|3|3550308|1|1||1|1|0|0||0|4.01_sebrae_b043||
        C|N-IMAGEM PERSONALIZACAO E ACESSORIOS PARA GADGETS EIRELI-E|N-IMAGEM|143307882119||||1
        C02|{cnpj}
        C05|RUA OLIMPIADAS|360|LUC 103|VILA OLIMPIA|3550308|SAO PAULO|SP|04551000|1058|BRASIL|1125033310
        E|HONOUR GOLD LIMITED|9||||
        E03a|
        E05|NO. 07,FL9, YONG AN ST|.|XIN DIAN DIST|.|9999999|Exterior|EX|00000000|1619|FORMOSA (TAIWAN)|
        
        """

        arquivo = open('C:/Users/Usuário/Desktop/importacao.txt','w+')
        arquivo.writelines(cabecalho_nota) 

        itens = pd.read_excel("C:/Users/Usuário/Desktop/layout_nota.xlsx")

        for i, produto in enumerate(itens['código']):
            codigo_produto = str(itens.loc[i,'código'])
            desc_produto = str(itens.loc[i,'descrição'])
            ncm_produto = str(itens.loc[i,'ncm'])
            clfiscal_produto = str(itens.loc[i,'class fiscal'])
            un_produto = str(itens.loc[i,'uni'])
            qtd_produto = float(itens.loc[i,'quantidade'])
            valor_un_produto = float(itens.loc[i,'vl unit'])
            valor_total_produto = float(itens.loc[i,'vl total'])
            base_icms_produto = float(itens.loc[i,'base icms'])
            valor_icms_produto = float(itens.loc[i,'vl icms'])
            base_ipi_produto = float(itens.loc[i,'base ipi'])
            valor_ipi_produto = float(itens.loc[i,'vl ipi'])
            base_piscofins_produto = float(itens.loc[i,'base pis/cofins'])
            valor_pis_produto = float(itens.loc[i,'vl pis'])
            valor_cofins_produto = float(itens.loc[i,'vl cofins'])
            valor_afrmm_produto = float(itens.loc[i,'afrmm'])
            valor_total2_produto = float(itens.loc[i,'vl 2'])
            aliquota_icms = float(itens.loc[i,'aliquota icms'])
            aliquota_ipi = float(itens.loc[i,'aliquota ipi'])
            aliquota_pis = float(itens.loc[i,'aliquota pis'])
            aliquota_cofins = float(itens.loc[i,'aliquota cofins'])

            descricao_item = f"""H|{i+1}|
        I|{codigo_produto}|||{desc_produto}|{ncm_produto}||3102|{un_produto}|{qtd_produto:.2f}|{valor_un_produto}|{valor_total_produto:.2f}|||{un_produto}|{qtd_produto:.2f}|{valor_un_produto:.2f}||||5925.84|1||
        I05a|AA9999
        I18|23/2401624-8|{data_atual}|AEROPORTO INTERNACIONAL DE SAO PAULO/GUARULHOS|SP|{data_atual}|4||1|19843146000127|SP|0007
        I25|2|1|0007||
        M
        N
        """

            calculo_icmsipi = f"""N10h|1|900|3|{base_icms_produto:.2f}|0.00|{aliquota_icms:.2f}|{valor_icms_produto:.2f}||||||
        O||||999
        O07|49|{valor_ipi_produto:.2f}
        O10|{base_ipi_produto:.2f}|{aliquota_ipi:.2f}
        """

        #     calculo_ipi = f"""O||||999
        # O07|49|{valor_ipi_produto}
        # O10|{base_ipi_produto}|{aliquota_ipi}"""

            calculo_afrmm = f"""P|{base_piscofins_produto:.2f}|0.00|{valor_afrmm_produto:.2f}|0.00
        Q
        """

            calculo_pis = f"""Q05|98|{valor_pis_produto:.2f}
        Q07|{base_piscofins_produto:.2f}|{aliquota_pis:.2f}
        S
        """

            calculo_cofins = f"""S05|98|{valor_cofins_produto:.2f}
        S07|{base_piscofins_produto:.2f}|{aliquota_cofins:.2f}
        """

            arquivo.writelines(descricao_item)
            arquivo.writelines(calculo_icmsipi)
            
            arquivo.writelines(calculo_afrmm)
            arquivo.writelines(calculo_pis)
            arquivo.writelines(calculo_cofins)



        totais_nota = f"""W
        W02|196295.50|35333.19|0.00|0.00|0.00|0.00|0.00|0.00|134225.41||||19959.09|13086.98|0.00|2399.58|11026.70|13649.92|196295.50
        W04c|0.00
        W04e|0.00
        W04g|0.00
        X|0
        """


        transportadora = f"""X03|MARCOS FERREIRA DE OLIVEIRA TRA NSPORTES|336669232115|R ELVIS PRESLEY, 20|GUARULHOS|SP
        X04|04460304000192
        X26|63|OUTROS|.|S/N|1001.380|1043.000
        YA
        YA01||15||196295.50
        """

        info_adicionais = f"""Z| |N/Ref OZZY007-23   - S/Ref PELICULAS - DI 23/2401624-8  06/12/23 - Tx.Siscomex R$ 223,64 - Valor PIS R$ 2.399,58 - Valor COFINS R$ 11.026,70 -
        """


        arquivo.writelines(totais_nota)
        arquivo.writelines(transportadora)
        arquivo.writelines(info_adicionais)

        messagebox.showinfo(message="Arquivo de importação gerado!")
    elif check_box1 == 0 and check_box2 == 1:
            cabecalho_nota = f"""NOTA FISCAL|1
            A|4.00|NFe
            B|35||DEVOLUÇÃO|55|1|999|{data_atual}T00:00:00-03:00|{data_atual}T00:00:00-03:00|0|3|3550308|1|1||1|1|0|0||0|4.01_sebrae_b043||
            C|N-IMAGEM PERSONALIZACAO E ACES SSORIOS PARA GADGETS EIRELI-E|N-IMAGEM|143307882119||||1
            C02|{cnpj}
            C05|RUA OLIMPIADAS|360|LUC 103|VILA OLIMPIA|3550308|SAO PAULO|SP|04551000|1058|BRASIL|1125033310
            E|HONOUR GOLD LIMITED|9||||
            E03a|
            E05|NO. 07,FL9, YONG AN ST|.|XIN DIAN DIST|.|9999999|Exterior|EX|00000000|1619|FORMOSA (TAIWAN)|

            """

            arquivo = open('C:/Users/Usuário/Desktop/devolucao.txt','w+')
            arquivo.writelines(cabecalho_nota) 

            itens = pd.read_excel("C:/Users/Usuário/Desktop/layout_nota.xlsx")

            for i, produto in enumerate(itens['código']):
                codigo_produto = str(itens.loc[i,'código'])
                desc_produto = str(itens.loc[i,'descrição'])
                ncm_produto = str(itens.loc[i,'ncm'])
                clfiscal_produto = str(itens.loc[i,'class fiscal'])
                un_produto = str(itens.loc[i,'uni'])
                qtd_produto = float(itens.loc[i,'quantidade'])
                valor_un_produto = float(itens.loc[i,'vl unit'])
                valor_total_produto = float(itens.loc[i,'vl total'])
                base_icms_produto = float(itens.loc[i,'base icms'])
                valor_icms_produto = float(itens.loc[i,'vl icms'])
                base_ipi_produto = float(itens.loc[i,'base ipi'])
                valor_ipi_produto = float(itens.loc[i,'vl ipi'])
                base_piscofins_produto = float(itens.loc[i,'base pis/cofins'])
                valor_pis_produto = float(itens.loc[i,'vl pis'])
                valor_cofins_produto = float(itens.loc[i,'vl cofins'])
                valor_afrmm_produto = float(itens.loc[i,'afrmm'])
                valor_total2_produto = float(itens.loc[i,'vl 2'])
                aliquota_icms = float(itens.loc[i,'aliquota icms'])
                aliquota_ipi = float(itens.loc[i,'aliquota ipi'])
                aliquota_pis = float(itens.loc[i,'aliquota pis'])
                aliquota_cofins = float(itens.loc[i,'aliquota cofins'])

                descricao_item = f"""H|{i+1}|
            I|{codigo_produto}|||{desc_produto}|{ncm_produto}||3102|{un_produto}|{qtd_produto:.2f}|{valor_un_produto}|{valor_total_produto:.2f}|||{un_produto}|{qtd_produto:.2f}|{valor_un_produto:.2f}||||5925.84|1||
            I05a|AA9999
            I18|23/2401624-8|{data_atual}|AEROPORTO INTERNACIONAL DE SAO PAULO/GUARULHOS|SP|{data_atual}|4||1|19843146000127|SP|0007
            I25|2|1|0007||
            M
            N
            """

                calculo_icmsipi = f"""N10h|1|900|3|{base_icms_produto:.2f}|0.00|{aliquota_icms:.2f}|{valor_icms_produto:.2f}||||||
            O||||999
            O07|49|{valor_ipi_produto:.2f}
            O10|{base_ipi_produto:.2f}|{aliquota_ipi:.2f}
            """

            #     calculo_ipi = f"""O||||999
            # O07|49|{valor_ipi_produto}
            # O10|{base_ipi_produto}|{aliquota_ipi}"""

                calculo_afrmm = f"""P|{base_piscofins_produto:.2f}|0.00|{valor_afrmm_produto:.2f}|0.00
            Q
            """

                calculo_pis = f"""Q05|98|{valor_pis_produto:.2f}
            Q07|{base_piscofins_produto:.2f}|{aliquota_pis:.2f}
            S
            """

                calculo_cofins = f"""S05|98|{valor_cofins_produto:.2f}
            S07|{base_piscofins_produto:.2f}|{aliquota_cofins:.2f}
            """

                arquivo.writelines(descricao_item)
                arquivo.writelines(calculo_icmsipi)
                
                arquivo.writelines(calculo_afrmm)
                arquivo.writelines(calculo_pis)
                arquivo.writelines(calculo_cofins)



            totais_nota = f"""W
            W02|196295.50|35333.19|0.00|0.00|0.00|0.00|0.00|0.00|134225.41||||19959.09|13086.98|0.00|2399.58|11026.70|13649.92|196295.50
            W04c|0.00
            W04e|0.00
            W04g|0.00
            X|0
            """


            transportadora = f"""X03|MARCOS FERREIRA DE OLIVEIRA TRA NSPORTES|336669232115|R ELVIS PRESLEY, 20|GUARULHOS|SP
            X04|04460304000192
            X26|63|OUTROS|.|S/N|1001.380|1043.000
            YA
            YA01||15||196295.50
            """

            info_adicionais = f"""Z| |N/Ref OZZY007-23   - S/Ref PELICULAS - DI 23/2401624-8  06/12/23 - Tx.Siscomex R$ 223,64 - Valor PIS R$ 2.399,58 - Valor COFINS R$ 11.026,70 -
            """


            arquivo.writelines(totais_nota)
            arquivo.writelines(transportadora)
            arquivo.writelines(info_adicionais)

            messagebox.showinfo(message="Arquivo de importação gerado!")

janela = tk.Tk()
janela.geometry("300x150")
janela.config(background="#FFFAFA")
janela.title("Gerador de XML")

c1 = tk.Checkbutton(janela,variable=var1, text='Devolução', onvalue=1, offvalue=0)

c2 = tk.Checkbutton(janela, variable=var2, text='Importação',onvalue=1, offvalue=0)


label_cnpj = tk.Label(janela,text="CNPJ")
insert_cnpj = tk.Entry(janela)
btn = tk.Button(janela,text="Gerar",command=emite_nota(c1,c2,insert_cnpj))

label_cnpj.pack()
insert_cnpj.pack()
c2.pack()
c1.pack()
btn.pack()

janela.mainloop()
