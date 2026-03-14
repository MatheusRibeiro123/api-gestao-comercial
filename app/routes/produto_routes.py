from flask import jsonify, request
from app.routes.bp_main import main
from app.database import db
from app.models.produto import Produto
#============================ ROTAS DE PRODUTOS ============================

#criar produto
@main.route("/produtos", methods = ["POST"])
def criar_produto():
    
    dados = request.json
    
    produto = Produto(
        nome = dados["nome"],
        preco = dados["preco"],
        estoque = dados["estoque"]
    )

    db.session.add(produto)
    db.session.commit()

    return jsonify (produto.to_dict()), 201


#listar produtos
@main.route("/produtos", methods = ["GET"])
def listar_produtos():
    produtos = Produto.query.all()

    return jsonify([produto.to_dict() for produto in produtos])

    
#listar produto por id
@main.route("/produtos/<int:id>", methods = ["GET"])
def listar_produto(id):
    produto = Produto.query.get(id)

    if produto:
        return jsonify(produto.to_dict())
    
    return jsonify({"erro":"Produto não encontrado"}),404

#alterar produto
@main.route("/produtos/<int:id>", methods = ["PUT"])
def atualizar_produto(id):
   produto = Produto.query.get(id)

   if not produto:
       return jsonify({"erro": "Produto não encontrado"}), 404
   
   dados= request.json

   produto.nome = dados.get("nome", produto.nome)
   produto.preco = dados.get("preco", produto.preco)
   produto.estoque = dados.get("estoque", produto.estoque)

   db.session.commit()

   return jsonify(produto.to_dict())

#deletar produto
@main.route("/produtos/<int:id>", methods = ["DELETE"])
def deletar_produto(id):
    produto = Produto.query.get(id)

    if not produto:
        return jsonify ({"erro":"Produto não encontrado"}), 404
    
    db.session.delete(produto)
    db.session.commit()

    return jsonify({"mensagem":"Produto deletado com sucesso"})



