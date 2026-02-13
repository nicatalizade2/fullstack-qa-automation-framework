from fastapi import FastAPI
from db_client import DBClient

app = FastAPI()
db = DBClient()

@app.get("/")
def home():
    return {"status": "API is Running!"}

@app.get("/users")
def get_users():
    # This will now use your DBClient to talk to Docker!
    return db.fetch("SELECT * FROM users;")
