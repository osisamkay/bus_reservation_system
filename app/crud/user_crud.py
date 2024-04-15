from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models import User
from app.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_username(db: Session, username: str):
    """
    Retrieve a user by username from the database.

    Parameters:
        db (Session): Database session.
        username (str): Username of the user to retrieve.

    Returns:
        User: User object if found, None otherwise.
    """
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.

    Parameters:
        db (Session): Database session.
        user (UserCreate): User data for creation.

    Returns:
        User: Newly created user object.
    """
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email,
                   password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_password(plain_password, hashed_password):
    """
    Verify the password by comparing plain text with hashed password.

    Parameters:
        plain_password (str): Plain text password.
        hashed_password (str): Hashed password from the database.

    Returns:
        bool: True if password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db: Session, user_id: int):
    """
    Retrieve a user by user ID from the database.

    Parameters:
        db (Session): Database session.
        user_id (int): ID of the user to retrieve.

    Returns:
        User: User object if found, None otherwise.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user by email from the database.

    Parameters:
        db (Session): Database session.
        email (str): Email of the user to retrieve.

    Returns:
        User: User object if found, None otherwise.
    """
    return db.query(User).filter(User.email == email).first()
