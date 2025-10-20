# main.py
import os
import pandas as pd
import requests
from flask import Flask

# Criando um app Flask simples
app = Flask(__name__)

# Lendo variáveis de ambiente (que vêm dos Segredos do GitHub)
api_key = os.getenv("MINHA_API_KEY")
db_url = os.getenv("DATABASE_URL")

@app.route('/')
def home():
    print("Testando pandas:")
    df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
    print(df)
    
    print("\nTestando requests:")
    try:
        r = requests.get("https://api.github.com")
        print(f"Status da API do GitHub: {r.status_code}")
    except Exception as e:
        print(f"Erro ao testar requests: {e}")

    print("\nVariáveis de Ambiente (Segredos):")
    print(f"API Key: {'...' + api_key[-4:] if api_key else 'NÃO CONFIGURADA'}")
    print(f"DB URL: {'Configurada' if db_url else 'NÃO CONFIGURADA'}")

    return (
        f"<h1>Ambiente pronto!</h1>"
        f"<p>Status da API do GitHub: {r.status_code}</p>"
        f"<p>API Key carregada: {'Sim' if api_key else 'Não'}</p>"
        f"<p>Para ver os logs, abra o terminal do Codespace.</p>"
    )

if __name__ == "__main__":
    print("=== Iniciando Aplicação no Codespace ===")
    home() # Executa a função uma vez para mostrar os logs
    print("\n=== Iniciando servidor web na porta 8000 ===")
    app.run(host='0.0.0.0', port=8000, debug=True)
