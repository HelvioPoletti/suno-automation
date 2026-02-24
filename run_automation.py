#!/usr/bin/env python3
"""
Main Orchestration Script for Suno AI to Whisk Automation
Automates the complete workflow: download -> extract lyrics -> generate prompts -> create videos
"""

import os
import sys
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Import configuration and modules
try:
    from config import (
        SUNO_DOWNLOADS_DIR,
        EXTRACTED_LYRICS_DIR,
        GENERATED_PROMPTS_DIR,
        PROCESSED_VIDEOS_DIR,
        BATCH_SIZE,
        MAX_WORKERS,
        LOG_DIR,
        LOG_LEVEL
    )
    from extract_lyrics import extract_lyrics_batch
    from prompt_generator import generate_prompts_batch
    from automation_setup import setup_automation_environment
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, 'automation.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def get_unprocessed_files(directory, processed_dir, extension='.mp3'):
    """
    Get list of files that haven't been processed yet
    """
    if not os.path.exists(directory):
        logger.error(f"Directory not found: {directory}")
        return []
    
    all_files = list(Path(directory).glob(f'*{extension}'))
    processed_files = set(Path(processed_dir).glob(f'*_lyrics.txt')) if os.path.exists(processed_dir) else set()
    
    unprocessed = [f for f in all_files if f'{f.stem}_lyrics.txt' not in {p.name for p in processed_files}]
    logger.info(f"Found {len(unprocessed)} unprocessed files in {directory}")
    return unprocessed


def process_batch(files, batch_num):
    """
    Process a batch of files through the pipeline
    """
    logger.info(f"Processing batch {batch_num} with {len(files)} files")
    
    try:
        # Step 1: Extract lyrics
        logger.info(f"Batch {batch_num}: Extracting lyrics...")
        lyrics_results = extract_lyrics_batch(files, EXTRACTED_LYRICS_DIR)
        
        # Step 2: Generate prompts
        logger.info(f"Batch {batch_num}: Generating prompts...")
        prompt_results = generate_prompts_batch(lyrics_results, GENERATED_PROMPTS_DIR)
        
        logger.info(f"Batch {batch_num}: Successfully processed {len(files)} files")
        return {"batch": batch_num, "status": "success", "files_processed": len(files)}
    
    except Exception as e:
        logger.error(f"Error processing batch {batch_num}: {str(e)}")
        return {"batch": batch_num, "status": "error", "error": str(e)}


def run_full_automation():
    """
    Execute the complete automation workflow
    """
    logger.info("="*50)
    logger.info("Starting Suno AI to Whisk Automation")
    logger.info("="*50)
    
    try:
        # Step 0: Setup environment
        logger.info("Setting up automation environment...")
        setup_automation_environment()
        
        # Step 1: Get unprocessed files
        logger.info(f"Scanning directory: {SUNO_DOWNLOADS_DIR}")
        files = get_unprocessed_files(SUNO_DOWNLOADS_DIR, EXTRACTED_LYRICS_DIR)
        
        if not files:
            logger.info("No unprocessed files found. Exiting.")
            return {"status": "completed", "files_processed": 0}
        
        logger.info(f"Total files to process: {len(files)}")
        
        # Step 2: Process files in batches
        batches = [files[i:i+BATCH_SIZE] for i in range(0, len(files), BATCH_SIZE)]
        logger.info(f"Processing {len(batches)} batches of up to {BATCH_SIZE} files each")
        
        results = []
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(process_batch, batch, i+1): i for i, batch in enumerate(batches)}
            
            for future in as_completed(futures):
                batch_num = futures[future] + 1
                try:
                    result = future.result()
                    results.append(result)
                    logger.info(f"Batch {batch_num} completed: {result}")
                except Exception as e:
                    logger.error(f"Batch {batch_num} failed: {str(e)}")
                    results.append({"batch": batch_num, "status": "error", "error": str(e)})
        
        # Summary
        logger.info("="*50)
        logger.info("Automation Complete!")
        successful = sum(1 for r in results if r.get("status") == "success")
        logger.info(f"Successfully processed {successful}/{len(batches)} batches")
        logger.info("="*50)
        
        return {"status": "completed", "batches_processed": len(batches), "successful": successful}
    
    except Exception as e:
        logger.error(f"Fatal error in automation: {str(e)}")
        return {"status": "failed", "error": str(e)}


if __name__ == "__main__":
    result = run_full_automation()
    sys.exit(0 if result.get("status") == "completed" else 1)
