from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Replace 'sqlite:///./app.db' with your database URI if needed
SQLALCHEMY_DATABASE_URI = 'sqlite:///./app.db'

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={
                       "check_same_thread": False})

# Create the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the database


def initialize_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully.")
