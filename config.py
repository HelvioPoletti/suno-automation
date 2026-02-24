import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent

# User-specific Suno downloads directory
SUNO_DOWNLOADS_DIR = r"C:\Users\abstt\OneDrive\Documentos\SUNO\Suno Downloads"

# Output directories
EXTRACTED_LYRICS_DIR = os.path.join(SUNO_DOWNLOADS_DIR, "extracted_lyrics")
GENERATED_PROMPTS_DIR = os.path.join(SUNO_DOWNLOADS_DIR, "generated_prompts")
PROCESSED_VIDEOS_DIR = os.path.join(SUNO_DOWNLOADS_DIR, "processed_videos")

# API Configuration
WHISK_API_KEY = os.getenv('WHISK_API_KEY', '')
WHISK_BASE_URL = os.getenv('WHISK_BASE_URL', 'https://whisk.ai/api')

# Processing configuration
BATCH_SIZE = int(os.getenv('BATCH_SIZE', '5'))
MAX_WORKERS = int(os.getenv('MAX_WORKERS', '4'))
TIMEOUT = int(os.getenv('TIMEOUT', '300'))

# Logging configuration
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Create necessary directories
for directory in [EXTRACTED_LYRICS_DIR, GENERATED_PROMPTS_DIR, PROCESSED_VIDEOS_DIR, LOG_DIR]:
    os.makedirs(directory, exist_ok=True)
