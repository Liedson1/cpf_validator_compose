# 🔐 Validador de CPF com Docker Compose

Uma solução simples, modular e containerizada para validar CPFs. Composta por três serviços — Server, WebApp e Cliente — este projeto demonstra uma arquitetura leve e prática baseada em Docker Compose.

## 📦 Componentes

### ⚙️ Servidor (API - `server`)
- Linguagem: Python
- Framework: Flask
- Função: expõe o endpoint `/validate` via POST
- Validação com: `validate-docbr`
- Resposta: `{"cpf": "...", "is_valid": true/false}`
- Porta: interna 5000 (uso apenas dentro da rede Docker)

### 🌐 Aplicação Web (`webapp`)
- Framework: Flask
- Interface amigável em HTML com CSS embutido
- Envia o CPF digitado ao servidor via `requests`
- Feedback visual com flash messages (válido, inválido, erro)
- Porta: `5001`, acessível via navegador

### 💻 Cliente Terminal (`client`)
- Script Python interativo
- Loop contínuo para digitar e validar CPFs via terminal
- Ideal para testes manuais e validações rápidas

## ⚙️ Pré-requisitos

- Docker instalado ([link](https://docs.docker.com/engine/install/))
- Docker Compose ([link](https://docs.docker.com/compose/install/))

## 🗂 Estrutura de Diretórios

```
📁 validador-cpf
├── client/
│   ├── client.py
│   ├── Dockerfile
│   └── requirements.txt
├── server/
│   ├── server.py
│   ├── Dockerfile
│   └── requirements.txt
├── web/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── docker-compose.yml
└── README.md
```

## 🚀 Executando a Aplicação (modo Web)

```bash
git clone https://github.com/seu-usuario/validador-cpf.git
cd validador-cpf
docker compose up --build
```

Acesse [http://localhost:5001](http://localhost:5001) no navegador e digite um CPF. O resultado será exibido na tela.

## 🧪 Usando o Cliente Terminal (modo CLI)

```bash
docker compose up server
# em outro terminal:
docker compose up client
```

Depois:
```
Digite o CPF para validação (ou 'sair' para terminar):
```

## 🛑 Parando os Containers

```bash
docker compose down
# ou pressione Ctrl + C
```


