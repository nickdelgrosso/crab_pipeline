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
    session: str
    camera: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    duration: Optional[timedelta]
    width: Optional[int]
    height: Optional[int]
    
    
def parse_metadata(fname: Path, camera: str = '', session: str = '') -> RawVideoMetaData:
    parser = createParser(str(fname))
    with parser:
        metadata = extractMetadata(parser).exportDictionary()['Metadata']
    
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
        start_date = datetime.fromisoformat(metadata['Creation date'])
    else:
        start_date = None

    end_date = start_date + duration if duration is not None and start_date is not None else None

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
        start_date = start_date,
        end_date = end_date,
        width=width,
        height=height,
        camera=camera,
        session=session,
    )


def main():    
    parser = argparse.ArgumentParser(description="Extracts Raw Video Data to JSON")
    parser.add_argument('fname', type=dir_path, help="Path to Video File")
    parser.add_argument('--camera', default='', help="Name of Camera")
    parser.add_argument('--session', default='', help="Name of Session")

    args = parser.parse_args()
    
    assert args.fname.exists()
    
    metadata = parse_metadata(
        fname=args.fname, 
        camera=args.camera, 
        session=args.session
    )
    print(metadata.json(indent=2))
    
    
def dir_path(path) -> Path:
    p = Path(path)
    if p.exists():
        return p
    else:
        raise argparse.ArgumentTypeError(f"{path} does not exist.")


if __name__ == '__main__':
    main()