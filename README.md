# Lunch Decision System

This is a Django-based REST API for an employee lunch decision system.

## Setup

1. Install Docker and Docker Compose.
2. Clone this repository.
3. Run `docker-compose up --build` to build and start the containers.
4. The API will be available at `http://localhost:8000`.

## API Endpoints

- `/api/auth/register/`: Register a new user
- `/api/auth/token/`: Obtain JWT token
- `/api/auth/token/refresh/`: Refresh JWT token
- `/api/restaurants/create/`: Create a new restaurant
- `/api/restaurants/upload_menu/`: Upload a menu for a restaurant
- `/api/restaurants/current_day_menu/`: Get the current day's menu
- `/api/employees/create/`: Create a new employee
- `/api/employees/vote/`: Vote for a menu
- `/api/employees/results/`: Get voting results for the current day

## Running Tests

To run the tests, execute the following command: