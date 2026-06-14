from fastapi import APIRouter # import router from fastapi
from fastapi import Depends # import depends from fastapi
from fastapi import HTTPException # import http exception from fastapi

from sqlalchemy.orm import Session # import session from sqlalchemy

from app.core.database import get_db # import get_db from app.core.database

# import get_current_user from app.dependencies.auth:
from app.dependencies.auth import (
    get_current_user
)

# import user model from app.models.user:
from app.models.user import User
from app.models.user import UserRole

from app.schemas.booking import (
    CreateBookingRequest
)

from app.services.booking_service import (
    BookingService
)

from app.repositories.booking_repository import (
    BookingRepository
)

# create router for bookings:
router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

# create endpoint for creating a booking:
@router.post("")
def create_booking(
    request: CreateBookingRequest, # request for creating a booking
    db: Session = Depends(get_db), # dependency for database session
    user: User = Depends(get_current_user) # dependency for current user
):

    # create booking service:
    service = BookingService(db)

    # create booking:
    return service.create_booking(
        room_id=request.room_id,
        slot_id=request.slot_id,
        user_id=user.id,
        booking_date=request.booking_date
    )

# create endpoint for getting current user's bookings:
@router.get("/me")
def my_bookings(
    db: Session = Depends(get_db), # dependency for database session
    user: User = Depends(get_current_user) # dependency for current user
):

    # create booking repository:
    repo = BookingRepository(db)

    # return current user's bookings:
    return repo.get_user_bookings(
        user.id
    )

# create endpoint for cancelling a booking:
@router.delete("/{booking_id}")
def cancel_booking(
    booking_id: int, # booking id
    db: Session = Depends(get_db), # dependency for database session
    user: User = Depends(get_current_user) # dependency for current user
):

    # create booking repository:
    repo = BookingRepository(db)

    # get booking by id:
    booking = repo.get(booking_id)

    # if booking is not found, raise http exception:
    if not booking:

        raise HTTPException(
            404,
            "Booking not found"
        )

    # if booking is not owned by current user and user is not admin, raise http exception:
    if (
        booking.user_id != user.id
        and user.role != UserRole.ADMIN
    ):
        raise HTTPException(
            403,
            "Forbidden"
        )

    # delete booking:
    repo.delete(booking)

    # return status:
    return {
        "status": "deleted"
    }