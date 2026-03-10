class Cliente:
    def __init__(self, id, nome, telefone):
        self.id= id
        self.nome = nome
        self.telefone = telefone
    
    def to_dict(self):
        return {
            "id" : self.id ,
                "nome" : self.nome,
                "telefone":self.telefone} 
    

        
        

            
    
