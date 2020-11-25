import mariadb
import sys

def get_db_cursor():
    try:
        conn = mariadb.connect(
            user="ifkarsyah",
            password="password",
            host="localhost",
            port=3306,
            database="employees"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    
    return conn.cursor()