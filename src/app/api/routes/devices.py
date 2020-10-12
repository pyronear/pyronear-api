from typing import List
from fastapi import APIRouter, Path, Depends, HTTPException
from app.api import routing
from app.db import devices
from app.api.schemas import BaseDevice, Device, DeviceOut, DeviceIn, DeviceDBIn, HeartbeatOut, HeartbeatIn
from app.security import get_password_hash
from app.deps import get_current_active_device
from datetime import datetime

router = APIRouter()


@router.post("/", response_model=DeviceOut, status_code=201)
async def create_device(payload: DeviceIn):
    device = DeviceDBIn(**payload.dict(), hashed_password=get_password_hash(payload.password))
    return await routing.create_entry(devices, device)


@router.get("/{id}/", response_model=DeviceOut)
async def get_device(id: int = Path(..., gt=0)):
    return await routing.get_entry(devices, id)


@router.get("/", response_model=List[DeviceOut])
async def fetch_devices():
    return await routing.fetch_entries(devices)


@router.put("/{id}/", response_model=DeviceOut)
async def update_device(payload: DeviceIn, id: int = Path(..., gt=0)):
    return await routing.update_entry(devices, payload, id)


@router.post("/heartbeat", response_model=HeartbeatOut)
async def heartbeat(current_device: Device = Depends(get_current_active_device)):
    payload = dict(**current_device)
    payload["last_ping"] = datetime.utcnow()
    return await routing.update_entry(devices, BaseDevice(**payload), current_device["id"])


@router.delete("/{id}/", response_model=DeviceOut)
async def delete_device(id: int = Path(..., gt=0)):
    return await routing.delete_entry(devices, id)
