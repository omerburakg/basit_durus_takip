import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Serel.2026",
        database="maintenance_db"
    )
