from fastapi import Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from api import schemas, models, utils, oauth2
from api.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix='/login', tags=['AUTHENTICATION'])


@router.post('/', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # check for valid email address
    user =\
        db.query(models.User).filter(
            models.User.email == user_credentials.username).first()
    if user is None:
        utils.raiseInvalidCredException()

    # check for valid password
    if not utils.verify(user_credentials.password, user.password):
        utils.raiseInvalidCredException()

    access_token = oauth2.create_access_token(
        {"user_id": user.id, "username": user.username})
    return {"access_token": access_token, "token_type": "bearer token"}
