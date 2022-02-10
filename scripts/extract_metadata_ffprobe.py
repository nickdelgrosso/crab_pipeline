
import json
import subprocess
import argparse
from typing import Dict

mov_filename = "/mnt/f/SWC/NINJAV_S001_S001_T003.MOV"

def get_video_metadata(mov_filename: str) -> Dict[str, str]:
    """Returns metadata dictionary from ffprobe's output from analyzing a movie filename."""

    # Run ffprobe to extract metadata, capture output to a string
    output = subprocess.run(['ffprobe', mov_filename], capture_output=True)

    # Find where metadata starts
    metadata_text = output.stderr[output.stderr.find(b"Metadata"):].decode()

    # Parse metadata text into a dictionary
    metadata = {}
    for line in metadata_text.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()

    return metadata


def main():

    parser = argparse.ArgumentParser(description="Exports ffprobe metadata from a video file to json.")
    parser.add_argument("vidfile", help='The video filename to analyze.')
    parser.add_argument('--camera', default='', help="Name of Camera")
    parser.add_argument('--session', default='', help="Name of Session")

    args = parser.parse_args()

    metadata = get_video_metadata(mov_filename=args.vidfile)
    if args.camera:
        metadata['camera'] = args.camera
    if args.session:
        metadata['session'] = args.session

    # Convert to JSON
    metadata_json = json.dumps(metadata, indent=2)

    # Print output
    print(metadata_json)


if __name__ == '__main__':
    main()