from pydantic import BaseModel
from datetime import date
from typing import Optional

class PatientBaseModel(BaseModel):
    first_name:str
    last_name:str
    dob:date
    gender:str
    phone:str


class PatientCreate(PatientBaseModel):
    pass

class PatientUpdate(BaseModel):
    pass

class PatientResponse(BaseModel):
    id: int

    class config:
        orm_mode = True

        