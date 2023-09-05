from fastapi import APIRouter, Depends, status, HTTPException
from ..utils import raiseCase404
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix='/api/cases', tags=['CASES'])

# ALL CASES


@router.get('/', response_model=List[schemas.CaseBase])
def get_cases(db: Session = Depends(get_db)):
    """get all cases.... Authentication Not Required"""
    cases = db.query(models.Case).all()
    return (cases)

# SINGLE CASE ID


@router.get('/{id}', response_model=schemas.CaseBase)
def get_case(id, db: Session = Depends(get_db)):
    """get single case.... Authentication Not Required"""
    case = db.query(models.Case).filter(models.Case.id == id).first()
    if case is None:
        raiseCase404(id)
    return (case)

@router.get('/{id}/updates', response_model=List[schemas.UpdateOutput])
# ALL UPDATES RELATED TO CASE ID
def get_account_cases(id: int, db: Session = Depends(get_db)):
    """get all cases for {ACCOUNT ID}.... Authentication Not Required"""
    case = db.query(models.Case).filter(
        models.Case.id == id).first()
    if not case:
        raiseCase404(id)
    updates_query = db.query(models.Update).filter(
        models.Update.case_id == id)
    updates = updates_query.all()
    return (updates)

# create update for case_id
@router.post('/{id}/updates', status_code=status.HTTP_201_CREATED, response_model=schemas.UpdateOutput)
def create_update(id: int, data: schemas.UpdateBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    user = current_user.id
    case = db.query(models.Case).filter(models.Case.id == id).first()
    if not case:
        raiseCase404(id)
    data_dict = data.model_dump()
    new_update = models.Update(user_id=user, case_id=id, **data_dict)
    try:
        db.add(new_update)
        db.commit()
        db.refresh(new_update)
    except Exception as err:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='...update creation failed...')
    return (new_update)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_case(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    """delete case.... Authentication Required"""
    case_query = db.query(models.Case).filter(models.Case.id == id)
    case = case_query.first()
    if not case:
        raiseCase404(id)
    case_query.delete()
    db.commit()


@router.patch('/{id}', response_model=schemas.CaseBase)
def update_case(data: schemas.CasePatch, id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    """update case.... Authentication Required"""
    case_query = db.query(models.Case).filter(models.Case.id == id)
    case = case_query.first()
    if not case:
        raiseCase404(id)
    case_query.update(data.model_dump())
    db.commit()
    return (case_query.first())
