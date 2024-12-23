import os
import shutil
import xml.etree.ElementTree as ET

palavra_especifica = 'decoskin'
pasta_destino = "C:/Users/Usuário/Desktop/arquivos"
pasta_principal = "Rede//192.168.2.121/contmatic/MFD 2019"

for pasta in os.listdir(pasta_principal):
    # Construa o caminho completo para cada pasta
    caminho_pasta = os.path.join(pasta_principal, pasta)
    
    # Verifique se é uma pasta
    if os.path.isdir(caminho_pasta):
        # Itere sobre todos os arquivos dentro da pasta
        for arquivo in os.listdir(caminho_pasta):
            # Verifique se é um arquivo XML
            if arquivo.endswith('.xml'):
                # Abra o arquivo XML usando ElementTree
                caminho_arquivo = os.path.join(caminho_pasta, arquivo)
                tree = ET.parse(caminho_arquivo)
                root = tree.getroot()

                if palavra_especifica in ET.tostring(root).decode('utf-8'):
                    # Se a palavra estiver presente, copie o arquivo para a pasta de destino
                    destino_arquivo = os.path.join(pasta_destino, pasta, arquivo)
                    os.makedirs(os.path.dirname(destino_arquivo), exist_ok=True)
                    shutil.copy(caminho_arquivo, destino_arquivo)