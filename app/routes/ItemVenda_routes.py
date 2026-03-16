from flask import request, jsonify
from app.routes.bp_main import main
from app.database import db
from app.models import ItemVenda

#--------------rotas da classe ItemVenda------------

#criar novo item venda
@main.route("/itens-venda", methods = ["POST"])
def criar_item_venda():
    dados = request.json

    item = ItemVenda(id_venda = dados["id_venda"],
                     id_produto = dados["id_produto"],
                     quantidade = dados["quantidade"],
                     preco_unitario = dados["preco_unitario"])
    
    db.session.add(item)
    db.session.commit()

#listar todos os itens venda
@main.route("/itens-venda", methods = ["GET"])
def listar_itens_venda():
    itens = ItemVenda.query.all()

    return jsonify([item.to_dict() for item in itens])

#buscar item-venda especifico
@main.route("/itens-venda/<int:id>", methods = ["GET"])
def listar_item_venda(id):
    item = ItemVenda.query.get_or_404(id)

    return jsonify(item.to_dict())

#deletar item-venda
@main.route("/itens-venda/<int:id>", methods = ["DELETE"])
def deletar_item_vendas(id):
    item = ItemVenda.query.get(id)

    if not item:
        return jsonify({"erro":"Item venda não existe!"}), 404
    
    db.session.delete(item)
    db.session.commit()

    return jsonify({"mensagem":"Item venda deletado com sucesso!"})

#atualizar item-venda
@main.route("/itens-venda/<int:id>", methods = ["PUT"])
def atualizar_itens_venda(id):

    item = ItemVenda.query.get_or_404(id)

    dados = request.json

    item.quantidade = dados.get("quantidade",item.quantidade)
    item.preco_unitario = dados.get("preco_unitario", item.preco_unitario)

    db.session.commit()

    return jsonify(item.to_dict())


