from typing import List, Optional,Annotated,Union
from pydantic import BaseModel, EmailStr
from datetime import datetime
from fastapi import Body

class UserBase(BaseModel):
    userName: str
    email: EmailStr
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phoneNumber: Optional[str] = None
    role: Optional[str] = None


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class TodolistBase(BaseModel):
    title: str
    dueDate: Annotated[Union[datetime, None], Body()] = None
    description: Optional[str] = None
    completed: Optional[bool] = False
    
class TodolistCreate(TodolistBase):
    owner_id: int

class TodoUpdate(TodolistBase):
    pass

class TodoList(TodolistBase):
    id: int
    class Config:
        orm_mode = True


class UserList(UserBase):
    id: int

    class Config:
        orm_mode = True
