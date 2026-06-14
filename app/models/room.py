from sqlalchemy import String # import String from sqlalchemy
from sqlalchemy.orm import Mapped # import Mapped from sqlalchemy.orm
from sqlalchemy.orm import mapped_column # import mapped_column from sqlalchemy.orm
from sqlalchemy.orm import relationship # import relationship from sqlalchemy.orm

from app.core.database import Base # import Base from app.core.database


# create Room class:
class Room(Base):

    __tablename__ = "rooms" # table name

    id: Mapped[int] = mapped_column(primary_key=True) # primary key

    # room name:
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    # room description:
    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    # slots relationship:
    slots = relationship(
        "TimeSlot", # time slot
        back_populates="room", # back populates
        cascade="all, delete-orphan" # cascade
    )

    # bookings relationship:
    bookings = relationship(
        "Booking", # booking
        back_populates="room", # back populates
        cascade="all, delete-orphan" # cascade
    )