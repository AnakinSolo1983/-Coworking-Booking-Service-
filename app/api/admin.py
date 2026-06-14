from fastapi import APIRouter # import router from fastapi
from fastapi import Depends # import depends from fastapi

from sqlalchemy.orm import Session # import session from sqlalchemy

from app.core.database import get_db # import get_db from app.core.database

# import admin_required from app.dependencies.auth:
from app.dependencies.auth import (
    admin_required
)

# import booking_repository from app.repositories.booking_repository:
from app.repositories.booking_repository import (
    BookingRepository
)

# create router for admin:
router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

# create endpoint for all bookings:
@router.get("/bookings")
def all_bookings(
    limit: int = 20, # limit of bookings per page
    offset: int = 0, # offset of bookings per page
    db: Session = Depends(get_db), # dependency for database session
    _=Depends(admin_required) # dependency for admin authentication
):

    # create booking repository:
    repo = BookingRepository(db)

    # return all bookings:
    return repo.get_all_paginated(
        limit=limit,
        offset=offset
    )