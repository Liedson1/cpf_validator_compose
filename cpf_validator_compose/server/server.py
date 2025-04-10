from flask import Flask, request, jsonify
from validate_docbr import CPF
import logging

app = Flask(__name__)
cpf_validator = CPF()

logging.basicConfig(level=logging.INFO)

@app.route('/validate', methods=['POST'])
def validate_cpf_endpoint():
    try:
        data = request.get_json()
        if not data or 'cpf' not in data:
            logging.error("Requisição inválida: JSON faltando ou sem a chave 'cpf'.")
            return jsonify({"error": "JSON inválido ou chave 'cpf' ausente"}), 400

        cpf_to_validate = data['cpf']
        logging.info(f"Recebido CPF para validação: {cpf_to_validate}")

        is_valid = cpf_validator.validate(cpf_to_validate)

        response = {
            "cpf": cpf_to_validate,
            "is_valid": is_valid
        }
        logging.info(f"Resultado da validação: {response}")
        return jsonify(response), 200

    except Exception as e:
        logging.error(f"Erro inesperado no servidor: {e}", exc_info=True)
        return jsonify({"error": "Erro interno no servidor"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 