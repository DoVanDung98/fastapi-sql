from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
from psycopg2.extras import RealDictCursor
import psycopg2
import time
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='1213', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was sucessfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1},
           {"title": "favorite foods", "content": "I like pizza", "id":2}]


def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/sqlalchemy")
def test_post(db: Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    print(posts)
    return {"data": "successfull"}




