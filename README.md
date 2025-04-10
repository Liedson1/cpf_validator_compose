# Validador de CPF com Docker Compose (Servidor API + WebApp + Cliente Terminal)

Este projeto demonstra uma arquitetura simples cliente-servidor para validação de CPFs (Cadastro de Pessoas Físicas) brasileiros, totalmente orquestrada com Docker Compose. Ele inclui um servidor de API backend, uma interface web frontend e um cliente de terminal opcional.

## Componentes

1. **Servidor (Backend API - `server`)**
    - Tecnologia: Python com Flask
    - Endpoint: POST `/validate`
    - Validação com `validate-docbr`
    - Retorno JSON: `{"cpf": "...", "is_valid": true/false}`
    - Porta interna: 5000

2. **Aplicação Web (Frontend - `webapp`)**
    - Tecnologia: Python com Flask
    - Interface com formulário HTML (`templates/index.html`)
    - Comunicação com servidor via `requests`
    - Feedback visual usando Flash Messages
    - Porta exposta: 5001 → `localhost:5001`

3. **Cliente (Terminal - `client`)**
    - Script em Python
    - Loop interativo de validação
    - Comunicação via HTTP com o servidor
    - Uso opcional para testes e interação rápida

## Pré-requisitos

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estrutura do Projeto

```
├── client/
│   ├── client.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── server/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── server.py
├── web/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── README.md
```

## Como Rodar a Aplicação (Interface Web)

1. Clone ou baixe este repositório
2. No terminal, acesse a raiz do projeto
3. Execute o comando:

```bash
docker compose up --build
```

4. Acesse `http://localhost:5001` no navegador
5. Digite um CPF e clique em "Validar CPF" para verificar

## Como Parar a Aplicação

```bash
docker compose down
```

ou pressione `Ctrl + C`

## Como Usar o Cliente de Terminal (Opcional)

1. Inicie o servidor

```bash
docker compose up server
```

2. Em outro terminal, execute o cliente

```bash
docker compose up client
```

3. Digite um CPF quando solicitado

```
Digite o CPF para validação (ou 'sair' para terminar):
```

Digite quantos quiser, ou `sair` para encerrar

## Licença

MIT

