from pydantic import BaseModel,validator,Field
from datetime import date
from typing import List



class Genre(BaseModel):

    name:str


class Author(BaseModel):

    name: str = Field(...,min_length=5 , max_length=25)
    last_name: str
    age: int= Field(...,gt=15, lt=90, description="Author age must be more than 15 and less than 90")

    # @validator('age')
    # def check_age(cls,v):
    #     if v<15:
    #         raise ValueError('The author age must be more than 15')
    #     else:
    #         return v

class Book(BaseModel):
    title:  str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int

    
class Task(BaseModel):
    task: str
    completed: bool = False


class TaskSchedule(BaseModel):
    task: str
    scheduled_time: str