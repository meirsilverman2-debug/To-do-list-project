from typing import Literal

from backend.dal.tasks_dal import tasks_dal
from fastapi import HTTPException
from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    title: str
    description: str
    day: Literal["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"]
    personal_number: str
    status: Literal["PENDING", "IN_PROGRESS", "COMPLETED"]


class TaskUpdateSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    day: Literal["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"] | None = (
        None
    )
    personal_number: str | None = None
    status: Literal["PENDING", "IN_PROGRESS", "COMPLETED"] | None = None


def get_tasks(day=None, personal_number=None, status=None):
    return tasks_dal.get_rows(day=day, personal_number=personal_number, status=status)


def create_task(data: TaskCreateSchema):
    checked_data = data.model_dump()
    new_task = tasks_dal.create(checked_data)
    if not new_task:
        raise HTTPException(status_code=400, detail="Bad request")
    return new_task


def update_task(task_id, data: TaskUpdateSchema):
    checked_data = data.model_dump(exclude_unset=True)
    if not checked_data:
        raise HTTPException(status_code=400, detail="Bad request")

    updated_task = tasks_dal.update(task_id, checked_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

def delete_task(task_id):
    deleted = tasks_dal.delete(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "deleted successfully"}
