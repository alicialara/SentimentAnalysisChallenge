import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    """
    Establish a connection to the MySQL database using environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: The database connection object.
    """
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def close_db_connection(conn):
    """
    Close the given database connection.

    Args:
        conn (mysql.connector.connection.MySQLConnection): The database connection object to close.
    """
    if conn.is_connected():
        conn.close()