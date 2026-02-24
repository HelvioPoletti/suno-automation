# Suno AI to Whisk Automation - Setup Guide

## Quick Start (5 Minutes)

### Step 1: Clone the Repository
```bash
git clone https://github.com/HelvioPoletti/suno-automation.git
cd suno-automation
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment
```bash
cp .env.example .env
# Edit .env file with your settings:
# - WHISK_API_KEY: Your Whisk AI API key
# - SUNO_DOWNLOADS_DIR: Path to your Suno downloads folder
```

### Step 4: Run Automation
```bash
python run_automation.py
```

## Detailed Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Suno.ai account with downloaded MP3 files
- Whisk AI account (optional, for video generation)

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/HelvioPoletti/suno-automation.git
   cd suno-automation
   ```

2. **Create Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Copy Environment Template**
   ```bash
   cp .env.example .env
   ```

2. **Edit Configuration**
   ```bash
   # .env file settings:
   WHISK_API_KEY=your_api_key_here
   WHISK_BASE_URL=https://whisk.ai/api
   BATCH_SIZE=5
   MAX_WORKERS=4
   TIMEOUT=300
   LOG_LEVEL=INFO
   SUNO_DOWNLOADS_DIR=C:\\Users\\abstt\\OneDrive\\Documentos\\SUNO\\Suno Downloads
   ```

### Directory Structure

The automation creates the following directories automatically:
- `extracted_lyrics/`: Contains extracted lyrics from MP3 files
- `generated_prompts/`: Contains AI-generated prompts for image creation
- `processed_videos/`: Contains final processed videos
- `logs/`: Contains execution logs

## Usage

### Basic Usage
```bash
python run_automation.py
```

### What It Does

1. **Scans Suno Downloads Directory**: Finds all unprocessed MP3 files
2. **Extracts Lyrics**: Uses speech recognition to extract lyrics from MP3s
3. **Generates Prompts**: Creates creative prompts for image generation
4. **Batch Processing**: Processes files in configurable batches for efficiency
5. **Parallel Execution**: Uses multiple workers for faster processing
6. **Logging**: Records all operations in detailed logs

## File Structure

```
suno-automation/
├── run_automation.py          # Main orchestration script
├── config.py                   # Configuration management
├── extract_lyrics.py           # Lyrics extraction module
├── prompt_generator.py         # Prompt generation module
├── automation_setup.py         # Setup and initialization
├── main.py                     # Main execution orchestrator
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── README.md                   # Project overview
├── SETUP_GUIDE.md             # This file
└── logs/                       # Execution logs directory
```

## Troubleshooting

### Issue: "Directory not found"
**Solution**: Check that SUNO_DOWNLOADS_DIR in .env points to the correct path

### Issue: "API Key Invalid"
**Solution**: Verify your WHISK_API_KEY in .env is correct

### Issue: "No unprocessed files found"
**Solution**: Ensure MP3 files are in the configured Suno downloads directory

### Issue: "Timeout errors"
**Solution**: Increase TIMEOUT value in .env (default 300 seconds)

## Advanced Configuration

### Batch Size
- Smaller batches: More frequent processing, less memory usage
- Larger batches: Faster processing, more memory usage
- Recommended: 5-10 files per batch

### Max Workers
- Number of parallel processing threads
- Recommended: 2-4 for standard machines
- Higher values for powerful machines

### Logging
- Set LOG_LEVEL to: DEBUG, INFO, WARNING, ERROR
- Logs saved to: `logs/automation.log`

## Performance Tips

1. Use batch processing for large file sets
2. Adjust MAX_WORKERS based on CPU cores
3. Monitor memory usage during processing
4. Run during off-peak hours for faster execution
5. Check logs for processing bottlenecks

## Security Notes

- Never commit .env file to Git (it's in .gitignore)
- Keep API keys confidential
- Use strong passwords for accounts
- Run on secure machines only

## Support

For issues or questions:
1. Check this setup guide
2. Review logs in `logs/automation.log`
3. Check GitHub Issues

## License

This project is provided as-is for educational purposes.
