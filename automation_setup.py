#!/usr/bin/env python3
"""
Automation Setup - Install dependencies and configure environment
"""

import os
import subprocess
import sys
from pathlib import Path

def setup_environment():
    """
    Set up the automation environment
    """
    print("Setting up Suno Automation environment...")
    
    # Create necessary directories
    dirs = ['mp3_files', 'lyrics', 'prompts', 'output']
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✓ Created directory: {dir_name}")
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("# Whisk API Key\n")
            f.write("WHISK_API_KEY=your_api_key_here\n")
            f.write("\n# Suno Configuration\n")
            f.write("SUNO_SESSION_ID=your_session_id_here\n")
        print("✓ Created .env file")
    
    print("\nSetup complete! Now you can:")
    print("1. Update .env with your API keys")
    print("2. Place MP3 files in mp3_files/ directory")
    print("3. Run: python main.py")

if __name__ == "__main__":
    setup_environment()
