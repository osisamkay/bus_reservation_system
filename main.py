from fastapi import FastAPI
from app.routers import user, reservation, bus, routes

app = FastAPI()


# Mount CSRF-protected routes
app.include_router(user.router)
app.include_router(reservation.router)
app.include_router(bus.router)
app.include_router(routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
