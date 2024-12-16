from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .. import constants
# Load MySQL credentials from .env or hardcode them for now
DATABASE_URL = f"mysql+mysqlconnector://{constants.DB_USERNAME}:{constants.DB_PASSWORD}@{constants.DB_HOST}:{constants.DB_HOST}/{constants.DB_DATABASE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
