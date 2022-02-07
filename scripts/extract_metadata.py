import re
from pathlib import Path
from datetime import timedelta, datetime
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from pydantic import BaseModel


class RawVideoMetaData(BaseModel):
    """The output data model for the metadata."""
    path: Path
    duration: timedelta
    created_on: datetime
    width: int
    height: int
    
    
def parse_metadata(fname: Path) -> RawVideoMetaData:
    parser = createParser(str(fname))
    with parser:
        metadata = extractMetadata(parser).exportDictionary()['Metadata']
    metadata
    
    aa = re.search("(\d+) min (\d+) sec (\d+) ms", metadata['Duration'])
    minutes, secs, msecs = aa.groups()
    duration = timedelta(minutes=int(minutes), seconds=int(secs), milliseconds=int(msecs))

    created_on = datetime.fromisoformat('2024-06-18 06:13:24')

    width = re.match("(\d+) pixels", metadata['Image width']).groups()[0]
    width = int(width)

    height = re.match("(\d+) pixels", metadata['Image height']).groups()[0]
    height = int(height)
    
    return RawVideoMetaData(
        path=Path(fname),
        duration = duration,
        created_on = created_on,
        width=width,
        height=height
    )


def main():
    
    from argparse import ArgumentParser
    
    parser = ArgumentParser(description="Extracts Raw Video Data to JSON")
    parser.add_argument('fname', type=Path, help="Path to Video File")
    args = parser.parse_args()
    
    assert args.fname.exists()
    
    metadata = parse_metadata(fname=args.fname)
    print(metadata.json())
    
    
if __name__ == '__main__':
    main()