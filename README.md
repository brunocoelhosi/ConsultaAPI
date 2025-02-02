## PROJETO: CONSULTA DE DADOS DE UMA API PÚBLICA

## Descrição

O objetivo do projeto é criar um script que consuma dados de uma API pública, manipule as informações recebidas e exiba os resultados de forma organizada. O script utiliza Python e a biblioteca `requests` para fazer requisições HTTP e trabalhar com os dados retornados no formato JSON.

A API utilizada é a [JSONPlaceholder](https://jsonplaceholder.typicode.com/), que fornece dados fictícios de usuários e posts.

## Funcionalidades

- Listar todos os usuários com seus respectivos IDs e nomes.
- Permitir que o usuário insira um ID para:
  - Exibir o nome e o email do usuário selecionado.
  - Listar os títulos dos posts criados por esse usuário.
- Tratamento de erros, como:
  - ID de usuário inválido.
  - Problemas de conexão com a API.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Bibliotecas Python (listadas no `requirements.txt`)

## Como Usar

Siga os passos abaixo para configurar e executar o projeto:

1. Clone este repositório:
   ```bash
   git clone https://github.com/brunocoelhosi/ConsultaAPI.git
2. Crie um ambiente virtual no repositório (opcional)
3. Instale as dependências
   ```bash
   pip install -r requirements.txt
   
4. Execute o script
   ```bash
   python main.py
