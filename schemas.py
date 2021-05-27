import typing

from pydantic import BaseModel, PositiveInt, constr


class Message(BaseModel):
    MessageID: typing.Optional[PositiveInt] = 1
    MessageText: typing.Optional[constr(max_length=160)] = None
    Counter: typing.Optional[PositiveInt] = 1
    Token: typing.Optional[constr(max_length=100)] = None

    class Config:
        orm_mode = True


class EditMessage(BaseModel):
    Message: typing.Optional[constr(max_length=160)] = None
    Token: typing.Optional[constr(max_length=100)] = None

    class Config:
        orm_mode = True
