from app.database import db

class Cliente(db.Model):
    
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    
    def to_dict(self):
        return {
            "id" : self.id ,
                "nome" : self.nome,
                "telefone":self.telefone} 
    

        
        

            
    
