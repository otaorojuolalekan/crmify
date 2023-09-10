from fastapi import APIRouter, Depends, status, HTTPException
from api.utils import raiseAccount404
from api import models, schemas, oauth2
from sqlalchemy.orm import Session
from api.database import get_db
from typing import List

router = APIRouter(prefix='/api/accounts', tags=['ACCOUNTS'])


@router.get('/', response_model=List[schemas.AccountBase])
def get_accounts(db: Session = Depends(get_db)):
    accounts = db.query(models.Account).all()
    print("*********************************************")
    print(accounts)
    print("*********************************************")
    return (accounts)


@router.get('/{id}', response_model=schemas.AccountBase)
def get_account(id, db: Session = Depends(get_db)):
    account_query = db.query(models.Account).filter(models.Account.id == id)
    account = account_query.first()
    print("*********************************************")
    print(account_query)
    print("*********************************************")
    if account is None:
        raiseAccount404(id)
    return (account)


@router.get('/{account_id}/cases', response_model=List[schemas.CaseBase])
# ALL CASES RELATED TO ACCOUNT ID
def get_account_cases(account_id: int, db: Session = Depends(get_db)):
    """get all cases for {ACCOUNT ID}.... Authentication Not Required"""
    account = db.query(models.Account).filter(
        models.Account.id == account_id).first()
    if not account:
        raiseAccount404(account_id)
    print("*********************************************")
    print(account.id)
    print("*********************************************")
    cases_query = db.query(models.Case).filter(
        models.Case.account_id == account_id)
    cases = cases_query.all()
    return (cases)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.AccountBase)
def create_account(data: schemas.AccountCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    user = current_user.id
    print(user)
    data_dict = data.model_dump()
    new_account = models.Account(**data_dict)
    try:
        db.add(new_account)
        db.commit()
        db.refresh(new_account)
    except Exception as err:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='...account creation failed...')
    return (new_account)


# create case related to account
@router.post('/{id}/cases', status_code=status.HTTP_201_CREATED, response_model=schemas.CaseBase)
def create_case(id: int, data: schemas.CaseCreate,
                db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    """create case for specific account.... Authentication Required"""
    # verify that account exist
    account = db.query(models.Account).filter(models.Account.id == id).first()
    print(account)
    if not account:
        raiseAccount404(id)

    # create new cases associated with specified account
    case_data_dict = data.model_dump()
    new_case = models.Case(user_id=current_user.id, account_id=id,
                           **case_data_dict)
    print(case_data_dict)
    try:
        db.add(new_case)
        db.commit()
        db.refresh(new_case)
    except Exception as err:
        db.rollback()
        print("error:", err)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='...case creation failed...')
    return new_case


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_account(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    account_query = db.query(models.Account).filter(models.Account.id == id)
    account = account_query.first()
    if not account:
        raiseAccount404(id)
    account_query.delete()
    db.commit()


@router.put('/{id}')
def update_account(data: schemas.AccountCreate, id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    account_query = db.query(models.Account).filter(models.Account.id == id)
    account = account_query.first()
    if not account:
        raiseAccount404(id)
    account_query.update(data.model_dump())
    db.commit()
    return (account_query.first)
