from datetime import date # import date from datetime

from sqlalchemy import select # import select from sqlalchemy
from sqlalchemy.orm import Session # import Session from sqlalchemy.orm

from app.models.booking import Booking # import Booking from app.models.booking


# create BookingRepository class:
class BookingRepository:

    # initialize BookingRepository:
    def __init__(self, db: Session): # db: Session
        self.db = db # self.db

    # create booking:
    def create(self, booking: Booking): # booking: Booking

        self.db.add(booking) # add booking
        self.db.commit() # commit
        self.db.refresh(booking) # refresh

        return booking
    
    # get booking by id:
    def get(self, booking_id: int): # booking_id: int

        return self.db.get(Booking, booking_id) # get booking by id
    
    # delete booking:
    def delete(self, booking: Booking): # booking: Booking

        self.db.delete(booking)
        self.db.commit()

    # get user bookings:
    def get_user_bookings(self, user_id: int): # user_id: int

        stmt = (
            select(Booking)
            .where(Booking.user_id == user_id)
        )

        return self.db.scalars(stmt).all()
    
    # get all bookings:
    def get_all(self):

        stmt = select(Booking)

        return self.db.scalars(stmt).all()
    
    # get booking by slot and date:
    def get_by_slot_and_date(
        self,
        room_id: int,
        slot_id: int,
        booking_date: date
    ):

        stmt = (
            select(Booking)
            .where(
                Booking.room_id == room_id,
                Booking.slot_id == slot_id,
                Booking.booking_date == booking_date
            )
        )

        return self.db.scalar(stmt)
    
    # get all bookings paginated:
    def get_all_paginated(
        self,
        limit: int,
        offset: int
    ):

        stmt = (
            select(Booking)
            .limit(limit)
            .offset(offset)
        )

        return self.db.scalars(stmt).all()