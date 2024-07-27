import mysql.connector

mydatabase = mysql.connector.connect(
     host="localhost",
    user="root",
    password="Indespicableme11#",
)
cursor = mydatabase.cursor()
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    mydatabase.commit()
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(e)

cursor.close()
mydatabase.close()

