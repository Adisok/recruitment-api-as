import typing

from pydantic import BaseModel, PositiveInt, constr


class Message(BaseModel):
    MessageID: typing.Optional[PositiveInt]
    MessageText: typing.Optional[constr(max_length=160)]
    Counter: typing.Optional[PositiveInt]

    class Config:
        orm_mode = True


