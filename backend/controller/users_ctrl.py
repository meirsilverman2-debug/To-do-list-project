from pydantic import BaseModel, ValidationError
from typing import Literal
from werkzeug.exceptions import abort

class NewUserSchema(BaseModel):
    personal_number: str
    name: str
    phone_number: str
    role: Literal["SOLDIER", "COMMANDER"]
    password: str
    commander_id: str | None = None

class UpdateUserSchema(BaseModel):
    personal_number: str | None = None
    name: str | None = None
    phone_number: str  | None = None
    role: Literal["SOLDIER", "COMMANDER"]  | None = None
    password: str  | None = None
    commander_id: str | None = None

def validate_new_user(body):
    return NewUserSchema(**body).model_dump()

def validate_update_user(body):
    data = UpdateUserSchema(**body).model_dump(exclude_unset=True)
    if len(data) == 0:
        abort(400, "No feilds were given")
    return data



