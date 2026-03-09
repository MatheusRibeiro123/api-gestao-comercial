from flask import jsonify, request
from app.routes.bp_main import main

#lista temporaria para armezenar dados até a criação do BD
produtos = []