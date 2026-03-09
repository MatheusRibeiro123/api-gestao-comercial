from flask import Flask
from app.routes.bp_main import main

def create_app():

    app=Flask(__name__)

    from app.routes import cliente_routes
    
    app.register_blueprint(main)
                           
    return app