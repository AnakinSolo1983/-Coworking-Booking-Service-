import sys # import sys
from pathlib import Path # import Path from pathlib

# add project root to sys.path:
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from datetime import time # import time from datetime
import app.models # import models from app.models

from app.core.database import SessionLocal # import SessionLocal from app.core.database

from app.models.user import User # import User from app.models.user
from app.models.user import UserRole # import UserRole from app.models.user

from app.models.room import Room # import Room from app.models.room
from app.models.slot import TimeSlot # import TimeSlot from app.models.slot
from app.models.booking import Booking # import Booking from app.models.booking

from app.core.security import hash_password # import hash_password from app.core.security


# create database session:
db = SessionLocal()

# create admin user:
admin = User(
    username="admin",
    password_hash=hash_password("admin123"),
    role=UserRole.ADMIN
)

# create employee user:
employee = User(
    username="user",
    password_hash=hash_password("user123"),
    role=UserRole.EMPLOYEE
)

db.add(admin) # add admin user
db.add(employee) # add employee user

# create rooms:
room_a = Room(
    name="Room A",
    description="Large meeting room"
)

room_b = Room(
    name="Room B",
    description="Small meeting room"
)

db.add(room_a) # add room A
db.add(room_b) # add room B

db.commit() # commit changes

db.refresh(room_a) # refresh room A
db.refresh(room_b) # refresh room B

# create time slots:
slots = [

    TimeSlot(
        room_id=room_a.id,
        start_time=time(9, 0),
        end_time=time(11, 0)
    ),

    TimeSlot(
        room_id=room_a.id,
        start_time=time(13, 0),
        end_time=time(16, 0)
    ),

    TimeSlot(
        room_id=room_b.id,
        start_time=time(9, 0),
        end_time=time(12, 0)
    ),

    TimeSlot(
        room_id=room_b.id,
        start_time=time(14, 0),
        end_time=time(18, 0)
    ),
]

db.add_all(slots) # add all slots
db.commit() # commit changes

print("Seed completed") # print seed completed