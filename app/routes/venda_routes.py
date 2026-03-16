from flask import jsonify, request
from app.routes.bp_main import main
from app.database import db
from app.models.venda import Venda
#============================ ROTAS DE VENDAS ============================

#criar venda
@main.route("/vendas", methods = ["POST"])
def criar_venda():
    
    dados = request.json

    venda = Venda(
        id_cliente=dados["id_cliente"],
         )

    db.session.add(venda)
    db.session.commit()

    return jsonify(venda.to_dict()), 201

#listar vendas 
@main.route("/vendas", methods = ["GET"])
def listar_vendas():
    
    vendas = Venda.query.all()

    return jsonify([venda.to_dict() for venda in vendas])

#listar venda por id
@main.route("/vendas/<int:id>",methods = ["GET"])
def listar_venda(id):
    venda = Venda.query.get(id)

    if not venda:
        return jsonify({"erro":"Venda não encontrada"}),404
        
    return jsonify(venda.to_dict())

#atualizar venda
@main.route("/vendas/<int:id>", methods = ["PUT"])
def atualizar_venda(id):

    venda = Venda.query.get(id)

    if not venda:
        return jsonify({"erro":"Venda não encontrada"}),404
    
    dados = request.json

    venda.id_cliente = dados.get("id_cliente",venda.id_cliente)
 
    db.session.commit()

    return jsonify({"mensagem": "Venda atualizada com sucesso"})
    

#deletar venda
@main.route("/vendas/<int:id>", methods = ["DELETE"])
def deletar_venda(id):
    venda = Venda.query.get(id)

    if not venda:
        return jsonify({"erro":"Venda não encontrada"}),404
    
    db.session.delete(venda)
    db.session.commit()

    return jsonify({"mensagem": "Venda deletada com sucesso"})