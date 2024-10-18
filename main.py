from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my My API"}

@app.get("/posts")
def getPosts():
    return {"data" : "all the posts"}

@app.post("/createposts")
def createPosts(payLoad: dict = Body()):
    print(payLoad)
    return {"Succesfully create posts"}