from curl_cffi import requests
from bs4 import BeautifulSoup
import zipfile
import os

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def nova_session():
    session = requests.Session(impersonate="chrome")
    return session

def download_pdf(session, pdf_url, pdf_path):
    try:
        print("baixando arquivo ", pdf_path)
        response = session.get(pdf_url)
        response.raise_for_status()
            
        with open(pdf_path, 'wb') as file:
            file.write(response.content)
                        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o arquivo {pdf_path}: {e}")
        return False

def main(): 
    session = nova_session()
    
    try:
        print("Obtendo página principal...")
        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        anexo1_link = None
        anexo2_link = None
        
        print("Procurando links dos anexos...")
        for link in soup.find_all("a", href=True):
            link_text = link.text.strip()
            if "Anexo II" in link_text:
                anexo2_link = link["href"]
                print(f"Anexo II encontrado: {anexo2_link}")
            elif "Anexo I" in link_text and link["href"].lower().endswith(".pdf"):
                anexo1_link = link["href"]
                print(f"Anexo I encontrado: {anexo1_link}")

        success = True

        os.makedirs('Arquivos_Gerados', exist_ok=True)
        
        if anexo1_link:
            if not download_pdf(session, anexo1_link, "Arquivos_Gerados/anexo1.pdf"):
                success = False
        else:
            print("Anexo I não encontrado")
            success = False

        if anexo2_link:
            if not download_pdf(session, anexo2_link, "Arquivos_Gerados/anexo2.pdf"):
                success = False
        else:
            print("Anexo II não encontrado")
            success = False

        if success:
            print("Criando arquivo ZIP...")
            with zipfile.ZipFile('Arquivos_Gerados/Anexos.zip', 'w') as zipf:
                if os.path.exists('Arquivos_Gerados/anexo1.pdf'):
                    zipf.write('Arquivos_Gerados/anexo1.pdf')
                if os.path.exists('Arquivos_Gerados/anexo2.pdf'):
                    zipf.write('Arquivos_Gerados/anexo2.pdf')
            print("Processo concluído com sucesso! A pasta se encontra dentro de 'Arquivos_Gerados'.")
        else:
            print("Processo concluído com erros. Verifique os logs acima.")

    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()