# Expense Tracker API
A simple RESTful API built with Python and Flask to track and manage expenses.

**Live Demo**: [TBD](TBD)

## Features
- Add, update, delete, view expenses
- Data persistence via PostgreSQL (TBD)
- Tested using Thunder Client
- Authentication (TBD)

## Tech Stack
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [PostgreSQL](https://www.postgresql.org/) (TBD)
- [Thunder Client](https://www.thunderclient.com/) (for testing)

## Getting Started
**Clone the repository**
```bash
git clone https://github.com/izzetp/expense-tracker-api.git
cd expense-tracker-api
```

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Create the database**
```bash
# TBD (init script / migrations)
```

**Run the app**
```bash
python app.py
```

## API Endpoints

| Method | Route            | Description          |
|--------|------------------|----------------------|
| GET    | `/expenses`      | Get all expenses     |
| POST   | `/expenses`      | Add a new expense    |
| PUT    | `/expenses/{id}` | Update expense by ID |
| DELETE | `/expenses/{id}` | Delete expense by ID |

## Example: Add an Expense

**POST** `/expenses`
```json
{
  "category": "Food",
  "amount": 25.50,
  "date": "2025-12-10",
  "description": "Lunch"
}
```

## Testing
You can test the endpoints using:
- [Thunder Client](https://www.thunderclient.com/)
- [Postman](https://www.postman.com/) or curl
