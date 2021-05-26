import models
import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException


def get_message(db, msg_id):
    return db.query(models.Content).filter(models.Content.MessageID == msg_id).first()


def create_message(db: Session, msg: schemas.Message):
    msg_id = db.query(models.Content).count() + 1
    db_msg = models.Content(
        MessageID=msg_id,
        MessageText=msg.MessageText,
        Counter=1
    )
    db.add(db_msg)
    db.commit()
    db.refresh(db_msg)
    return db_msg


def edit_message(db: Session, msg: schemas.Message, msg_id: int):
    new_vals = {key: val for key,val in dict(msg).items() if val is not None}
    new_vals["Counter"] = 1
    if new_vals:
        db.query(models.Content).filter(models.Content.MessageID == msg_id).update(values=new_vals)
    db.commit()
    pass


def delete_message(db: Session, msg_id: int):
    db.query(models.Content).filter(models.Content.MessageID == msg_id).delete()
    db.commit()
    pass


def view_message(db: Session, msg_id: int):
    counter = db.query(models.Content.Counter).filter(models.Content.MessageID == msg_id).first()[0] + 1
    db.query(models.Content).filter(models.Content.MessageID == msg_id).update(values={"Counter": counter})
    db.commit()
    return db.query(models.Content).filter(models.Content.MessageID == msg_id).first()




