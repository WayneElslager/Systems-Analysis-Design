# Panther Hotel – Room Reservation System

A prototypical hotel reservation website built with **Python**, **Flask**, **SQLite**, and **Bootstrap 5** for CIST 1310 Systems Analysis and Design (Spring 2026).

---

## Features

| Feature | Description |
|---|---|
| Welcome Page | Landing page with links to book a room or open the manager view |
| Reservation Page | Form to submit a guest reservation (name, check-in/out dates, room type) |
| Confirmation Page | Displays a booking summary after successful submission |
| Manager Dashboard | Lists all reservations with the ability to delete individual records |

---

## Project Structure

```
panther_hotel/
├── app.py                  # Flask application & routes
├── requirements.txt        # Python dependencies
├── .gitignore
├── instance/
│   └── hotel.db            # SQLite database (auto-created on first run)
├── static/
│   └── css/
│       └── style.css       # Custom stylesheet
└── templates/
    ├── base.html           # Shared layout (navbar, footer)
    ├── index.html          # Welcome page
    ├── reservation.html    # Reservation form
    ├── confirmation.html   # Booking confirmation
    └── manager.html        # Manager / reservation list
```

---

## Setup & Running

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd panther_hotel
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

Open your browser and navigate to **http://127.0.0.1:5000**

---

## Database

The SQLite database (`instance/hotel.db`) is created automatically on first run. It contains a single `reservations` table:

| Column | Type | Description |
|---|---|---|
| id | INTEGER PK | Auto-incremented primary key |
| name | TEXT | Guest full name |
| checkin | TEXT | Check-in date (YYYY-MM-DD) |
| checkout | TEXT | Check-out date (YYYY-MM-DD) |
| room_type | TEXT | Standard Room / Deluxe Room / Suite |
| created_at | TIMESTAMP | Booking timestamp |

---

## Technologies Used

- **Python 3** – server-side logic
- **Flask** – web framework
- **SQLite** – lightweight relational database
- **Jinja2** – HTML templating (included with Flask)
- **Bootstrap 5** – responsive front-end framework
- **Bootstrap Icons** – icon library
