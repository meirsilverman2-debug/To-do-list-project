from backend.controller.tasks_ctrl import (
    create_task,
    delete_task,
    get_tasks,
    update_task,
)
from flask import Blueprint, jsonify, request

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.get("")
def get_tasks_route():
    day = request.args.get("day")
    personal_number = request.args.get("personal_number")
    status = request.args.get("status")

    result = get_tasks(day, personal_number, status)
    return jsonify(result), 200

@tasks_bp.post("")
def create_task_route():
    body = request.get_json() or {}
    result = create_task(body)
    return jsonify(result), 201

@tasks_bp.patch("/<str:id>")
def update_task_route(id):
    body = request.get_json()
    result = update_task(id, body)
    return jsonify(result), 200

@tasks_bp.delete("/<str:id>")
def delete_task_route(id):
    result = delete_task(id)
    return jsonify(result), 200