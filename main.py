from fastapi import FastAPI
from app.routers import user, reservation

app = FastAPI()


# Mount CSRF-protected routes
app.include_router(user.router)
app.include_router(reservation.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
