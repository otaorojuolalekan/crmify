from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'crmify_web'
password = 'Lelekumo@1'
host = 'localhost'
db = 'crmify'

# Encode the password
encoded_password = quote_plus(password)

# Construct the URL
SQLALCHEMY_DATABASE_URL = f'mysql://{user}:{encoded_password}@{host}/{db}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
