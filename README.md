# 👕 Clothing Store API (My First FastAPI Project)

Este repositório contém o meu primeiro projeto prático estudando **FastAPI** e o desenvolvimento de APIs modernas com Python. 

O projeto simula o backend de um sistema de controle de estoque para uma loja de roupas (camisetas, calças e jaquetas), integrado a uma interface visual web dinâmica.

## 🎓 Créditos e Aprendizado
Este projeto foi construído acompanhando a excelente didática do tutorial "Build a Simple API from Scratch" da **Mariya Sha** ([GitHub Original](https://github.com/MariyaSha/Simple_API_Example)). 

A estrutura base do código (incluindo o cliente visual em Jinja2) foi criada por ela. Para consolidar meus estudos, eu **adaptei e expandi** o projeto original das seguintes formas:
* Reestruturei as pastas do projeto para facilitar a execução local.
* Modifiquei o tema de "entregas em Nova Jersey" para um "Estoque de Loja de Roupas".
* Padronizei o código fonte do backend para o inglês.
* Adicionei novas regras de negócio e validações de erro personalizadas.

## 🚀 O que eu aprendi e apliquei neste projeto:
Durante o desenvolvimento, pude colocar em prática conceitos fundamentais de desenvolvimento web e infraestrutura:

* **Ambientes Virtuais:** Configuração e uso de ambientes isolados rodando no Linux via **WSL**.
* **Rotas Dinâmicas (Path Parameters):** Criação de URLs que aceitam variáveis (ex: `/warehouse/{product}`).
* **Query Parameters & Type Casting:** Recebimento de dados via URL e conversão segura de strings para inteiros.
* **Regras de Negócio e Tratamento de Erros:** Uso do `HTTPException` para proteger a API:
  * Retorna erro **400 (Bad Request)** se o cliente tentar pedir uma quantidade maior do que o estoque disponível.
  * *(Adição Própria)* Retorna erro **404 (Not Found)** se o cliente buscar um produto que não existe no dicionário da loja.
* **Integração Full-Stack Básica:** Entendimento de como um cliente HTML/Jinja2 consome uma API RESTful de forma dinâmica.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12**
* **FastAPI** (Framework Web)
* **Uvicorn** (Servidor ASGI)
* **Jinja2** (Renderização de templates HTML)
* **Requests** (Para comunicação entre o cliente visual e o servidor)

## 💻 Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone [https://github.com/SEU-USUARIO/seu-repositorio.git](https://github.com/SEU-USUARIO/seu-repositorio.git)
cd seu-repositorio
```

2. Crie e ative um ambiente virtual:
```bash
conda create -n api_env python=3.12
conda activate api_env
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Em um terminal, inicie o Servidor (Backend) na porta 8000:
```bash
uvicorn nj_server:app --reload
```

5. Em um segundo terminal (com o ambiente virtual ativado), inicie o Cliente (Frontend) na porta 8001:
```bash
uvicorn ny_client:app --reload --port 8001
```

6. Acesse a interface visual no seu navegador através de: http://localhost:8001






