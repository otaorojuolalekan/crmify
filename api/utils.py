from fastapi import HTTPException, status
from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(plain_pwd):
    return password_context.hash(plain_pwd)

def verify(plain_pwd, hashed_pwd):
    return password_context.verify(plain_pwd, hashed_pwd)

def raiseAccount404(id):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Account with {id} doesn't exist")

def raiseUpdate404(id):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Update with {id} doesn't exist")

def raiseCase404(id):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Case with {id} doesn't exist")

def raiseUser404(id):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with {id} doesn't exist")

def raiseInvalidCredException():
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Invalid Credentials")