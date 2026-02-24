#!/usr/bin/env python3
"""
Main automation script - Orchestrates the full workflow
"""

import os
from dotenv import load_dotenv
from extract_lyrics import process_all_mp3s
from prompt_generator import generate_prompts
import automation_setup

def main():
    """
    Main orchestration function
    """
    # Load environment variables
    load_dotenv()
    
    print("=== Suno to Whisk Automation ===")
    print()
    
    # Step 1: Setup (create directories if needed)
    print("[1/3] Setting up environment...")
    automation_setup.setup_environment()
    print()
    
    # Step 2: Extract lyrics from MP3s
    print("[2/3] Extracting lyrics from MP3 files...")
    lyrics_results = process_all_mp3s()
    successful_lyrics = sum(1 for r in lyrics_results.values() if r == 'Success')
    print(f"Successfully extracted {successful_lyrics}/{len(lyrics_results)} files")
    print()
    
    # Step 3: Generate prompts for Whisk
    print("[3/3] Generating Whisk prompts...")
    prompts_results = generate_prompts()
    print(f"Generated {len(prompts_results)} prompts")
    print()
    
    print("=== Automation Complete ===")
    print("Next steps:")
    print("1. Review generated prompts in ./prompts/")
    print("2. Upload to Whisk AI for image/video generation")
    print("3. Combine with MP3 files for final video")

if __name__ == "__main__":
    main()
