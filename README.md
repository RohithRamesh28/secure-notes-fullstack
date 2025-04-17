# Secure Notes – Backend 🛡️

> Please install the following packages after creating your virtual environment:

```bash
pip install email-validator
pip install psycopg[binary]
```

---

## 📁 Frontend Repository

This repository contains the **backend** for the project. The **frontend** can be found here:  
🔗 [todo-application](https://github.com/RohithRamesh28/todo-application)

---

## ⚙️ How to Run This FastAPI Backend

### 🧭 Step 1: Clone and Enter the Project Folder

```bash
git clone https://github.com/RohithRamesh28/secure-notes-fullstack.git
cd secure-notes-fullstack
```

---

### 🐍 Step 2: Create and Activate a Virtual Environment

```bash
python -m venv your_env_name
your_env_name\Scripts\activate.bat
```

(If activation doesn’t work, ensure Python is added to your system's PATH.)

---

### 📦 Step 3: Install the Required Packages

Install FastAPI, Uvicorn, and other dependencies:

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install -r requirements.txt
```

> 💡 If you're using **VS Code**, install any recommended extensions when prompted.

---

### ▶️ Step 4: Run the Server

```bash
uvicorn app.main:app --reload --port 8080
```

> (Change the port if `8080` is already in use.)

---

## 🛠 Database Options

### 🐘 Option 1: Use PostgreSQL (Recommended)

1. Make sure **PostgreSQL** is installed.
2. Create a database (e.g., `secure_notes_app`).
3. Update your database URL in:

**`app/database.py`:**
```python
DATABASE_URL = "postgresql://yourusername:yourpassword@localhost:5432/your_db_name"
```

**`alembic.ini`:**
```
sqlalchemy.url = postgresql://yourusername:yourpassword@localhost:5432/your_db_name
```

4. Run migrations:
```bash
alembic upgrade head
```

You’ll now see two tables (`users` and `notes`) created in your PostgreSQL database.

---

### 🍃 Option 2: Use SQLite (Easier Setup)

1. Update the database URL in:

**`app/database.py`:**
```python
DATABASE_URL = "sqlite:///./notes.db"
```

**`alembic.ini`:**
```
sqlalchemy.url = sqlite:///./notes.db
```

2. Run migrations:
```bash
alembic upgrade head
```

This will create a `notes.db` file and handle table creation automatically.

---

## ✅ You're All Set!

Choose your preferred database, follow the steps above, and your backend should be up and running smoothly 🚀.

---

### 🛠 Need Help?

If you face any issues, recheck the steps or feel free to reach out via [GitHub Issues](https://github.com/RohithRamesh28/secure-notes-fullstack/issues) 😄
