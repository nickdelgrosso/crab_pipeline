import csv
from pathlib import Path
import json
from typing import List
import pandas as pd


def csv_from_json_filenames(filenames: List[str], output: str) -> None:
    texts = (Path(f).read_text() for f in filenames)
    data = [json.loads(text) for text in texts]
    df = pd.DataFrame(data)
    df.to_csv(output, index=False)


def main():
    csv_from_json_filenames(
        filenames=snakemake.input,
        output=snakemake.output[0],
    )
    

if __name__ == '__main__':
    main()
