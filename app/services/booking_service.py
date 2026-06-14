from datetime import date # import date from datetime

from fastapi import HTTPException # import HTTPException from fastapi

from sqlalchemy.orm import Session # import Session from sqlalchemy.orm

from app.models.booking import Booking # import Booking from app.models.booking

from app.repositories.room_repository import (
    RoomRepository # import RoomRepository from app.repositories.room_repository
)

from app.repositories.booking_repository import (
    BookingRepository # import BookingRepository from app.repositories.booking_repository
)


# create BookingService class:
class BookingService:

    # initialize BookingService:
    def __init__(self, db: Session): # db: Session

        self.rooms = RoomRepository(db) # self.rooms
        self.bookings = BookingRepository(db) # self.bookings

    # create booking:
    def create_booking(
        self,
        room_id: int, # room id
        slot_id: int, # slot id
        user_id: int, # user id
        booking_date: date # booking date
    ):

        room = self.rooms.get_room(room_id) # get room by room id

        if not room: # if room not found

            raise HTTPException(
                404,
                "Room not found"
            )

        slot = self.rooms.get_slot(slot_id) # get slot by slot id

        if not slot: # if slot not found

            raise HTTPException(
                404,
                "Slot not found"
            )

        existing = (
            self.bookings
            .get_by_slot_and_date(
                room_id,
                slot_id,
                booking_date
            )
        )

        if existing: # if booking already exists

            raise HTTPException(
                409,
                "Slot already booked"
            )

        booking = Booking(
            room_id=room_id,
            slot_id=slot_id,
            user_id=user_id,
            booking_date=booking_date
        )

        if slot.room_id != room_id: # if slot does not belong to room

            raise HTTPException(
                400,
                "Slot does not belong to room"
            )

        return self.bookings.create(
            booking
        ) # return booking