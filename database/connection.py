import sqlite3
import psycopg2
import mysql.connector
import pyodbc 

def get_connection(db_type, host, db_name, user, password):
    if db_type == "SQLite":
        return sqlite3.connect(db_name if db_name else ":memory:")
    elif db_type == "PostgreSQL":
        return psycopg2.connect(host=host, database=db_name, user=user, password=password)
    elif db_type == "MySQL":
        return mysql.connector.connect(host=host, database=db_name, user=user, password=password)
    elif db_type == "SQL Server":
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host};DATABASE={db_name};UID={user};PWD={password}'
        return pyodbc.connect(conn_str)
