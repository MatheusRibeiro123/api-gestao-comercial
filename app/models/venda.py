from app.database import db

class Venda(db.Model):

    id = db.Column(db.Integer, primary_key= True)
    id_cliente = db.Column(db.Integer , db.ForeignKey("cliente.id"), nullable = False)
    id_produto = db.Column(db.Integer , db.ForeignKey("produto.id"), nullable = False)
    quantidade = db.Column(db.Integer , nullable = False)    

    cliente = db.relationship("Cliente")
    produto = db.relationship("Produto")
    
    def to_dict(self):
            return{
                "id":self.id ,
                   "id_cliente":self.id_cliente,
                   "id_produto":self.id_produto,
                   "quantidade":self.quantidade,
                   "cliente":self.cliente.nome if self.cliente else None,
                   "produto":self.produto.nome if self.produto else None
                   }
        
        

            
    
