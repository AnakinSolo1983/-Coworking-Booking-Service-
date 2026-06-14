from .user import User # import User from app.models.user
from .room import Room # import Room from app.models.room
from .slot import TimeSlot # import TimeSlot from app.models.slot
from .booking import Booking # import Booking from app.models.booking

# export all models:
__all__ = [
    "User",
    "Room",
    "TimeSlot",
    "Booking",
]