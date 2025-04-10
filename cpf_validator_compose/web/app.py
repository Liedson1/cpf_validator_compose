# webapp/app.py
import os
import requests
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)

VALIDATION_SERVER_URL = os.environ.get('VALIDATION_SERVER_URL', 'http://server:5000/validate')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cpf_input = request.form.get('cpf')
        if not cpf_input:
            flash('Por favor, digite um CPF.', 'error')
            return redirect(url_for('index'))

        payload = {"cpf": cpf_input}
        result_message = None
        message_category = 'error' 

        try:
            print(f"WEBAPP: Enviando CPF '{cpf_input}' para {VALIDATION_SERVER_URL}")
            response = requests.post(VALIDATION_SERVER_URL, json=payload, timeout=10)
            response.raise_for_status() 

            result = response.json()
            print(f"WEBAPP: Resposta recebida: {result}")

            if result.get('is_valid'):
                result_message = f"O CPF '{cpf_input}' é VÁLIDO."
                message_category = 'success'
            else:
                result_message = f"O CPF '{cpf_input}' é INVÁLIDO."
                message_category = 'info' 

        except requests.exceptions.ConnectionError:
            result_message = f"Erro: Não foi possível conectar ao servidor de validação em {VALIDATION_SERVER_URL}."
            print(f"WEBAPP: Erro de conexão.")
        except requests.exceptions.Timeout:
            result_message = "Erro: A requisição para o servidor de validação expirou (timeout)."
            print(f"WEBAPP: Timeout.")
        except requests.exceptions.RequestException as e:
            result_message = f"Erro na comunicação com o servidor: {e}"
            print(f"WEBAPP: Erro na requisição: {e}")
            if response is not None:
                 print(f"WEBAPP: Status: {response.status_code}, Body: {response.text}")
                 result_message += f" (Status: {response.status_code})"


        if result_message:
            flash(result_message, message_category)

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)