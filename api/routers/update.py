from fastapi import APIRouter, Depends, status, HTTPException
from api.utils import raiseUpdate404
from api import models, schemas, oauth2
from sqlalchemy.orm import Session
from api.database import get_db
from typing import List

router = APIRouter(prefix='/api/updates', tags=['UPDATES'])


@router.get('/', response_model=List[schemas.UpdateOutput])
def get_updates(db: Session = Depends(get_db)):
    updates = db.query(models.Update).all()
    return (updates)


@router.get('/{id}', response_model=schemas.UpdateOutput)
def get_update(id, db: Session = Depends(get_db)):
    update = db.query(models.Update).filter(models.Update.id == id).first()
    if update is None:
        raiseUpdate404(id)
    return (update)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_update(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    update_query = db.query(models.Update).filter(models.Update.id == id)
    update = update_query.first()
    if not update:
        raiseUpdate404(id)
    update_query.delete()
    db.commit()


@router.put('/{id}', response_model=schemas.UpdateOutput)
def update_update(data: schemas.UpdateBase, id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    update_query = db.query(models.Update).filter(models.Update.id == id)
    update = update_query.first()
    if not update:
        raiseUpdate404(id)
    update_query.update(data.model_dump())
    db.commit()
    return (update_query.first())
