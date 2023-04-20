from fastapi import FastAPI, Depends, HTTPException, status,Query
from sqlalchemy.orm import Session
from typing import List,Optional
import models,crud,database,schemas

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

async def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

########### Users ##########   

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_username(db, username=user.userName)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return await crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = await crud.get_all_users(db)
    return users

@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user: schemas.UserBase, db: Session = Depends(get_db)):
    updated_user = await crud.update_user(db, user_id=user_id, user=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = await crud.delete_user(db, user_id=user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

########### Todolist ##########

@app.post("/Todolists/", response_model=schemas.TodoList)
async def create_Todolist(Todolist: schemas.TodolistCreate, db: Session = Depends(get_db)):
    return await crud.create_Todolist(db=db, Todolist=Todolist)

@app.get("/Todolists/{Todolist_id}", response_model=schemas.TodoList)
async def read_Todolist(Todolist_id: int, db: Session = Depends(get_db)):
    db_Todolist = await crud.get_Todolist_by_id(db, Todolist_id=Todolist_id)
    if db_Todolist is None:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return db_Todolist

@app.put("/Todolists/{Todolist_id}", response_model=schemas.TodoList)
async def update_Todolist(Todolist_id: int, Todolist: schemas.TodolistBase, db: Session = Depends(get_db)):
    updated_Todolist = await crud.update_Todolist(db, Todolist_id=Todolist_id, Todolist=Todolist)
    if updated_Todolist is None:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return updated_Todolist

@app.delete("/Todolists/{Todolist_id}", response_model=schemas.TodoList)
async def delete_Todolist(Todolist_id: int, db: Session = Depends(get_db)):
    deleted_Todolist = await crud.delete_Todolist(db, Todolist_id=Todolist_id)
    if deleted_Todolist is None:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return deleted_Todolist

@app.get("/Todolists/created_updated/")
async def created_updated(sort_by:str = Query("created",enum=["created","updated"]),db:Session=Depends(get_db)):
    db_Todolist = await crud.created_updated(db=db,sort_by=sort_by)
    if db_Todolist is None:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return db_Todolist

@app.get("/Todolists/completed/")
async def completed(completed: Optional[bool] = None,db: Session = Depends(get_db)):
    db_Todolist = await crud.completed(db=db,completed=completed)
    if db_Todolist is None:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return db_Todolist

@app.get("/Todolists/show5")
async def read_Todolist5(db:Session = Depends(get_db)):
    db_Todolist = await crud.read_Todolist5(db=db)
    if db_Todolist is None:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return db_Todolist

@app.get("/Todolists/show_skip_limit/", response_model=List[schemas.TodoList])
async def read_Todolists(skip: int = 0,limit: int = 5,db: Session = Depends(get_db)):
    db_Todolist = await crud.get_Todolists(db, skip=skip, limit=limit)
    if db_Todolist is None:
        raise HTTPException(status_code=404, detail="TodoList not found")
    return db_Todolist