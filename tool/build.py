import os
import sqlite3
import json

combi = {}

def insertJson(path: str, cursor: sqlite3.Cursor):
    jsonData = json.load(open(path, 'r'))

    table: str = list(jsonData.keys())[0]

    combi[table] = jsonData[table] 

    for entry in jsonData[table]:
        columns = ', '.join(entry.keys())
        placeholders = ':'+', :'.join(entry.keys())
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'

        try:
            cursor.execute(query, entry)
        except sqlite3.Error as sqliteError:
            print("Error inserting Json:")
            print(entry)
            print("SQLite Error:", sqliteError)
            exit(100)

if __name__ == "__main__":
    output = f"{os.path.dirname(__file__)}/../processed/db.sqlite"
    jsonCombiOutput = f"{os.path.dirname(__file__)}/../processed/combi.json"

    tmpFile = f"{os.path.dirname(__file__)}/tmp.sqlite"

    try:
        os.mkdir(f"{os.path.dirname(__file__)}/../processed")
    except:
        print("Output folder exists, skipping")


    try:
        os.remove(tmpFile)
    except:
        print("tmp.sqlite doesn't exist, skip deletion")

    con = sqlite3.connect(tmpFile)

    file = open(f"{os.path.dirname(__file__)}/../sql/create.sql", 'r')
    cur = con.cursor()


    cur.executescript(file.read())

    # In order of dependencies
    insertJson("data/concerns.json", cur)
    insertJson("data/media.json", cur)
    insertJson("data/names.json", cur)
    insertJson("data/coverage.json", cur)

    cur.execute("PRAGMA optimize");

    con.commit()
    con.close()
    print("Done!")

    try:
        os.remove(output)
    except:
        print("Output doesn't exist, skip deletion")

    os.replace(tmpFile, output)

    with open(jsonCombiOutput, 'w') as f:
        json.dump(combi, f)
