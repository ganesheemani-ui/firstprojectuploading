#  Django REST API - Player Management System

A RESTful API built using Django and Django REST Framework to manage player data efficiently.  
This project demonstrates CRUD operations, API design, and backend development best practices.

---

##  Features

- Create, Read, Update, Delete (CRUD) player records
- RESTful API endpoints using Django REST Framework
- Data validation using serializers
- Structured database management with SQLite
- Admin panel integration for easy data handling

---

## Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- SQLite
- Postman (for API testing)

---

## Project Structure
project/
│── project/ # Main project settings
│── team_players/ # App containing models, views, serializers
│── manage.py
│── db.sqlite3


---

## ⚙️ API Endpoints

| Method | Endpoint              | Description              |
|--------|---------------------|--------------------------|
| GET    | /players/           | Get all players          |
| GET    | /players/{id}/      | Get single player        |
| POST   | /players/           | Create new player        |
| PUT    | /players/{id}/      | Update player            |
| DELETE | /players/{id}/      | Delete player            |
