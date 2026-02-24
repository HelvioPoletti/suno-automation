#!/usr/bin/env python3
"""
Generate Whisk AI prompts from lyrics
"""

import json
from pathlib import Path

def create_prompt_from_lyrics(lyrics, song_title=""):
    """
    Transform lyrics into a creative Whisk AI prompt
    """
    # Extract key themes and emotions from lyrics
    keywords = extract_keywords(lyrics)
    mood = analyze_mood(lyrics)
    style = determine_style(lyrics)
    
    prompt = f"""
Create a visually stunning music video for: {song_title}

Mood: {mood}
Style: {style}
Key Elements: {', '.join(keywords)}

Generate dynamic, high-quality video frames that match these themes.
Focus on: cinematography, color grading, transitions
"""
    
    return prompt.strip()

def extract_keywords(lyrics):
    """
    Extract important keywords from lyrics
    """
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
    words = lyrics.lower().split()
    keywords = [w for w in words if len(w) > 4 and w not in stop_words]
    return list(set(keywords))[:5]

def analyze_mood(lyrics):
    """
    Analyze emotional tone of lyrics
    """
    positive_words = ['happy', 'love', 'joy', 'bright', 'beautiful', 'amazing']
    negative_words = ['sad', 'dark', 'night', 'pain', 'break', 'lost']
    
    lyrics_lower = lyrics.lower()
    positive_count = sum(1 for w in positive_words if w in lyrics_lower)
    negative_count = sum(1 for w in negative_words if w in lyrics_lower)
    
    if positive_count > negative_count:
        return "Uplifting, joyful, vibrant"
    elif negative_count > positive_count:
        return "Emotional, dramatic, introspective"
    else:
        return "Balanced, neutral, energetic"

def determine_style(lyrics):
    """
    Determine visual style from lyrics
    """
    return "Modern, cinematic, high contrast"

def generate_prompts(lyrics_dir='lyrics', output_dir='prompts'):
    """
    Generate prompts for all lyrics files
    """
    Path(output_dir).mkdir(exist_ok=True)
    results = {}
    
    for lyrics_file in Path(lyrics_dir).glob('*.txt'):
        with open(lyrics_file, 'r', encoding='utf-8') as f:
            lyrics = f.read()
        
        prompt = create_prompt_from_lyrics(lyrics, lyrics_file.stem)
        output_file = Path(output_dir) / f"{lyrics_file.stem}_prompt.txt"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        results[lyrics_file.name] = 'Generated'
        print(f"✓ Generated prompt for {lyrics_file.stem}")
    
    return results

if __name__ == "__main__":
    results = generate_prompts()
    print(f"\nGenerated {len(results)} prompts")
    print(json.dumps(results, indent=2))
