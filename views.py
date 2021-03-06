from fastapi import APIRouter, Depends, HTTPException
from pydantic import PositiveInt
from sqlalchemy.orm import Session
from fastapi.responses import PlainTextResponse
from pydantic import constr
import crud
import schemas
from database import get_db

router = APIRouter()

TOKEN = "BASIC2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"


def check_for_message(db, msg_id):
    is_supp = crud.get_message(db, msg_id)
    if is_supp is None:
        raise HTTPException(status_code=404, detail="Not Okie Dokie ID")
    return is_supp


def check_auth(token):
    if token != TOKEN:
        raise HTTPException(status_code=401, detail="Wrong Token")


@router.post("/create_msg", response_model=schemas.Message, status_code=201)
async def creat_msg(msg: schemas.Message, db: Session = Depends(get_db)):
    check_auth(msg.Token)
    if msg.MessageText is None:
        raise HTTPException(status_code=404, detail="Really? Empty Message?")
    return crud.create_message(db, msg)


@router.put("/edit_msg/{msg_id}", response_model=schemas.Message, status_code=201)
async def edit_msg(msg_id: PositiveInt, msg: schemas.EditMessage, db: Session = Depends(get_db)):
    check_auth(msg.Token)
    db_msg = crud.get_message(db, msg_id)
    if db_msg is None:
        raise HTTPException(status_code=404, detail= "Msg not found")
    return crud.edit_message(db, msg, msg_id)


@router.delete("/delete_msg/{msg_id}", status_code=204)
async def delete_msg(msg_id: PositiveInt, auth: constr(max_length=100), db: Session = Depends(get_db)):
    check_auth(auth)
    db_msg = check_for_message(db, msg_id)
    crud.delete_message(db, msg_id)
    return PlainTextResponse("Deleted!", status_code=204)


@router.get("/info_msg/{msg_id}", status_code=200)
async def info_msg(msg_id: PositiveInt, db: Session = Depends(get_db)):
    db_msg = check_for_message(db, msg_id)
    return crud.view_message(db, msg_id)
