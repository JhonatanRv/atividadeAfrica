import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="3.221.155.173",
    user="admin",
    password="senha123",
    database="AFRICA"
  )
  return mydb