from fastapi import APIRouter
from fastapi import APIRouter, Depends, status, HTTPException
from api.utils import raiseUser404
from api import models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from api.database import get_db
from typing import List

router = APIRouter(prefix='/api/users', tags=['USERS'])


@router.get('/', response_model=List[schemas.UserBase])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return (users)


@router.get('/{id}', response_model=schemas.UserBase)
def get_user(id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raiseUser404(id)
    return (user)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOutput)
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    data_dict = data.model_dump()
    new_user = models.User(**data_dict)
    # hash the string-password-input
    password_hash = utils.hash(new_user.password)
    new_user.password = password_hash
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return (new_user)
    except Exception as err:
        db.rollback()
        print(err)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='...user creation failed...')


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if not user:
        raiseUser404(id)
    user_query.delete()
    db.commit()


@router.put('/{id}', response_model=schemas.UserBase)
def update_user(data: schemas.UserBase, id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if not user:
        raiseUser404(id)
    user_query.user(data.model_dump(), synchronize_session=False)
    db.commit()
    return (user_query.first())
