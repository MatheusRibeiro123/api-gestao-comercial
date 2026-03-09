from flask import jsonify, request
from app.routes.bp_main import main

#lista temporaria para armezenar dados até a criação do BD
vendas = []

#============================ ROTAS DE VENDAS ============================

#criar venda
@main.routes("/vendas", methods = ["POST"])
def criar_venda():
    venda = request.json
    vendas.append(venda)
    return jsonify(venda), 201

#listar vendas 
@main.routes("/vendas", methods = ["GET"])
def listar_vendas():
    return jsonify(vendas)

#listar venda por id
@main.routes("/vendas/<int:id>",methods = ["GET"])
def listar_venda(id):
    for venda in vendas:
        if venda["id"] == id:
            return jsonify(venda)
        
    return jsonify [{"erro":"Venda não encontrada"}]

#atualizar venda
@main.routes("/vendas/<int:id>", methods = ["PUT"])
def atualizar_venda(id):
