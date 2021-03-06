# Copyright (C) 2021, Pyronear contributors.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

from typing import List, Dict, Mapping, Any
from sqlalchemy import Table
from fastapi import HTTPException, status

from app.api import crud
from app.api.schemas import AccessType
from app.db import accesses


async def is_in_same_group(table: Table, entry_id: int, group_id: int) -> bool:
    entity_group_id = await crud.groups.get_entity_group_id(table, entry_id)
    return entity_group_id == group_id


async def is_access_in_group(access_id: int, group_id: int) -> bool:
    access_group_id = await crud.groups.get_entity_group_id(accesses, access_id)
    return access_group_id == group_id


async def is_admin_access(access_id: int) -> bool:
    access = await crud.base.get_entry(accesses, access_id)
    return access["scope"] == AccessType.admin


async def check_group_read(access_id: int, group_id: int) -> bool:
    if (not await is_admin_access(access_id)) and not (await is_access_in_group(access_id, group_id)):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You can't access this ressource")
    return True


async def check_group_update(access_id: int, group_id: int) -> bool:
    if (
            (group_id is not None)
            and (not await is_admin_access(access_id))
            and (not await is_access_in_group(access_id, group_id))):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You can't specify another group")
    return True
