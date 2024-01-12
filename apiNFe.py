from pynfe.processamento.comunicacao import ComunicacaoSefaz

certificado = "C:/Users/Usuário/Desktop/bramport.pfx"
senha = 'Deco80'
uf = 'sp'
homologacao = True


con = ComunicacaoSefaz(uf,certificado,senha,homologacao)
xml = con.status_servico('nfe')

print(xml.text)