from flask import jsonify, request
from app.routes.bp_main import main


#lista temporaria para armezenar dados até a criação do BD
clientes = []


#============================ ROTAS DE CLIENTES ============================

#criar novo cliente
@main.route("/clientes",methods = ["POST"])
def criar_cliente():
    cliente = request.json
    clientes.append(cliente)
    return jsonify(cliente)


#listar clientes
@main.route("/clientes", methods = ["GET"])
def listar_clientes():
    return jsonify(clientes)


#listar apenas um cliente
@main.route("/clientes/<int:id>",methods = ["GET"])
def buscar_cliente(id):
    for cliente in clientes:
        if cliente["id"] == id:
            return jsonify(cliente)
        
    return jsonify({"erro": "Cliente não encontrado"})


#atualizar cliente
@main.route("/clientes/<int:id>",methods = ["PUT"])
def atualizar_cliente(id):
    dados = request.json

    for cliente in clientes:
        if cliente["id"] == id:
            cliente.update(dados)
            return jsonify(cliente)
        
    return jsonify({"erro": "Cliente não encontrado"})

    
#deletar cliente
@main.route("/clientes/<int:id>" ,methods = ["DELETE"])
def deletar_cliente(id):
    for cliente in clientes:
        if cliente["id"] == id:
            clientes.remove(cliente)
            return jsonify({"mensagem":"Cliente removido"})
    return jsonify({"erro":"Cliente não encontrado"})
