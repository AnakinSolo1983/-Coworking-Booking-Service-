from pydantic import BaseModel # import BaseModel from pydantic
from pydantic import ConfigDict # import ConfigDict from pydantic


# create RoomResponse schema:
class RoomResponse(BaseModel): # BaseModel

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int # id
    name: str # name
    description: str | None # description