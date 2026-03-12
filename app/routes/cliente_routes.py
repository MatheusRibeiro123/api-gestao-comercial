from flask import jsonify, request
from app.routes.bp_main import main
from app.models.cliente import Cliente
from app.database import db


#============================ ROTAS DE CLIENTES ============================

#criar novo cliente
@main.route("/clientes",methods = ["POST"])
def criar_cliente():
   
   dados = request.json
   cliente = Cliente(
      nome = dados["nome"],
      telefone = dados["telefone"]
   )

   db.session.add(cliente)
   db.session.commit()

   return jsonify(cliente.to_dict()), 201

#listar clientes
@main.route("/clientes", methods = ["GET"])
def listar_clientes():
    
    clientes = Cliente.query.all()

    lista_clientes = [cliente.to_dict() for cliente in clientes]

    return jsonify(lista_clientes)


#listar apenas um cliente
@main.route("/clientes/<int:id>",methods = ["GET"])
def buscar_cliente(id):
    cliente = Cliente.query.get(id)

    if cliente:
        return jsonify(cliente.to_dict())
    
    return jsonify({"erro": "Cliente não encontrado"}), 404


#atualizar cliente
@main.route("/clientes/<int:id>",methods = ["PUT"])
def atualizar_cliente(id):
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify({"erro": "Cliente não encontrado"}), 404
    
    dados = request.json

    cliente.nome = dados["nome"]
    cliente.telefone = dados["telefone"]

    db.session.commit()    

    return jsonify(cliente.to_dict())

        
    #deletar cliente
@main.route("/clientes/<int:id>" ,methods = ["DELETE"])
def deletar_cliente(id):
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify ({"erro":"Cliente não encontrado"}), 404
    
    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"mensagem": "Cliente removido"})