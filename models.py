from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String(50), unique=True, index=True)
    email = Column(String(320), unique=True, index=True)
    firstName = Column(String(50), nullable=True)
    lastName = Column(String(50), nullable=True)
    phoneNumber = Column(String(20), nullable=True)
    role = Column(String(20), nullable=True)
    password = Column(String(200))

    todolists = relationship("Todolist", back_populates="owner")


class Todolist(Base):
    __tablename__ = "todolists"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    dueDate = Column(DateTime, nullable=True)
    description = Column(String(200), nullable=True)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="todolists")
