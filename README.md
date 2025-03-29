# nivelamento-intuitive-care

Destinado ao PS da Intuitive Care

## Configuração e Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/yagompassos/nivelamento-intuitive-care
   cd nivelamento-intuitive-care
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Fase 1. TESTE DE WEB SCRAPING
Execute o script correspondente a fase 1:
```sh
python scraper.py
```

Os arquivos aparecerão na pasta `Arquivos_Gerados`, criada pós rodar o script.

## Fase 2. TESTE DE TRANSFORMAÇÃO DE DADOS
Execute o script correspondente a fase 2:
```sh
python transformacao.py
```

Os arquivos aparecerão na pasta `Arquivos_Gerados`.

## Fase 3. TESTE DE BANCO DE DADOS
Os scripts foram desenvolvidos para MySQL 8 e estão dentro da pasta `scripts_sql`.

Não é possível baixar arquivos em scripts .sql, por isso o csv foi baixado e incluído junto a pasta.

Para a importação dos dados do CSV, se feito no MySQL WorkBench, é necessário [desativar a configuração do -secure-file-priv](https://stackoverflow.com/questions/32737478/how-should-i-resolve-secure-file-priv-in-mysql)

## Fase 4. TESTE DE API
Toda essa fase foi desenvolvida dentro do diretório `api_application`

Para rodar, certifique-se de já ter instalado os requirements, ensinado na etapa de Configuração e instalação, no início desse documento.

Rode o back-end com o comando:
```sh
python api_application/server.py
```

Agora, em outro terminal, abra o arquivo do front-end:
```sh
cd api_application/frontend-operadoras
```

Instale as dependências com:
```sh
npm isntall
```

Inicie o servidor Vue:
```sh
npm run dev
```

Ele roda, por padrão, na porta 5173. Acesse: http://localhost:5173