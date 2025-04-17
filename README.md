# secure-notes-fullstack
please install this packages after creation of env
pip install email-validator
pip install psycopg[binary]
Hi,
This is the back-end of the repo (which holds the frontend of the project)named:[todo-application](https://github.com/RohithRamesh28/todo-application) 
After clonning and installing all the required packages and intructions done below, Please clone this repo mentioned above.

⚙️ How to Run This FastAPI Backend
Step 1: Clone and Enter the Project Folder
First things first — clone this backend repo:

git clone https://github.com/your-username/secure-notes-backend.git

cd secure-notes-backend

Step 2: Install a Virtual Environment

Open your terminal (cmd or PowerShell) and go to the folder where this repo was cloned.

python -m venv your_env_name
Once done, you can type dir and see your environment folder is created.

Now to activate it:

your_env_name\Scripts\activate.bat
(If this doesn't work, try doing the steps again or make sure Python is added to PATH.)

Step 3: Install the Required Packages
Once your environment is activated:

pip install fastapi
pip install "uvicorn[standard]"
Also, you'll find a requirements.txt file in the repo — that holds all the dependencies needed to run this project. So just install everything with:

pip install -r requirements.txt

If you're using VSCode (which I highly recommend since this project was built using it), install any extensions or packages it suggests when you run the server.

Step 4: Run the Server
Now you're all set! Run the server with:

uvicorn app.main:app --reload --port 8080
(Change the port if 8080 doesn't work for you.)

🛠 This Project Uses PostgreSQL by Default (but SQLite is Ready Too)
The backend is built with PostgreSQL — it's smooth, fast, and with Alembic, setting up migrations feels like sliding down a waterfall 😌.

🐘 If You Want to Use PostgreSQL:
Make sure PostgreSQL is installed.

Create a database (e.g., secure_notes_app or whatever name you like).

Go to app/database.py and update the DB URL:


DATABASE_URL = "postgresql://yourusername:yourpassword@localhost:5432/your_db_name"
Then, go to alembic.ini and do the same:

sqlalchemy.url = postgresql://yourusername:yourpassword@localhost:5432/your_db_name
Once done, run:


alembic upgrade head
And boom — you'll have two tables (users and notes) created in your PostgreSQL database.

🍃 If You Want to Use SQLite (Much Easier!)
If you don't have PostgreSQL — no worries, I got you 💪.

In app/database.py, change the DB URL to:


DATABASE_URL = "sqlite:///./notes.db"
And in alembic.ini, update:

sqlalchemy.url = sqlite:///./notes.db
Now just run:

alembic upgrade head
This will auto-create a notes.db file and handle all migrations like table creation etc. You're good to go!

That's it! Pick whatever DB option works for you and you'll have the backend up and running 🚀.

If you face any issues, just recheck the steps or hit me up on GitHub 😄
