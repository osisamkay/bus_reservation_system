from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.database import get_db
from app.schemas import User, UserCreate
from app.crud import user_crud
import jwt
from datetime import datetime, timedelta

router = APIRouter()

# JWT Secret Key
SECRET_KEY = "your_secret_key"
# Token expiration time
TOKEN_EXPIRE_MINUTES = 30

# Create a password context object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def verify_password(plain_password, hashed_password):
    """Verify the password by comparing plain text with hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Generate hash for the password."""
    return pwd_context.hash(password)


def create_access_token(data: dict):
    """
    Create JWT access token.

    Parameters:
        data (dict): User data to be encoded in the token.

    Returns:
        str: Encoded JWT access token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


@router.post("/login", response_class=JSONResponse)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Login endpoint to authenticate users and generate JWT token.

    Parameters:
        form_data (OAuth2PasswordRequestForm): Form data containing username and password.
        db (Session): Database session.

    Raises:
        HTTPException: If invalid credentials are provided.

    Returns:
        dict: Dictionary containing access token and token type.
    """
    try:
        # Passing db session to get_user_by_username
        user = user_crud.get_user_by_username(db, form_data.username)
        print(user)
        if not user or not verify_password(form_data.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Generate JWT token
        access_token = create_access_token(data={"sub": user.username})

        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/register", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.

    Parameters:
        user (UserCreate): User data to be registered.
        db (Session): Database session.

    Raises:
        HTTPException: If the email is already registered.

    Returns:
        User: Newly created user data.
    """
    try:
        db_user = user_crud.get_user_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(
                status_code=400, detail="Email already registered")
        return user_crud.create_user(db=db, user=user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
