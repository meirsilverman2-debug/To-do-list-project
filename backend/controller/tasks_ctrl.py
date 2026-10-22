from typing import Literal

from backend.dal.tasks_dal import tasks_dal
from pydantic import BaseModel, ValidationError
from werkzeug.exceptions import InternalServerError, BadRequest, NotFound


class TaskCreateSchema(BaseModel):
    title: str
    description: str
    day: Literal["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"]
    personal_number: str
    status: Literal["PENDING", "IN_PROGRESS", "COMPLETED"]


class TaskUpdateSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    day: Literal["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"] | None = None
    personal_number: str | None = None
    status: Literal["PENDING", "IN_PROGRESS", "COMPLETED"] | None = None


def get_tasks(day=None, personal_number=None, status=None):
    return {
        "success": "true",
        "data": tasks_dal.get_rows(
            day=day, personal_number=personal_number, status=status
        ),
    }


def create_task(data):

    validated = TaskCreateSchema(**data)

    checked_data = validated.model_dump()
    if not checked_data:
        raise BadRequest("No fields to create")

    new_task = tasks_dal.create(checked_data)
    if not new_task:
        raise InternalServerError("Cannot create task")
    return {"success": "true", "data": new_task}


def update_task(task_id, data):
    validated = TaskUpdateSchema(**data)

    checked_data = validated.model_dump(exclude_unset=True)

    if not checked_data:
        raise BadRequest("Nothing to update")

    updated_task = tasks_dal.update(task_id, checked_data)
    if not updated_task:
        raise NotFound("Task not found")
    return {"success": "true", "data": updated_task}


def delete_task(task_id):
    deleted = tasks_dal.delete(task_id)
    if not deleted:
        raise NotFound("Task not found")
    return {"success": "true", "data": "deleted successfully"}
