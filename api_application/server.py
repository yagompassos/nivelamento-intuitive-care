from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Função para limpar valores NaN
def clean_data(data):
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(item) for item in data]
    elif pd.isna(data):
        return None
    return data

# Carregando os dados
try:
    df = pd.read_csv('../scripts_sql/Relatorio_cadop.csv', encoding='utf-8', delimiter=';')
    print("Dados carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar CSV: {str(e)}")
    df = pd.DataFrame()

@app.route('/api/buscar', methods=['GET'])
def buscar_operadoras():
    try:
        termo = request.args.get('termo', '').lower().strip()
        print(f"Termo buscado: '{termo}'")
        
        if not termo:
            return jsonify({'resultados': [], 'mensagem': 'Digite um termo para buscar'})
        
        if df.empty:
            return jsonify({'resultados': [], 'mensagem': 'Dados não disponíveis'})
        
        # Colunas para busca
        colunas_busca = ['Razao_Social', 'Nome_Fantasia', 'Cidade', 'UF']
        
        # Filtra os dados
        mask = df[colunas_busca].apply(
            lambda col: col.astype(str).str.lower().str.contains(termo, na=False)
        ).any(axis=1)
        
        resultados = df[mask].head(50)
        
        # Converte para dict e limpa NaN
        resultados_dict = resultados.to_dict('records')
        resultados_clean = clean_data(resultados_dict)
        
        return jsonify({
            'resultados': resultados_clean,
            'total': len(resultados),
            'termo': termo
        })
        
    except Exception as e:
        print(f"Erro na busca: {str(e)}")
        return jsonify({
            'error': 'Erro interno',
            'mensagem': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)