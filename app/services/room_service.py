from datetime import date # import date from datetime

from sqlalchemy.orm import Session # import Session from sqlalchemy.orm

from app.repositories.room_repository import (
    RoomRepository # import RoomRepository from app.repositories.room_repository
)

# import BookingRepository from app.repositories.booking_repository:
from app.repositories.booking_repository import (
    BookingRepository
)


# create RoomService class:
class RoomService:

    # initialize RoomService:
    def __init__(self, db: Session): # db: Session

        self.rooms = RoomRepository(db) # self.rooms
        self.bookings = BookingRepository(db) # self.bookings

    # get availability:
    def get_availability(
        self,
        room_id: int, # room id
        booking_date: date # booking date
    ):

        slots = self.rooms.get_room_slots(
            room_id
        ) # get room slots

        result = [] # result

        for slot in slots: # for each slot

            booking = (
                self.bookings
                .get_by_slot_and_date(
                    room_id,
                    slot.id,
                    booking_date
                )
            ) # get booking by slot and date

            result.append(
                {
                    "slot_id": slot.id,
                    "start_time": slot.start_time,
                    "end_time": slot.end_time,
                    "available": booking is None
                }
            ) # append result

        return result # return result