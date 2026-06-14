from datetime import date # import date from datetime

from fastapi import APIRouter # import router from fastapi
from fastapi import Depends # import depends from fastapi

from sqlalchemy.orm import Session # import session from sqlalchemy

from app.core.database import get_db # import get_db from app.core.database

# import room service from app.services.room_service:
from app.services.room_service import (
    RoomService
)

# import room repository from app.repositories.room_repository:
from app.repositories.room_repository import (
    RoomRepository
)

# create router for rooms:
router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)

# create endpoint for getting all rooms:
@router.get("")
def get_rooms(
    db: Session = Depends(get_db) # dependency for database session
):

    # create room repository:
    repo = RoomRepository(db)

    # return all rooms:
    return repo.get_all()


# create endpoint for getting room availability:
@router.get("/{room_id}/availability")
def availability(
    room_id: int, # room id
    date_value: date, # date
    db: Session = Depends(get_db) # dependency for database session
):

    # create room service:
    service = RoomService(db)

    # return room availability:
    return service.get_availability(
        room_id,
        date_value
    )