#!/usr/bin/env python3
"""
Extract lyrics from MP3 files using metadata or speech-to-text
"""

import os
import json
from pathlib import Path
from mutagen.easyid3 import EasyID3

def extract_lyrics_from_metadata(mp3_file):
    """
    Extract lyrics from MP3 metadata tags
    """
    try:
        audio = EasyID3(mp3_file)
        lyrics = audio.get('lyrics', [''])[0]
        if lyrics:
            return lyrics
        # Try comment field if no lyrics
        return audio.get('comment', [''])[0]
    except Exception as e:
        print(f"Error reading {mp3_file}: {e}")
        return None

def process_all_mp3s(mp3_dir='mp3_files', output_dir='lyrics'):
    """
    Process all MP3 files and extract lyrics
    """
    Path(output_dir).mkdir(exist_ok=True)
    results = {}
    
    for mp3_file in Path(mp3_dir).glob('*.mp3'):
        print(f"Processing: {mp3_file.name}")
        lyrics = extract_lyrics_from_metadata(mp3_file)
        
        if lyrics:
            # Save lyrics to text file
            output_file = Path(output_dir) / f"{mp3_file.stem}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(lyrics)
            results[mp3_file.name] = 'Success'
            print(f"✓ Saved lyrics to {output_file}")
        else:
            results[mp3_file.name] = 'No lyrics found'
    
    return results

if __name__ == "__main__":
    results = process_all_mp3s()
    print(f"\nProcessed {len(results)} files")
    print(json.dumps(results, indent=2))
