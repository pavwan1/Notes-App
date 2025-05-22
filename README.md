# Notes App 📝

A simple and sleek Notes App built using React (frontend) and Flask with SQLAlchemy (backend). This app helps you create, update, delete, and manage your notes securely with user authentication.

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

---

## 📦 Backend Setup (Flask)

### 🔧 Prerequisites

- Python 3.9+
- pip
- Virtual Environment (recommended)

### 🔌 Installation

```bash
# Navigate to the backend directory
cd flask_backend

# Create virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up the database
python setup_db.py

# Run the Flask app
flask run
```

The Flask backend will run by default on:  
📍 `http://localhost:5000`

---

## 🎨 Frontend Setup (React)

### 🔧 Prerequisites

- Node.js
- npm

### ⚙️ Installation

```bash
# Navigate to the frontend directory
cd react_frontend

# Install dependencies
npm install
```

### 🚦 Start the App

```bash
npm start
```

🌐 Open `http://localhost:3000` to view the app in your browser.  
The app will reload automatically as you make changes.

---

## 🛠️ Build for Production

To create an optimized production build:

```bash
npm run build
```

📁 The build artifacts will be stored in the `build/` directory, ready to be deployed.

---

## 🚀 Deployment

Refer to the official Create React App docs for deployment:  
🔗 [CRA Deployment Guide](https://facebook.github.io/create-react-app/docs/deployment)

---

## 🧠 Learn More

- [React Docs](https://reactjs.org/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [Create React App Docs](https://facebook.github.io/create-react-app/docs/getting-started)

---

Made with ❤️ by **Pavan Kumar Reddy**
