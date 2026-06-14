from datetime import time # import time from datetime

from sqlalchemy import ForeignKey # import ForeignKey from sqlalchemy
from sqlalchemy import Time # import Time from sqlalchemy
from sqlalchemy.orm import Mapped # import Mapped from sqlalchemy.orm
from sqlalchemy.orm import mapped_column # import mapped_column from sqlalchemy.orm
from sqlalchemy.orm import relationship # import relationship from sqlalchemy.orm

from app.core.database import Base # import Base from app.core.database


# create TimeSlot class:
class TimeSlot(Base):

    __tablename__ = "time_slots" # table name

    id: Mapped[int] = mapped_column(primary_key=True) # primary key

    # room id:
    room_id: Mapped[int] = mapped_column(
        ForeignKey("rooms.id")
    )

    # start time:
    start_time: Mapped[time] = mapped_column(
        Time,
        nullable=False
    )

    # end time:
    end_time: Mapped[time] = mapped_column(
        Time,
        nullable=False
    )

    # room relationship:
    room = relationship(
        "Room", # room
        back_populates="slots" # back populates
    )

    # bookings relationship:
    bookings = relationship(
        "Booking", # booking
        back_populates="slot" # back populates
    )