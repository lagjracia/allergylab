import mysql.connector
import os
db_name = os.environ['DB_NAME']
dbUser = os.environ['DB_USER']
dbPass = os.environ['DB_PASS']

def connection():
    # Edited out actual values
    conn = mysql.connector.connect( host='dbhost',
                            port=3306,
                            database=db_name,
                            user=dbUser,
                            password=dbPass)
    c = conn.cursor()

    return c, conn