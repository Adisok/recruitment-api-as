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

def check_for_supplier(db, supp_id):
    is_supp = crud.get_supplier(db, supp_id)
    if is_supp is None:
        raise HTTPException(status_code=404, detail="Not Okie Dokie ID")
    return is_supp


@router.get("/shippers/{shipper_id}", response_model=schemas.Shipper)
async def get_shipper(shipper_id: PositiveInt, db: Session = Depends(get_db)):
    db_shipper = crud.get_shipper(db, shipper_id)
    if db_shipper is None:
        raise HTTPException(status_code=404, detail="Shipper not found")
    return db_shipper

@router.get("/create_msg")
async def creat_msg(msg: constr(max_length=160), db: Session = Depends(get_db)):
    pass

@router.put("/edit_msg/{msg_id}") #licznik wyswietlen = 0
async def edit_msg(msg_id: PositiveInt, db: Session = Depends(get_db)):
    pass

@router.delete("/delete_msg/{msg_id}")
async def delete_msg(msg_id: PositiveInt, db: Session = Depends(get_db)):
    pass

@router.get("/info_msg/{msg_id}")    #licznik wyświetlen i wiadmosc
async def info_msg(msg_id: PositiveInt, db: Session = Depends(get_db)):
    pass


