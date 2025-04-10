# client/client.py
import requests
import sys
import time
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - CLIENT - %(levelname)s - %(message)s')


SERVER_HOST = os.environ.get('SERVER_HOST', 'server')
SERVER_URL = f"http://{SERVER_HOST}:5000/validate"

def send_cpf_for_validation(cpf):
    """Envia um CPF para validação no servidor e imprime o resultado."""
    payload = {"cpf": cpf}
    retries = 3 
    wait_time = 2

    for i in range(retries):
        try:
            logging.info(f"Tentando conectar ao servidor: {SERVER_URL} com CPF: {cpf}")
            response = requests.post(SERVER_URL, json=payload, timeout=10)
            response.raise_for_status() 

            result = response.json()
            logging.info(f"Resposta recebida do servidor: {result}")
            print(f"\n--- Resultado da Validação para {cpf} ---")
            print(f"É válido? {'Sim' if result.get('is_valid') else 'Não'}")
            print("-----------------------------------------\n")
            return True 

        except requests.exceptions.ConnectionError as e:
            logging.warning(f"Não foi possível conectar ao servidor (tentativa {i+1}/{retries}): {e}. Tentando novamente em {wait_time}s...")
            time.sleep(wait_time)
        except requests.exceptions.Timeout:
            logging.warning(f"Timeout ao conectar ao servidor (tentativa {i+1}/{retries}). Tentando novamente em {wait_time}s...")
            time.sleep(wait_time)
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro na requisição para o servidor (tentativa {i+1}/{retries}): {e}")
            if response is not None:
                logging.error(f"Status Code: {response.status_code}, Response: {response.text}")
                print(f"\nERRO: O servidor retornou um erro ({response.status_code}). Detalhes: {response.text}\n")
            else:
                 print(f"\nERRO: Falha na comunicação com o servidor. Verifique se ele está rodando.\n")
            time.sleep(wait_time)

    logging.error(f"Falha ao comunicar com o servidor para o CPF {cpf} após múltiplas tentativas.")
    print(f"\nERRO CRÍTICO: Não foi possível obter resposta do servidor para o CPF {cpf}.\n")
    return False 

if __name__ == "__main__":
    logging.info("Cliente iniciado. Aguardando 5 segundos para garantir que o servidor esteja pronto...")
    time.sleep(5)
    logging.info("Pronto para receber CPFs.")

    while True:
        try:
            cpf_to_test = input("Digite o CPF para validação (ou 'sair' para terminar): ").strip()

            if cpf_to_test.lower() == 'sair':
                logging.info("Comando 'sair' recebido. Encerrando o cliente.")
                break

            if not cpf_to_test:
                continue

            
            send_cpf_for_validation(cpf_to_test)

        except EOFError:
            logging.warning("Entrada fechada (EOF). Encerrando o cliente.")
            break
        except KeyboardInterrupt:
            logging.info("Interrupção de teclado recebida. Encerrando o cliente.")
            break

    print("\nCliente encerrado.")