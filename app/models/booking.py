from datetime import date # import date from datetime
from datetime import datetime # import datetime from datetime

from sqlalchemy import Date # import Date from sqlalchemy
from sqlalchemy import DateTime # import DateTime from sqlalchemy
from sqlalchemy import ForeignKey # import ForeignKey from sqlalchemy
from sqlalchemy import UniqueConstraint # import UniqueConstraint from sqlalchemy
from sqlalchemy.orm import Mapped # import Mapped from sqlalchemy.orm
from sqlalchemy.orm import mapped_column # import mapped_column from sqlalchemy.orm
from sqlalchemy.orm import relationship # import relationship from sqlalchemy.orm

from app.core.database import Base # import Base from app.core.database


# create Booking class:
class Booking(Base):

    __tablename__ = "bookings" # table name

    # table arguments:
    __table_args__ = (
        UniqueConstraint(
            "room_id",
            "slot_id",
            "booking_date",
            name="uq_room_slot_date"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True) # primary key

    # room id:
    room_id: Mapped[int] = mapped_column(
        ForeignKey("rooms.id")
    )

    # slot id:
    slot_id: Mapped[int] = mapped_column(
        ForeignKey("time_slots.id")
    )

    # user id:
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    # booking date:
    booking_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    # created at:
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # room relationship:
    room = relationship(
        "Room",
        back_populates="bookings"
    )

    # slot relationship:
    slot = relationship(
        "TimeSlot",
        back_populates="bookings"
    )

    # user relationship:
    user = relationship(
        "User",
        back_populates="bookings"
    )