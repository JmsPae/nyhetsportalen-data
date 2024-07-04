import duckdb

import typer

app = typer.Typer()

@app.command()
def build(datadir: str, dist: str):
    db = duckdb.read_json(f"{datadir}/*.json")

    db.write_parquet(f"{dist}/data.paraquet")

if __name__ == "__main__":
    app()
