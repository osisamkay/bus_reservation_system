from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import RouteCreate, Route, RouteUpdate
from sqlalchemy.orm import Session
from app.crud import route_crud
from app.database import get_db
from fastapi.responses import JSONResponse
router = APIRouter()


@router.get('/route', response_model=List[Route])
def get_all_routes(db: Session = Depends(get_db)):
    """
    Gets All Routes

    Returns:
        Route: All route data.
    """
    try:
        all_routes = route_crud.get_all_routes(db)
        return all_routes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/route/{route_id}/", response_model=List[Route])
def get_route_by_id(route_id: str, db: Session = Depends(get_db)):
    """
    Get an existing Route by ID.

    Parameters:
        route_id (str): ID of the route to retrieve.

    Raises:
        HTTPException: If the route with the given ID doesn't exist.

    Returns:
        RouteModel: Route data for the specified route ID.
    """
    try:
        route = route_crud.get_route_by_id(route_id, db)
        if not route:
            raise HTTPException(status_code=404, detail="Route not found")
        return [route]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/route/add/", response_model=Route)
def add_route(route_data: RouteCreate, db: Session = Depends(get_db)):
    """
    Add a new route.

    Parameters:
        route_data (RouteCreate): Route data.
        db (Session): Database session.

    Returns:
        Route: Newly added route data.
    """
    try:
        # Create a new route in the database
        new_route = route_crud.create_route(db, route_data)
        return new_route
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/route/update/{route_id}/", response_model=List[Route])
def update_route(route_id: str, route_data: RouteUpdate, db: Session = Depends(get_db)):
    """
    Update an existing Route.

    Parameters:
        route_id (str): ID of the route to update.
        route_data (RouteModel): Updated route data.
        db (Session): Database session.

    Raises:
        HTTPException: If the route with the given ID doesn't exist.

    Returns:
        RouteModel: Updated route data.
    """
    try:
        updated_route = route_crud.update_route_by_id(
            route_id, route_data.dump(), db)
        if not updated_route:
            raise HTTPException(status_code=404, detail="Route not found")
        return updated_route
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/route/delete/{route_id}/")
def delete_bus(route_id: int):
    """
    Delete an existing route.

    Parameters:
        route_id (int): ID of the route to delete.

    Raises:
        HTTPException: If the route with the given ID doesn't exist.

    Returns:
        dict: Response message.
    """
    # Implement delete route logic here
    # For example, delete the route from the database by its ID
    # If the route doesn't exist, raise an HTTPException with status code 404
    # Otherwise, return a response message indicating successful deletion
    return {"message": f"Route with ID {route_id} deleted successfully"}
