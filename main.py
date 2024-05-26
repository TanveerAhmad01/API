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




@app.post("/signUp")
async def post_data(data: dict):
    name = data.get("name")
    UserName = data.get("UserName")
    Password = data.get("Password")
    getUser = CheckUserNamme(UserName)
    if  getUser:
        return {"message":"User Alreay Exist"}
    else: 
        get_message = insert_data_into_table(name, UserName, Password)
        if get_message:
            return {"message": "Data inserted successfully"}
        else:
            return {"message": "Data not inserted successfully"}




@app.post("/login")
async def post_data(data: dict):
    UserName = data.get("UserName")
    Password = data.get("Password")
    formatted_data = login(UserName, Password)
    if formatted_data:
         return {"Login_SuccessFully": formatted_data}
            
            
    else:
        return {"Login_SuccessFully": "Invalid username or password"}
    



