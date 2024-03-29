from datetime import datetime, timedelta
from jose import JWTError, jwt
from api import schemas, models
from api.database import get_db
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES'))



def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    # decode the encoded access token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        username: str = payload.get("username")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id, username=username)
    except JWTError:
        raise credentials_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Unable to Authenticate credentials", headers={'WWW-Authenticate': 'Bearer'})
    token = verify_access_token(token, credentials_exception)

    jwt_user = db.query(models.User).filter(models.User.id == token.id).first()

    return jwt_user
