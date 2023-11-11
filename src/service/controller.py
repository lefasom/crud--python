from flask import request, Response, redirect, url_for
from bson import json_util, ObjectId

from config.mongodb import mongo


def create_lista_service():
    title = request.form.get("titulo")
    description = request.form.get("descripcion")
    print(description,title)
    if title:
        response = mongo.db.lista.insert_one(
            {"title": title, "description": description, "done": False}
        )
        result = {
            "id": str(response.inserted_id),
            "title": title,
            "description": description,
            "done": False,
        }
        # return result
        return redirect(url_for('Home'))
    else:
        return "Invalid payload", 400


def get_listas_service():
    data = mongo.db.lista.find()
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")


def get_lista_service(id):
    data = mongo.db.lista.find_one({"_id": ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype="application/json")


def update_lista_service(id):
    data = request.get_json()
    if len(data) == 0:
        return "Invalid payload", 400
    response = mongo.db.lista.update_one({"_id": ObjectId(id)}, {"$set": data})
    if response.modified_count >= 1:
        return 'Lista update successfully',200
    else:
        return 'Lista not found', 404
def delete_lista_service(id):
    if request.method == 'DELETE' or (request.method == 'POST' and request.form.get('_method') == 'DELETE'):
        response = mongo.db.lista.delete_one({'_id': ObjectId(id)})
        if response.deleted_count >= 1:
            return redirect(url_for('Home'))
    return "Lista not found", 404