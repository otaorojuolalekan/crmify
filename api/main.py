from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import models
from api.database import engine
from api.routers import account, case, update, user, auth
from api.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:5000",  # Add the origin of your client application here
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:33323"
    # Add other allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["*"],  # You can specify specific headers if needed
)

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
