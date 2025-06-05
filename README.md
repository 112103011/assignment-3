# Assignment 3: Django Message Board

This repository contains the code for **Assignment 3**, a simple web-based message board application built using the Django framework.

## Project Structure

```
assignment-3/
├── board/                # Application code (presumably the main app)
├── messageboard/         # Django project settings and configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3            # SQLite3 database file (default for Django)
├── manage.py             # Django project management script
├── venv/                 # Virtual environment (not tracked in Git)
```

## Features

- User-friendly message board interface (details depend on implementation in `board/`)
- Django-based backend
- Persistent storage using SQLite3

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- (Recommended) Virtualenv for isolated environment

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/112103011/assignment-3.git
   cd assignment-3
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser and go to** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Interact with the message board at the local server address.
- Add, view, and manage messages (functionality depends on your implementation in the `board` app).
