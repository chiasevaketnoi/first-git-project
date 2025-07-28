from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from my_app.models import User, UserCreate, UserRead
from my_app.services import UserService
from my_app.database import get_db

router = APIRouter()

@router.post("/users/", response_model=UserRead)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = User(name=user.name, age=user.age, email=user.email)
    user_obj = await UserService.create_user(db_user, db)
    return user_obj

@router.get("/users/", response_model=List[UserRead])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await UserService.get_users(db)

@router.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await UserService.get_user(user_id, db)

@router.put("/users/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user_update: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = User(name=user_update.name, age=user_update.age, email=user_update.email)
    db_user.id = user_id
    return await UserService.update_user(user_id, db_user, db)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await UserService.delete_user(user_id, db)
