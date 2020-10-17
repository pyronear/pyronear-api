from typing import List

from fastapi import APIRouter, Path, Security

from app.api import routing
from app.db import users
from app.api.schemas import UserOut, UserIn, UserOut
from app.api.deps import get_current_user

router = APIRouter()


@router.get("/me", response_model=UserOut)
async def get_my_user(current_user: UserOut = Security(get_current_user, scopes=["me"])):
    return current_user


@router.put("/update-me", response_model=UserOut)
async def update_me(payload: UserIn, me: UserOut = Security(get_current_user, scopes=["me"])):
    return await routing.update_entry(users, payload, me.id)


@router.post("/", response_model=UserOut, status_code=201)
async def create_user(payload: UserIn, _: UserOut = Security(get_current_user, scopes=["admin"])):
    return await routing.create_entry(users, payload)


@router.get("/{id}/", response_model=UserOut)
async def get_user(id: int = Path(..., gt=0), _: UserOut = Security(get_current_user, scopes=["admin"])):
    return await routing.get_entry(users, id)


@router.get("/", response_model=List[UserOut])
async def fetch_users(_: UserOut = Security(get_current_user, scopes=["admin"])):
    return await routing.fetch_entries(users)


@router.put("/{id}/", response_model=UserOut)
async def update_user(payload: UserIn, id: int = Path(..., gt=0), _: UserOut = Security(get_current_user, scopes=["admin"])):
    return await routing.update_entry(users, payload, id)


@router.delete("/{id}/", response_model=UserOut)
async def delete_user(id: int = Path(..., gt=0), _: UserOut = Security(get_current_user, scopes=["admin"])):
    return await routing.delete_entry(users, id)
