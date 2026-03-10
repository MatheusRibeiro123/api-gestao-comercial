from flask import jsonify, request
from app.routes.bp_main import main

#lista temporaria para armezenar dados até a criação do BD
vendas = []

#============================ ROTAS DE VENDAS ============================

#criar venda
@main.route("/vendas", methods = ["POST"])
def criar_venda():
    venda = request.json
    vendas.append(venda)
    return jsonify(venda), 201

#listar vendas 
@main.route("/vendas", methods = ["GET"])
def listar_vendas():
    return jsonify(vendas)

#listar venda por id
@main.route("/vendas/<int:id>",methods = ["GET"])
def listar_venda(id):
    for venda in vendas:
        if venda["id"] == id:
            return jsonify(venda)
        
    return jsonify ({"erro":"Venda não encontrada"}) , 404

#atualizar venda
@main.route("/vendas/<int:id>", methods = ["PUT"])
def atualizar_venda(id):

    dados = request.json
    for venda in vendas:
        if venda["id"] == id:
            venda["id_cliente"] = dados.get("id_cliente", venda["id_cliente"])
            venda["id_produto"] = dados.get("id_produto", venda["id_produto"])
            venda["quantidade"] = dados.get("quantidade", venda["quantidade"])

            return jsonify(venda)
       
    return jsonify({"erro": "Venda não encontrada"}), 404

#deletar venda
@main.route("/vendas/<int:id>", methods = ["DELETE"])
def deletar_venda(id):
    for venda in vendas:
        if venda["id"] == id:
            vendas.remove(venda)
            return jsonify({"mensagem": "Venda deletada com sucesso"})

    return jsonify({"erro": "Venda não encontrada"}), 404   