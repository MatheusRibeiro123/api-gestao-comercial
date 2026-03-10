class Venda:
    def __init__(self, id, id_cliente, id_produto, quantidade):
        self.id=id
        self.id_cliente=id_cliente
        self.id_produto=id_produto
        self.quantidade=quantidade

    def to_dict(self):
            return{
                "id":self.id ,
                   "id_cliente":self.id_cliente,
                   "id_produto":self.id_produto,
                   "quantidade":self.quantidade}
        
        

            
    
