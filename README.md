# Bus Reservation System

This is a simple Bus Reservation System developed using FastAPI, SQLAlchemy, and SQLite. It allows users to register, login, make reservations, and manage buses and routes.

## Features

- User Authentication: Register, login, and manage user accounts.
- Bus Management: Add, update, and delete buses along with their routes and capacities.
- Reservation System: Allow users to make and cancel reservations for specific buses and routes.
- JWT Authentication: Secure user authentication using JWT tokens.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/osisamkay/bus-reservation-system.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd bus-reservation-system
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**

   ```bash
   python initialize_db.py
   ```

5. **Run the FastAPI server**

   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API documentation**

   Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the Swagger UI with API endpoints and test them.

## Project Structure

- `app/`: Contains the main application files.
  - `models.py`: SQLAlchemy models for database tables.
  - `routers/`: Contains API route handlers.
  - `schemas/`: Pydantic schemas for request and response validation.
- `alembic/`: Database migration scripts managed by Alembic.
- `tests/`: Unit tests for the application.
- `initialize_db.py`: Script to initialize the SQLite database.
- `main.py`: Entry point for the FastAPI application.
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/): Fast web framework for building APIs.
- [SQLAlchemy](https://www.sqlalchemy.org/): SQL toolkit and Object-Relational Mapping (ORM) library.
- [SQLite](https://www.sqlite.org/): Lightweight database engine.
- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and settings management using Python type annotations.
- [JWT](https://jwt.io/): JSON Web Tokens for user authentication.
- [Alembic](https://alembic.sqlalchemy.org/en/latest/): Database migration tool for SQLAlchemy.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
