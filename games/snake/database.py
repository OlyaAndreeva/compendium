from sqlite3 import connect
from pathlib import Path

path = str(Path(__file__).parent) + "\snake.db"


def db_init():
    with connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS results(
        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL
        )
        """)

        cursor.execute("""
        SELECT * FROM results
        """)
        rows = len(cursor.fetchall())  

        while rows < 3:
            cursor.execute("""
            INSERT INTO results(name, score) VALUES ("player", 0)
            """)
            rows = rows + 1

def db_check_insert(score):
    leaders = db_get_leaders()
    if score > leaders[2][2]:
        return True
    else:
        return False


def db_get_leaders():
    with connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM results
        ORDER BY score DESC 
        LIMIT 3
        """)
        return cursor.fetchall()
    
def db_insert(name, score):
    with connect(path) as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
        INSERT INTO results(name, score) VALUES ("{name}", {score})
        """)

# i'm so sad :(
