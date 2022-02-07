import re
import argparse
from typing import Optional
from pathlib import Path
from datetime import timedelta, datetime
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from pydantic import BaseModel

class RawVideoMetaData(BaseModel):
    """The output data model for the metadata."""
    directory: Path
    filename: Path
    duration: Optional[timedelta]
    created_on: Optional[datetime]
    width: Optional[int]
    height: Optional[int]
    
    
def parse_metadata(fname: Path) -> RawVideoMetaData:
    parser = createParser(str(fname))
    with parser:
        metadata = extractMetadata(parser).exportDictionary()['Metadata']
    metadata
    
    if 'Duration' in metadata:
        dur = metadata['Duration']
        hours = int(match.groups()[0]) if (match := re.search("(\d+) hours", dur)) else 0
        minutes = int(match.groups()[0]) if (match := re.search("(\d+) min", dur)) else 0
        secs = int(match.groups()[0]) if (match := re.search("(\d+) sec", dur)) else 0
        msecs = int(match.groups()[0]) if (match := re.search("(\d+) ms", dur)) else 0
        duration = timedelta(hours=hours, minutes=minutes, seconds=secs, milliseconds=msecs)
    else:
        duration = None

    if 'Creation date' in metadata:
        created_on = datetime.fromisoformat(metadata['Creation date'])
    else:
        created_on = None

    if 'Image width' in metadata:
        width = re.match("(\d+) pixels", metadata['Image width']).groups()[0]
        width = int(width)
    else:
        width = None

    if 'Image height' in metadata:
        height = re.match("(\d+) pixels", metadata['Image height']).groups()[0]
        height = int(height)
    else:
        height = None
    
    return RawVideoMetaData(
        directory=Path(fname).parent,
        filename=Path(fname).name,
        duration = duration,
        created_on = created_on,
        width=width,
        height=height
    )


def main():    
    parser = argparse.ArgumentParser(description="Extracts Raw Video Data to JSON")
    parser.add_argument('fname', type=dir_path, help="Path to Video File")
    args = parser.parse_args()
    
    assert args.fname.exists()
    
    metadata = parse_metadata(fname=args.fname)
    print(metadata.json(indent=2))
    
    
def dir_path(path) -> Path:
    p = Path(path)
    if p.exists():
        return p
    else:
        raise argparse.ArgumentTypeError(f"{path} does not exist.")


if __name__ == '__main__':
    main()