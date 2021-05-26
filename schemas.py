import typing

from pydantic import BaseModel, PositiveInt, constr


class Message(BaseModel):
    MessageID: typing.Optional[PositiveInt]
    MessageText: typing.Optional[constr(max_length=160)]
    Counter: typing.Optional[PositiveInt]
    Token: typing.Optional[constr(max_length=100)]

    class Config:
        orm_mode = True


class EditMessage(BaseModel):
    Message: typing.Optional[constr(max_length=160)] = None
    Token: typing.Optional[constr(max_length=100)]

    class Config:
        orm_mode = True
