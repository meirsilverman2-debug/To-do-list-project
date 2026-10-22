from flask import Blueprint, request, jsonify
from backend.dal.users_dal import soldiers_repo
from werkzeug.exceptions import abort
from backend.controller.users_ctrl import validate_new_user, validate_update_user

soldiers_bp = Blueprint("soldiers", __name__)


@soldiers_bp.post("")
def add_new_soldier():
    body = request.get_json(silent=True)
    if not body:
        abort(400, "body is required")

    data = validate_new_user(body)
    new_user = soldiers_repo.create_row(data)
    return jsonify({"success": True, "data": new_user})



@soldiers_bp.patch("/<string:personal_number>")
def update_soldier_data(personal_number):
    body = request.get_json(silent=True)
    if not body:
        abort(400, "body is required")

    data = validate_update_user(body)
    updated_user = soldiers_repo.update_row(data, personal_number=personal_number)
    if not updated_user:
        abort(404, f"soldier {personal_number} not found")

    return jsonify({
        "success": True,
        "data": updated_user
    })


@soldiers_bp.delete("/<string:personal_number>")
def remove_soldier(personal_number):
    deleted_user = soldiers_repo.delete_row(personal_number=personal_number)
    if not deleted_user:
        abort(404, f"soldier {personal_number} not found")

    return jsonify({
        "success": True,
        "data": deleted_user
    })


@soldiers_bp.get("")
def get_all_soldiers():
    role = request.args.get("role")
    commander_id = request.args.get("commander_id")

    filters = {}
    if role: filters["role"] = role
    if commander_id: filters["commander_id"] = commander_id

    users = soldiers_repo.get_rows(**filters)
    return jsonify({
        "success": True,
        "data": users 
    })


@soldiers_bp.get("/<string:personal_number>")
def get_soldier_by_personal_number(personal_number):
    user = soldiers_repo.get_one_row(personal_number=personal_number)
    if not user:
        abort(404, f"soldier {personal_number} not found")
    return jsonify({
        "success": True,
        "data": user
    })
