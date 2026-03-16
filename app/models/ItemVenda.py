from app.database import db

class ItemVenda(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_venda = db.Column(db.Integer, db.ForeignKey("venda.id"), nullable = False)
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"), nullable = False)
    quantidade = db.Column(db.Integer, nullable = False)
    preco_unitario = db.Column(db.Float, nullable = False)

    venda = db.relationship("Venda")
    produto = db.relationship("Produto")

    def to_dict(self):
        return {
            "id": self.id,
            "id_produto": self.id_produto,
            "produto": self.produto.nome if self.produto else None,
            "quantidade":self.quantidade,
            "preco_unitario": self.preco_unitario

}