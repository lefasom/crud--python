from flask import Blueprint

from service.controller import create_lista_service, get_listas_service, get_lista_service, update_lista_service, delete_lista_service

rutas = Blueprint('rutas', __name__)

# @rutas.route('/', methods=['GET'])
# def get_listas():
#     return get_listas_service()

# @rutas.route('/<id>',methods=['GET'])
# def get_lista(id):
#     return get_lista_service(id)

@rutas.route('/', methods=['POST'])
def create_lista():
    return create_lista_service()

# @rutas.route('/<id>',methods=['PUT'])
# def update_lista(id):
#     return update_lista_service(id)

@rutas.route('/<id>',methods=['POST', 'DELETE'])
def delete_lista(id):
    return delete_lista_service(id)