from sqlalchemy import Table
from pydantic import BaseModel
from typing import Optional, Tuple, Any
from fastapi import HTTPException, Path

from app.api import crud, security
from app.api.schemas import UserAuth, UserCreation, UserRead
from app.api.schemas import AccessIn, AccessRead
from app.api.schemas import DeviceAuth, DeviceCreation, DeviceOut
from app.db import access as access_table


async def create_entry(table: Table, payload: BaseModel):
    entry_id = await crud.post(payload, table)
    return {**payload.dict(), "id": entry_id}


async def get_entry(table: Table, entry_id: int = Path(..., gt=0)):
    entry = await crud.get(entry_id, table)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry


async def fetch_entries(table: Table, query_filter: Optional[Tuple[str, Any]] = None):
    return await crud.fetch_all(table, query_filter)


async def fetch_entry(table: Table, query_filter: Tuple[str, Any]):
    return await crud.fetch_one(table, query_filter)


async def update_entry(table: Table, payload: BaseModel, entry_id: int = Path(..., gt=0)):
    await get_entry(table, entry_id)
    entry_id = await crud.put(entry_id, payload, table)

    return {**payload.dict(), "id": entry_id}


async def delete_entry(table: Table, entry_id: int = Path(..., gt=0)):
    entry = await get_entry(table, entry_id)
    await crud.delete(entry_id, table)

    return entry


async def create_access(username: str, password: str, scopes: str) -> AccessRead:
    # Hash the password
    pwd = await security.hash_password(password)
    access = AccessIn(username=username, hashed_password=pwd, scopes=scopes)
    access_entry = AccessRead(** await create_entry(access_table, access))
    return access_entry


async def create_user(user_table: Table, payload: UserAuth) -> UserRead:
    # Check that username does not already exist
    if await fetch_entry(user_table, ('username', payload.username)) is not None:
        raise HTTPException(
            status_code=400,
            detail=f"An entry with username='{payload.username}' already exists.",
        )
    access_entry = await create_access(payload.username, payload.password, scopes=payload.scopes)
    user = UserCreation(username=payload.username, access_id=access_entry.id)
    return await create_entry(user_table, user)


async def create_device(device_table: Table, payload: DeviceAuth) -> DeviceOut:
    # Check that device does not already exist
    if await fetch_entry(device_table, ('name', payload.name)) is not None:
        raise HTTPException(
            status_code=400,
            detail=f"An entry with name='{payload.name}' already exists.",
        )
    access_entry = await create_access(payload.name, payload.password, scopes=payload.scopes)
    payload = DeviceCreation(**payload.dict(), access_id=access_entry.id)
    return await create_entry(device_table, payload)
