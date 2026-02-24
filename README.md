# Suno AI to Whisk Automation

Automated workflow to convert Suno AI-generated music into YouTube-ready videos using Whisk AI image generation.

## Features

- Automatically extract lyrics from MP3 files
- Generate creative prompts from lyrics for image generation
- Batch process multiple songs
- Integration with Whisk AI API for image/video creation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HelvioPoletti/suno-automation.git
cd suno-automation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run setup:
```bash
python automation_setup.py
```

## Usage

1. Place MP3 files in `mp3_files/` directory
2. Run the automation:
```bash
python main.py
```
3. Review generated prompts in `prompts/` directory
4. Upload to Whisk AI for video generation

## Files

- `automation_setup.py` - Initial setup and environment configuration
- `extract_lyrics.py` - Extract lyrics from MP3 metadata
- `prompt_generator.py` - Generate Whisk AI prompts from lyrics
- `main.py` - Main orchestration script

## Requirements

- Python 3.7+
- mutagen (for MP3 metadata)
- python-dotenv (for environment variables)
- Whisk API key (for image generation)

## License

MIT
