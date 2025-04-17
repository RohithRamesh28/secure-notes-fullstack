from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

# Correct database URL for PostgreSQL
DATABASE_URL = "sqlite:///./notes.db"


engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
