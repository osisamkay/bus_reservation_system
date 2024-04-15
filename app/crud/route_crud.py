from sqlalchemy.orm import Session
from app.models import Route
from app.schemas import RouteCreate, Route as RouteModel
from typing import List
from fastapi import HTTPException


def create_route(db: Session, route_data: RouteCreate) -> Route:
    """
    Create a new route in the database if it doesn't already exist.

    Parameters:
        db (Session): Database session.
        route_data (RouteCreate): Route data for creation.

    Returns:
        Route: Newly created route object.
    """
    existing_route = db.query(Route).filter(
        Route.source == route_data.source,
        Route.destination == route_data.destination
    ).first()

    if existing_route:
        raise HTTPException(status_code=400, detail="Route already exists")

    new_route = Route(**route_data.dict())
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route


def get_all_routes(db: Session):
    """
    Get all routes from the database.

    Parameters:
        db (Session): Database session.

    Returns:
        List[RouteModel]: List of all available routes as Pydantic objects.
    """
    try:
        all_routes = db.query(Route).all()
        return [RouteModel(
            id=str(route.id),
            source=route.source,
            destination=route.destination
        ) for route in all_routes]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_route_by_id(id, db: Session):
    """
    Get all routes from the database.

    Parameters:
        db (Session): Database session.

    Returns:
        List[RouteModel]: List of all available routes as Pydantic objects.
    """
    try:
        all_routes = db.query(Route).filter_by(id=id).first()
        return all_routes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def update_route_by_id(route_id: str, updated_data: dict, db: Session):
    """
    Update an existing Route by its ID.

    Parameters:
        route_id (str): ID of the route to update.
        updated_data (dict): Dictionary containing updated route data.
        db (Session): Database session.

    Returns:
        Route: Updated route object.
    """
    # Retrieve the route from the database based on the provided ID
    route = db.query(Route).filter(Route.id == route_id).first()

    if not route:
        return None  # Route with the given ID doesn't exist

    # Update the route object with the provided data
    for key, value in updated_data.items():
        setattr(route, key, value)

    # Commit the changes to the database
    db.commit()

    # Refresh the route object to reflect the updated data
    db.refresh(route)

    return route  # Return the updated route object
