from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app, get_db
from database import engine
import models,database,schemas

client = TestClient(app)


def test_create_user(user):
    print(user)
    response = client.post("/users/", json=user)

def test_read_user(id):
    response = client.get(f"/users/{id}")
    data = response.json()
    print(data)

def test_update_user(id):
    new_user = schemas.UserCreate(
        userName="new_user",
        email="new@example.com",
        firstName="New",
        lastName="User",
        phoneNumber="555-5678",
        role="admin",
        password="new_password"
    )
    response = client.put(f"/users/{id}", json=new_user.dict())
    data = response.json()
    print(data)
test_create_user({
        'userName':"Paes",
        'email':"testPae@example.com",
        'firstName':"Test",
        'lastName':"User",
        'phoneNumber':"55522-1234",
        'role':"user",
        'password':"01"})
