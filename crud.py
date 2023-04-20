from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import desc

async def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit() 
    db.refresh(db_user)
    return db_user

async def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.userName == username).first()

async def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

async def get_all_users(db: Session):
    return db.query(models.User).all()

async def update_user(db: Session, user_id: int, user: schemas.UserBase):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

async def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

async def create_Todolist(db: Session, Todolist: schemas.TodolistCreate):
    db_Todolist = models.Todolist(**Todolist.dict())
    db.add(db_Todolist)
    db.commit()
    db.refresh(db_Todolist)
    return db_Todolist

async def get_Todolist_by_id(db: Session, Todolist_id: int):
    return db.query(models.Todolist).filter(models.Todolist.id == Todolist_id).first()

async def created_updated(db:Session,sort_by:str):
    query = db.query(models.Todolist)
    if sort_by == "created":
        query = query.order_by(desc(models.Todolist.id))
    elif sort_by == "updated":
        query = query.order_by(desc(models.Todolist.dueDate))
    return query.all()

async def completed(db: Session,completed: bool = None):
    if completed is not None:
        return db.query(models.Todolist).filter(models.Todolist.completed == completed).all()
    else:
        return None
             
async def update_Todolist(db: Session, Todolist_id: int, Todolist: schemas.TodolistBase):
    db_Todolist = db.query(models.Todolist).filter(models.Todolist.id == Todolist_id).first()
    if db_Todolist is None:
        return None
    Todo_data = Todolist.dict(exclude_unset=True)
    for key, value in Todo_data.items():
        setattr(db_Todolist, key, value)
    db.commit()
    db.refresh(db_Todolist)
    return db_Todolist

async def delete_Todolist(db: Session, Todolist_id: int):
    db_Todolist = db.query(models.Todolist).filter(models.Todolist.id == Todolist_id).first()
    if db_Todolist is None:
        return None
    db.delete(db_Todolist)
    db.commit()
    return db_Todolist

async def read_Todolist5(db: Session):
    return db.query(models.Todolist).limit(5).all()

async def get_Todolists(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.Todolist).offset(skip).limit(limit).all()