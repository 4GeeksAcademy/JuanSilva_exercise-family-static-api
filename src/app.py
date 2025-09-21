""" This module takes care of starting the API Server, Loading the DB and Adding the endpoints """
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Endpoint 1: Obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Endpoint 2: Obtener un miembro específico por ID
@app.route('/members/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    # Buscamos por  ID
    member = jackson_family.get_member(member_id)
    
    # Si no existe, devolver error 404
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    
    # Si existe, devolver el miembro
    return jsonify(member), 200

# Endpoint 3: Agregar nuevo miembro
@app.route('/members', methods=['POST'])
def add_member():
    
    body = request.get_json()
    
    if not body:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    if "first_name" not in body:
        return jsonify({"error": "first_name is required"}), 400
    
    if "age" not in body:
        return jsonify({"error": "age is required"}), 400
    
    if "lucky_numbers" not in body:
        return jsonify({"error": "lucky_numbers is required"}), 400
    
    # Agregamos el miembro a la familia
    jackson_family.add_member(body)
    
    # Devolvemos "successfully"
    return jsonify({"message": "Member added successfully"}), 200

# Endpoint 4: Eliminar un miembro por id
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # Intentamos eliminar el miembro
    deleted = jackson_family.delete_member(member_id)
    
    # Si no existe, devolver error
    if not deleted:
        return jsonify({"error": "Member not found"}), 404
    
    # Si se eliminó correctamente
    return jsonify({"done": True}), 200

# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)