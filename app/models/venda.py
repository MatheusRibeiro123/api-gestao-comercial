from app.database import db
from app.models import ItemVenda
class Venda(db.Model):

    id = db.Column(db.Integer, primary_key= True)
    id_cliente = db.Column(db.Integer , db.ForeignKey("cliente.id"), nullable = False)
    itens = db.relationship("ItemVenda")
    cliente = db.relationship("Cliente")
    
    
    def to_dict(self):
            return{
                "id":self.id ,
                   "id_cliente":self.id_cliente,
                   "cliente":self.cliente.nome if self.cliente else None,
                   "itens":[item.to_dict() for item in self.itens],
                   "total":self.calcular_total()
                   }
        
    def calcular_total(self):
          return sum(item.quantidade * item.preco_unitario for item in self.itens)

            
    
