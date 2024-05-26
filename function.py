import mysql.connector
from fastapi import HTTPException

def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pashabd"
    )

def getdata():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM userinfo")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    formatted_data = []
    for row in results:
        data_item = {
            "id": row[0],
            "name": row[1],
            "username": row[2],
            "password": row[3]
        }
        formatted_data.append(data_item)
    return formatted_data



def insert_data_into_table(name, UserName, Password):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO `userinfo` (`name`, `UserName`, `Password`) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, UserName, Password,))
    connection.commit()  # Don't forget to commit changes
    connection.close()
    return True


def CheckUserNamme(UserName):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT  `UserName` FROM `userinfo` WHERE UserName = %s"
    cursor.execute(query, (UserName,))
    result = cursor.fetchone()
    connection.close()
    return result
    
    

   



def fetch_data_from_user_id(UserID):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT `UserID`, `name`, `UserName`, `Password` FROM `userinfo` WHERE UserID = %s"
    cursor.execute(query, (UserID,))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    formatted_data = []
    for row in results:
        data_item = {
            "id": row[0],
            "name": row[1],
            "username": row[2],
            "password": row[3]
         }
        formatted_data.append(data_item)
    return formatted_data



def login(UserName, Password):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT `UserID`, `name`, `UserName`, `Password` FROM `userinfo` WHERE UserName = %s AND Password = %s"
    cursor.execute(query, (UserName, Password))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    formatted_data = []
    for row in results:
        data_item = {
            "username": row[1],
            "password": row[3],
            "name": row[2],
            "UserID": row[0],
        }
        formatted_data.append(data_item)
    return formatted_data