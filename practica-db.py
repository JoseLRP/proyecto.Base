import sqlite3
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH+ '/mydatabase.db'

con = sqlite3.connect(DB_PATH)
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE REGISTRO(

        ID INT PRIMARE KEY NOT NULL,
        nombre TEXT NOT NULL,
        edad INT NOT NULL,
        correo TEXT NOT NULL,
        fecha INT NOT NULL
            )


        """)