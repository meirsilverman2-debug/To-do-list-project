from flask import Blueprint, request, jsonify
from backend.dal.users_dal import soldiers_repo

soldiers_bp = Blueprint("soldiers", __name__)

@soldiers_bp.post("")
def add_new_soldier():
    return "not implemented"

@soldiers_bp.put("/<int:personal_number>")
def update_soldier_data(personal_number):
    return "not implemented"

@soldiers_bp.delete("/<int:personal_number>")
def remove_soldier(personal_number):
    return "not implemented"

@soldiers_bp.get("")
def get_all_soldiers():
    return "not implemented 10"

@soldiers_bp.get("/<int:personal_number>")
def get_soldier_by_personal_number(personal_number):
    return "not implemented 1"