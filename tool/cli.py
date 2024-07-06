import os

import sqlite3

import typer
import json

app = typer.Typer()

def insertJson(path: str, cursor: sqlite3.Cursor):
    jsonData = json.load(open(path, 'r'))

    table: str = list(jsonData.keys())[0]

    for entry in jsonData[table]:
        columns = ', '.join(entry.keys())
        placeholders = ':'+', :'.join(entry.keys())
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'

        print(entry)
        cursor.execute(query, entry)
    
@app.command()
def build():
    con = sqlite3.connect(f"{os.path.dirname(__file__)}/../data/db.sqlite")

    file = open(f"{os.path.dirname(__file__)}/../sql/create.sql", 'r')
    cur = con.cursor()


    cur.executescript(file.read())

    insertJson("data/media.json", cur)
    insertJson("data/concerns.json", cur)
    insertJson("data/names.json", cur)
    insertJson("data/coverage.json", cur)

    con.commit()



if __name__ == "__main__":
    app()
