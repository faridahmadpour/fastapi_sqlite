from typing import List, Optional
from pydantic import Json
from pydantic import BaseModel



class UserForm(BaseModel):
    form: Optional[Json]
    file_url: Optional[str]
    class Config:
        orm_mode = True

class UserFormDict(BaseModel):
    form: Optional[dict]
    file_url: Optional[str]
    class Config:
        orm_mode = True

class AllForm(BaseModel):
    all_forms: List[UserFormDict]

    class Config:
        orm_mode = True