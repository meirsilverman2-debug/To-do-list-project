from typing import Literal

from backend.dal.tasks_dal import tasks_dal
from pydantic import BaseModel, ValidationError
from werkzeug.exceptions import BadRequest, NotFound


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
    return tasks_dal.get_rows(day=day, personal_number=personal_number, status=status)


def create_task(data: TaskCreateSchema):
    try:
        validated = TaskCreateSchema(**data)
    except ValidationError as err:
        raise BadRequest(err.json())
    
    checked_data = validated.model_dump()
    
    new_task = tasks_dal.create(checked_data)
    if not new_task:
        raise BadRequest("Bad request")
    return new_task


def update_task(task_id, data: TaskUpdateSchema):
    try:
        validated = TaskUpdateSchema(**data)
    except ValidationError as err:
        raise BadRequest(err.json())
    
    checked_data = validated.model_dump(exclude_unset=True)

    if not checked_data:
        raise BadRequest("Bad request")

    updated_task = tasks_dal.update(task_id, checked_data)
    if not updated_task:
        raise NotFound("Task not found")
    return updated_task


def delete_task(task_id):
    deleted = tasks_dal.delete(task_id)
    if not deleted:
        raise NotFound("Task not found")
    return {"message": "deleted successfully"}
