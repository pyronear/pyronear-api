# Copyright (C) 2021, Pyronear contributors.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

from typing import List
from fastapi import APIRouter, Path, Security, Depends
from sqlalchemy import and_, or_
from datetime import datetime
from app.api import crud
from app.db import installations, database, get_session, models
from app.api.schemas import InstallationOut, InstallationIn, AccessType
from app.api.deps import get_current_access
from app.api.crud.authorizations import is_admin_access, check_group_read, check_group_update
from app.api.crud.groups import get_entity_group_id

router = APIRouter()


@router.post("/", response_model=InstallationOut, status_code=201, summary="Create a new installation")
async def create_installation(
    payload: InstallationIn,
    _=Security(get_current_access, scopes=[AccessType.admin])
):
    """Creates a new installation based on the given information

    Below, click on "Schema" for more detailed information about arguments
    or "Example Value" to get a concrete idea of arguments
    """
    return await crud.create_entry(installations, payload)


@router.get("/{installation_id}/", response_model=InstallationOut,
            summary="Get information about a specific installation")
async def get_installation(
    installation_id: int = Path(..., gt=0),
    requester=Security(get_current_access, scopes=[AccessType.admin, AccessType.user])
):
    """
    Based on a installation_id, retrieves information about the specified installation
    """
    requested_group_id = await get_entity_group_id(installations, installation_id)
    await check_group_read(requester.id, requested_group_id)
    return await crud.get_entry(installations, installation_id)


@router.get("/", response_model=List[InstallationOut], summary="Get the list of all installations")
async def fetch_installations(
    requester=Security(get_current_access, scopes=[AccessType.admin, AccessType.user]),
    session=Depends(get_session)
):
    """
    Retrieves the list of all installations and their information
    """
    if await is_admin_access(requester.id):
        return await crud.fetch_all(installations)
    else:
        retrieved_installations = (session.query(models.Installations)
                                   .join(models.Sites)
                                   .filter(models.Sites.group_id == requester.group_id).all())
        retrieved_installations = [x.__dict__ for x in retrieved_installations]
        return retrieved_installations


@router.put("/{installation_id}/", response_model=InstallationOut,
            summary="Update information about a specific installation")
async def update_installation(
    payload: InstallationIn,
    installation_id: int = Path(..., gt=0),
    requester=Security(get_current_access, scopes=[AccessType.admin, AccessType.user])
):
    """
    Based on a installation_id, updates information about the specified installation
    """
    requested_group_id = await get_entity_group_id(installations, installation_id)
    await check_group_update(requester.id, requested_group_id)
    return await crud.update_entry(installations, payload, installation_id)


@router.delete("/{installation_id}/", response_model=InstallationOut, summary="Delete a specific installation")
async def delete_installation(
    installation_id: int = Path(..., gt=0),
    _=Security(get_current_access, scopes=[AccessType.admin])
):
    """
    Based on a installation_id, deletes the specified installation
    """
    return await crud.delete_entry(installations, installation_id)


@router.get("/site-devices/{site_id}", response_model=List[int],
            summary="Get all devices related to a specific site")
async def get_active_devices_on_site(
    site_id: int = Path(..., gt=0),
    requester=Security(get_current_access, scopes=[AccessType.admin, AccessType.user]),
    session=Depends(get_session)
):
    """
    Based on a site_id, retrieves the list of all the related devices and their information
    """
    current_ts = datetime.utcnow()

    query = (session.query(models.Installations)
                    .join(models.Sites)
                    .filter(and_(models.Sites.id == site_id,
                                 models.Installations.start_ts <= current_ts,
                                 or_(models.Installations.end_ts.is_(None),
                                     models.Installations.end_ts >= current_ts)
                                 )))

    if not await is_admin_access(requester.id):
        # Restrict on the group_id of the requester
        query = query.filter(models.Sites.group_id == requester.group_id)

    retrieved_device_ids = [x.__dict__['device_id'] for x in query.all()]
    return retrieved_device_ids
