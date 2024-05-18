from fastapi import FastAPI
from function import *

app = FastAPI()

@app.get("/get_message")
async def get_message():
    return {"message": "This is the first API"}

@app.get("/get_data")
async def get_data():
    data = getdata()
    if data:
            return {"message":data}
    else:
        return {"message": "Invalid data"}


@app.get("/get_dataByUserID/{UserID}")
async def get_data(UserID:int):
    data = fetch_data_from_user_id(UserID)
    if data:
            return {"message":data}
    else:
        return {"message": "Invalid data"}
    


@app.post("/postData")
async def post_data(data: dict):
    name = data.get("name")
    UserName = data.get("UserName")
    Password = data.get("Password")
    insert_data_into_table(name, UserName, Password)
    return {"message": "Data inserted successfully"}

@app.post("/login")
async def post_data(data: dict):
    UserName = data.get("UserName")
    Password = data.get("Password")
    message = login(UserName, Password)
    if message:
            return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}
    



