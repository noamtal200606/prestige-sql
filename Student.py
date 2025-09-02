from pydantic import BaseModel, constr


class Student(BaseModel):
    id: constr(regex=r'^\d{9}$')
    grade: str
    name: str
    age: int