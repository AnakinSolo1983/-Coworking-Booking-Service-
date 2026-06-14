from datetime import date # import date from datetime

from pydantic import BaseModel # import BaseModel from pydantic
from pydantic import ConfigDict # import ConfigDict from pydantic

# create CreateBookingRequest schema:
class CreateBookingRequest(BaseModel): # BaseModel
    
    room_id: int # room id
    slot_id: int # slot id
    booking_date: date # booking date

# create BookingResponse schema:
class BookingResponse(BaseModel): # BaseModel

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int # id
    room_id: int # room id
    slot_id: int # slot id
    user_id: int # user id
    booking_date: date # booking date