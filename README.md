# API de Gestão Comercial

## 📌 Sobre o projeto

Esta é uma **API REST de gestão comercial**, desenvolvida com o objetivo de simular um sistema real de controle de vendas.

A aplicação permite o gerenciamento de:

* Clientes
* Produtos
* Vendas
* Itens de venda

Durante o desenvolvimento, foram aplicados conceitos fundamentais de backend, como **relacionamento entre entidades**, **estruturação de API REST** e **lógica de negócio**, incluindo o cálculo automático do valor total das vendas.

---

## 🚀 Tecnologias utilizadas

* Python
* Flask
* SQLAlchemy
* SQLite
* JSON

---

## ⚙️ Funcionalidades

* CRUD completo de clientes
* CRUD completo de produtos
* Registro de vendas com múltiplos itens
* Relacionamento entre vendas e produtos
* Cálculo automático do valor total da venda
* Retorno estruturado em JSON

---

## 🧠 Regras de negócio implementadas

* Uma venda pode conter vários itens
* Um produto pode estar presente em várias vendas
* O valor total da venda é calculado dinamicamente com base nos itens
* Cada item de venda armazena o preço unitário no momento da venda

---

## 📡 Exemplo de resposta da API

```json
{
  "cliente": "João Silva",
  "id": 1,
  "id_cliente": 1,
  "itens": [
    {
      "id": 1,
      "id_produto": 1,
      "produto": "Mouse Gamer",
      "quantidade": 2,
      "preco_unitario": 35.0
    },
    {
      "id": 2,
      "id_produto": 2,
      "produto": "Teclado Mecânico",
      "quantidade": 1,
      "preco_unitario": 30.0
    }
  ],
  "total": 100.0
}
```

---

## 🛠 Estrutura do projeto

```
api-gestao-comercial
│
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── routes
│   │   └── bp_main.py
│
├── run.py
└── README.md
```

---

## ▶️ Como executar o projeto

1. Clone o repositório:

```
git clone https://github.com/MatheusRibeiro123/api-gestao-comercial.git
```

2. Acesse a pasta:

```
cd api-gestao-comercial
```

3. Crie e ative um ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

4. Instale as dependências:

```
pip install -r requirements.txt
```

5. Execute a aplicação:

```
python run.py
```

---

## 📚 Objetivo

Este projeto foi desenvolvido com foco em **aprendizado prático de desenvolvimento backend**, simulando um cenário próximo ao de sistemas comerciais reais.

---

## 👨‍💻 Autor

Desenvolvido por **Matheus Ribeiro**, estudante de Tecnologia da Informação.
