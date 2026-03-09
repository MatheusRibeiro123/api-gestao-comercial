from flask import jsonify, request
from app.routes.bp_main import main

#lista temporaria para armezenar dados até a criação do BD
produtos = []


#============================ ROTAS DE PRODUTOS ============================

#criar produto
@main.route("/produtos", methods = ["POST"])
def criar_produto():
    produto = request.json
    produtos.append(produto)
    return jsonify(produto), 201

#listar produto
@main.route("/produtos", methods = ["GET"])
def listar_produtos():
    return jsonify(produtos)

#listar produto por id
@main.route("/produtos/<int:id>", methods = ["GET"])
def listar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)
    
    return jsonify [{"erro":"produto não encontrado"}]

#alterar produto
@main.route("/produtos/<int:id>", methods = ["PUT"])
def atualizar_produto(id):
    dados = request.json
    for produto in produtos:
        if produto["id"] ==id:
            produto["nome"] = dados.get("nome",produto["nome"])
            produto["preco"] = dados.get("preco",produto["preco"])

            return jsonify(produto)
        
    return jsonify({"erro": "Produto não encontrado"}), 404

#deletar produto
@main.route("/produtos/<int:id>", methods = ["DELETE"])
def deletar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            produtos.remove(produto)
            return jsonify({"mensagem": "Produto deletado com sucesso"})

    return jsonify({"erro": "Produto não encontrado"}), 404



