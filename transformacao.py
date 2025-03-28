import pdfplumber
import pandas as pd
import zipfile
import os

if not os.path.exists('Arquivos_Gerados/'):
    print('Pasta /Arquivos_Gerados/ não existe.')
    print('Você deve rodar o script scraper.py primeiro. (tente: python scraper.py ou leia o README.md)')
    raise FileNotFoundError('Pasta /Arquivos_Gerados/ não encontrada. O script será encerrado.')

dados = []

# abre o PDF e extrai as tabelas
with pdfplumber.open("Arquivos_Gerados/anexo1.pdf") as pdf:
    print('Abrindo PDF e extraíndo Tabelas. Número de páginas:', len(pdf.pages))
    for pagina in pdf.pages[2:]: 
        tabela = pagina.extract_table()
        if tabela:
            print('pagina:', pagina.page_number, '- Tabela extraída.')
            dados.extend(tabela[1:]) 
        else:
            print('pagina:', pagina.page_number, '- Tabela não encontrada')

colunas = ["PROCEDIMENTO", "RN (alteração)", "VIGÊNCIA", "Seg. Odontológica", "Seg. Ambulatorial", "HCO", "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"]

df = pd.DataFrame(dados, columns=colunas)

df.replace("OD", "Seg. Odontológica", inplace=True)
df.replace("AMB", "Seg. Ambulatorial", inplace=True)

# Salva tudo em um CSV
df.to_csv("Arquivos_Gerados/dados_extraidos.csv", index=False, encoding="utf-8")

print("Extração concluída! CSV gerado com sucesso na pasta /Arquivos_Gerados/.")

with zipfile.ZipFile('Arquivos_Gerados/Teste_Yago.zip', 'w') as zipf:
    if os.path.exists('Arquivos_Gerados/dados_extraidos.csv'):
        zipf.write('Arquivos_Gerados/dados_extraidos.csv')

print("Arquivo ZIP criado com sucesso na pasta /Arquivos_Gerados/!")