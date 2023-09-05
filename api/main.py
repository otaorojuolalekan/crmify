from fastapi import FastAPI
from . import models
from .database import engine
from .routers import account, case, update, user, auth
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

print(settings.model_config)
print(settings.database_name)
app.include_router(account.router)
app.include_router(case.router)
app.include_router(update.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def index():
    return {'message': 'Welcome to CRMIFY API homepage!'}


"""
**********************************************
        Accounts API methods Section
**********************************************
"""


"""
**********************************************
        Cases API methods Section
**********************************************
"""


"""
**********************************************
        Users API methods Section
**********************************************
"""


"""
**********************************************
        Updates API methods Section
**********************************************
"""
