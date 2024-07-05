import os
import pyarrow as pa
from pyarrow import dataset, json as pajson

import typer

app = typer.Typer()

@app.command()
def build():
    table = pajson.read_json(f"{os.path.dirname(__file__)}/../data/media.json")

    ds = dataset.dataset(table)

    dataset.write_dataset(ds, f"{os.path.dirname(__file__)}/../dist", format="arrow", schema=ds.schema)

if __name__ == "__main__":
    app()
