from flask import Flask
from app.routes.bp_main import main
from app.database import db

def create_app():

    app=Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
   
    from app.routes import cliente_routes
    from app.routes import produto_routes
    from app.routes import venda_routes
    from app.routes import ItemVenda_routes
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()                       
    
    return app