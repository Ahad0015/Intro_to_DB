# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (replace with your credentials if needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # replace with your MySQL root password if set
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Ensure cleanup
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
