from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import PositiveInt, ValidationError, constr
from sqlalchemy.orm import Session
from fastapi.responses import Response

import crud
import schemas
import models
from database import get_db

router = APIRouter()


def check_for_message(db, msg_id):
    is_supp = crud.get_message(db, msg_id)
    if is_supp is None:
        raise HTTPException(status_code=404, detail="Not Okie Dokie ID")
    return is_supp


@router.post("/create_msg", response_model=schemas.Message, status_code=201)
async def creat_msg(msg: schemas.Message, db: Session = Depends(get_db)):
    return crud.create_message(db, msg)


@router.put("/edit_msg/{msg_id}",response_model=schemas.Message, status_code=201) #licznik wyswietlen = 0
async def edit_msg(msg_id: PositiveInt, msg: schemas.Message, db: Session = Depends(get_db)):
    db_msg = crud.get_message(db, msg_id)
    if db_msg is None:
        raise HTTPException(status_code=404, detail= "Msg not found")
    return crud.edit_message(db, msg, msg_id)


@router.delete("/delete_msg/{msg_id}")
async def delete_msg(msg_id: PositiveInt, db: Session = Depends(get_db)):
    db_msg = check_for_message(db, msg_id)
    crud.delete_message(db, msg_id)
    return Response(status_code=204)


@router.get("/info_msg/{msg_id}")    #licznik wyświetlen i wiadmosc
async def info_msg(msg_id: PositiveInt, db: Session = Depends(get_db)):
    db_msg = check_for_message(db, msg_id)

    return crud.view_message(db, msg_id)


