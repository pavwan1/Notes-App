# Notes App 📝

A simple Notes App built using **Flask**, **Jinja templates**, and **SQLAlchemy**. Users can register, log in, and manage their personal notes securely.

---

## 🚀 Getting Started

These instructions will help you set up and run the project on your local machine.

---

## 🔧 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Virtual Environment (recommended)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_GITHUB_USERNAME/notes-app.git

# Navigate to the project directory
cd notes-app

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

---

## 🛠️ Database Setup

```bash
# Run the database setup script (if any)
python setup_db.py
```

Or if you're using Flask-Migrate:

```bash
flask db init
flask db migrate
flask db upgrade
```

---

## 🚦 Running the App

```bash
# Set the Flask environment variables
export FLASK_APP=app
export FLASK_ENV=development  # Optional: for debug mode

# On Windows (use set instead of export)
set FLASK_APP=app
set FLASK_ENV=development

# Run the Flask server
flask run
```

🔗 Open your browser and visit:  
**http://localhost:5000**

---

## 💡 Features

- User registration and login (authentication)
- Secure password hashing
- Add, edit, and delete notes
- Notes linked to specific users
- Responsive UI with Jinja templates

---

## 📚 Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Jinja2 Docs](https://jinja.palletsprojects.com/)

---

Made with ❤️ by **Pavan Kumar Reddy**
