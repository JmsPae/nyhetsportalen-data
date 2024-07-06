import os
import sqlite3
import json

def insertJson(path: str, cursor: sqlite3.Cursor):
    jsonData = json.load(open(path, 'r'))

    table: str = list(jsonData.keys())[0]

    for entry in jsonData[table]:
        columns = ', '.join(entry.keys())
        placeholders = ':'+', :'.join(entry.keys())
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'

        print(entry)
        cursor.execute(query, entry)

if __name__ == "__main__":
    output = f"{os.path.dirname(__file__)}/../processed/db.sqlite"

    try:
        os.mkdir(f"{os.path.dirname(__file__)}/../processed")
    except:
        print("Output folder exists, skipping")

    try:
        os.remove(output)
    except:
        print("Output doesn't exist, skip deletion")

    con = sqlite3.connect(output)

    file = open(f"{os.path.dirname(__file__)}/../sql/create.sql", 'r')
    cur = con.cursor()


    cur.executescript(file.read())

    insertJson("data/media.json", cur)
    insertJson("data/concerns.json", cur)
    insertJson("data/names.json", cur)
    insertJson("data/coverage.json", cur)

    con.commit()
