from sqlalchemy import select # import select from sqlalchemy
from sqlalchemy.orm import Session # import Session from sqlalchemy.orm

from app.models.room import Room # import Room from app.models.room
from app.models.slot import TimeSlot # import TimeSlot from app.models.slot


# create RoomRepository class:
class RoomRepository:

    # initialize RoomRepository:
    def __init__(self, db: Session): # db: Session

        self.db = db # self.db

    # get all rooms:
    def get_all(self):

        stmt = select(Room) # select Room

        return self.db.scalars(stmt).all() # return all rooms

    # get room by id:
    def get_room(self, room_id: int): # room_id: int

        return self.db.get(Room, room_id) # get room by id

    # get slot by id:
    def get_slot(self, slot_id: int): # slot_id: int

        return self.db.get(TimeSlot, slot_id) # get slot by id

    # get room slots:
    def get_room_slots(self, room_id: int): # room_id: int

        stmt = (
            select(TimeSlot)
            .where(TimeSlot.room_id == room_id)
        )

        return self.db.scalars(stmt).all()