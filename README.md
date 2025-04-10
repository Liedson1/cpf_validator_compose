# Validador de CPF com Docker Compose (Servidor API + WebApp + Cliente Terminal)

Este projeto demonstra uma arquitetura simples cliente-servidor para validação de CPFs (Cadastro de Pessoas Físicas) brasileiros, totalmente orquestrada com Docker Compose. Ele inclui um servidor de API backend, uma interface web frontend e um cliente de terminal opcional.

## Componentes

1.  **Servidor (Backend API - `server`)**
    *   Tecnologia: Python com Flask.
    *   Responsabilidade: Expõe um endpoint REST (`/validate` via método POST) que recebe um CPF em formato JSON.
    *   Validação: Utiliza a biblioteca `validate-docbr` para verificar a validade matemática do CPF.
    *   Comunicação: Responde com um JSON indicando se o CPF é válido ou não (`{"cpf": "...", "is_valid": true/false}`).
    *   Acessibilidade: Ouve na porta 5000 *dentro* da rede Docker, não exposta diretamente ao host.

2.  **Aplicação Web (Frontend - `webapp`)**
    *   Tecnologia: Python com Flask.
    *   Responsabilidade: Fornece uma interface web amigável para o usuário.
    *   Interface: Apresenta um formulário HTML (`templates/index.html`) onde o usuário pode digitar um CPF. O CSS está embutido no HTML para simplicidade.
    *   Comunicação: Ao submeter o formulário, a webapp envia o CPF para o endpoint `/validate` do serviço `server` usando a biblioteca `requests`.
    *   Feedback: Exibe o resultado da validação (Válido/Inválido) ou mensagens de erro diretamente na página usando o sistema de *flash messages* do Flask.
    *   Acessibilidade: Ouve na porta 5001 *dentro* do container, que é mapeada para a porta 5001 do seu computador host (`localhost:5001`).

3.  **Cliente (Terminal - `client`)** (Opcional)
    *   Tecnologia: Script Python simples.
    *   Responsabilidade: Oferece uma interface de linha de comando para interagir com o servidor API.
    *   Interação: Roda em um loop, pede ao usuário para digitar um CPF, envia para o endpoint `/validate` do serviço `server` e imprime a resposta no terminal.
    *   Uso: Principalmente para testes ou cenários onde uma interface web não é necessária.

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:

*   [Docker Engine](https://docs.docker.com/engine/install/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (Geralmente já vem incluído no Docker Desktop)

## Estrutura do Projeto
├── client/
│ ├── client.py
│ ├── Dockerfile
│ └── requirements.txt
├── docker-compose.yml
├── server/
│ ├── Dockerfile
│ ├── requirements.txt
│ └── server.py
├── web/
│ ├── app.py
│ ├── Dockerfile
│ ├── requirements.txt
│ └── templates/
│ └── index.html
└── README.md

## Como Rodar a Aplicação (Interface Web)

Esta é a forma principal e recomendada de usar o projeto.

1.  **Clone ou Baixe o Projeto:** Certifique-se de ter todos os arquivos e pastas listados acima no seu computador.

2.  **Navegue até o Diretório Raiz:**
    Abra seu terminal ou prompt de comando e use o comando `cd` para entrar na pasta principal do projeto (a que contém o `docker-compose.yml`).

3.  **Construa as Imagens e Inicie os Containers:**
    Execute o seguinte comando. Ele irá:
    *   Construir as imagens Docker para `server`, `webapp` e `client` (usando a flag `--build` para garantir que usem o código mais recente).

    ```bash
    docker compose up --build 
    ```
    
    Aguarde alguns segundos para que os containers iniciem e o servidor esteja pronto.

4.  **Acesse a Aplicação Web:**
    Abra seu navegador de internet e navegue para o seguinte endereço:
    [http://localhost:5001](http://localhost:5001)

5.  **Interaja:**
    *   Você verá a página "Validador de CPF".
    *   Digite um número de CPF (com ou sem pontuação) no campo de texto.
    *   Clique no botão "Validar CPF".
    *   A página será recarregada e uma mensagem aparecerá acima do formulário indicando se o CPF é "VÁLIDO" (em verde) ou "INVÁLIDO" (em azul/info), ou exibirá uma mensagem de erro (em vermelho) se algo der errado na comunicação com o servidor.

## Como Parar a Aplicação

Para parar e remover os containers, redes e volumes (se houver) criados pelo Docker Compose, execute o seguinte comando no terminal, dentro da pasta do projeto:

```bash
docker compose down
```
## Como Usar o Cliente de Terminal (Opcional)
Se preferir usar a interface de linha de comando em vez da web:
Garanta que o Servidor Esteja Rodando: O serviço server precisa estar em execução. Você pode iniciá-lo separadamente:
```bash
docker compose up server
```
Execute o Cliente: Use o comando docker compose up client

**Interaja no Terminal:**
O cliente aguardará 5 segundos.
Você verá o prompt: Digite o CPF para validação (ou 'sair' para terminar):
Digite um CPF e pressione Enter. O resultado será impresso.
Continue digitando CPFs ou digite sair para encerrar o script e remover o container (devido ao --rm).
