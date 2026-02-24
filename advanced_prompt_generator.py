#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Prompt Generator with Music Analysis
Analyzes song lyrics to generate 5 thematic prompts per song
Optimized for Whisk AI video generation
"""

import os
import json
from pathlib import Path
from collections import Counter
import re

# Mapeamento de palavras-chave para temas
THEME_KEYWORDS = {
    'darkness': ['dark', 'darkness', 'black', 'night', 'shadow', 'sombra', 'escuro', 'noite'],
    'power': ['power', 'force', 'strong', 'mighty', 'powerful', 'forca', 'poder', 'forte'],
    'energy': ['energy', 'electric', 'lightning', 'vibrant', 'energi', 'eletric', 'raio'],
    'emotion': ['feel', 'heart', 'soul', 'love', 'pain', 'sinto', 'coracao', 'alma', 'dor', 'amor'],
    'movement': ['moving', 'dance', 'jump', 'run', 'fly', 'danca', 'salto', 'correr', 'voar'],
    'destruction': ['break', 'destroy', 'crush', 'shatter', 'ruin', 'quebra', 'destruir', 'estrago'],
    'light': ['light', 'bright', 'sun', 'glow', 'shine', 'luz', 'brilho', 'sol', 'brilhante'],
    'cosmic': ['space', 'star', 'universe', 'galaxy', 'cosmic', 'espaco', 'estrela', 'universo'],
    'nature': ['nature', 'forest', 'mountain', 'water', 'wind', 'natureza', 'floresta', 'montanha', 'agua', 'vento'],
    'technological': ['machine', 'digital', 'robot', 'future', 'cyber', 'maquina', 'digital', 'futuro', 'ciber']
}

PROMPT_TEMPLATES = {
    'darkness': "Dark, ominous landscape with {element}. Deep shadows and mysterious atmospheres. Black clouds with hints of {accent_color}. Cinematic, dramatic, moody lighting. Professional 4K quality.",
    'power': "Powerful, explosive scene showing raw force and {element}. Dynamic energy waves in {accent_color}. Intense lighting creating dramatic shadows. Professional 4K cinematic quality.",
    'energy': "Vibrant, pulsing energy visualization with {element} in motion. Neon {accent_color} patterns and glowing geometric shapes. Synchronized with intense beat. Professional 4K quality.",
    'emotion': "Emotional journey visualized through {element}. Artistic, expressive scenes with {accent_color} tones. Deep, introspective atmosphere. Cinematic quality. 4K resolution.",
    'movement': "Dynamic motion scene with {element} flowing and moving. Kinetic energy in {accent_color} colors. Blurred movement effects, fast-paced action. Professional 4K quality.",
    'destruction': "Cataclysmic scene showing {element} breaking and transforming. Explosive impact with {accent_color} light. Debris and energy bursting outward. Dramatic 4K cinematic quality.",
    'light': "Brilliant light manifestation with {element} illuminated. Divine rays of {accent_color} piercing through atmosphere. Heavenly, ethereal atmosphere. Professional 4K quality.",
    'cosmic': "Cosmic visualization featuring {element} in space. {accent_color} nebula and stellar phenomena. Universe-scale perspective. Sci-fi cinematic 4K quality.",
    'nature': "Natural landscape showing {element} in wild form. Earthy {accent_color} tones with organic textures. Majestic, untamed beauty. Professional 4K cinematic quality.",
    'technological': "Futuristic {element} with digital aesthetics. Neon {accent_color} technology patterns and cyber elements. High-tech, sci-fi atmosphere. Professional 4K quality."
}

ELEMENTS = {
    'darkness': ['abyssal void', 'storm clouds', 'cosmic darkness', 'shadow dimension', 'midnight abyss'],
    'power': ['shockwave', 'energy vortex', 'force field', 'gravitational wave', 'electromagnetic pulse'],
    'energy': ['plasma flow', 'electric discharge', 'quantum field', 'light waves', 'matter transformation'],
    'emotion': ['heart glowing', 'soul manifestation', 'ethereal form', 'living emotion', 'spirit energy'],
    'movement': ['swirling vortex', 'flowing particles', 'kinetic trails', 'dynamic waves', 'motion streaks'],
    'destruction': ['fracturing reality', 'shattering landscape', 'explosive core', 'rupture event', 'collapse sequence'],
    'light': ['luminous sphere', 'radiant core', 'heavenly glow', 'stellar burst', 'divine light'],
    'cosmic': ['black hole', 'nebula', 'quantum realm', 'dimensional rift', 'universe gateway'],
    'nature': ['ancient forest', 'towering mountain', 'raging waterfall', 'wild storm', 'primal landscape'],
    'technological': ['digital matrix', 'holographic system', 'quantum computer', 'neural network', 'AI consciousness']
}

ACCENT_COLORS = {
    'darkness': ['purple', 'deep blue', 'dark red', 'magenta', 'violet'],
    'power': ['red', 'orange', 'golden', 'amber', 'bright yellow'],
    'energy': ['cyan', 'blue', 'electric purple', 'neon green', 'bright white'],
    'emotion': ['pink', 'magenta', 'rose', 'soft gold', 'silver'],
    'movement': ['white', 'silver', 'cyan', 'electric blue', 'bright colors'],
    'destruction': ['red', 'orange', 'yellow', 'molten gold', 'bright white'],
    'light': ['gold', 'white', 'silver', 'pale yellow', 'bright cream'],
    'cosmic': ['purple', 'cyan', 'blue', 'electric magenta', 'space blue'],
    'nature': ['green', 'brown', 'earth tones', 'forest green', 'golden brown'],
    'technological': ['neon cyan', 'electric purple', 'bright pink', 'holographic colors', 'digital blue']
}

def analyze_lyrics(lyrics_content):
    """Analisa o conteúdo da letra e identifica temas principais"""
    lyrics_lower = lyrics_content.lower()
    
    # Conte ocorrências de palavras-chave por tema
    theme_scores = {theme: 0 for theme in THEME_KEYWORDS}
    
    for theme, keywords in THEME_KEYWORDS.items():
        for keyword in keywords:
            theme_scores[theme] += lyrics_lower.count(keyword)
    
    # Ordene temas por pontuação
    sorted_themes = sorted(theme_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Retorne top 5 temas
    top_themes = [theme for theme, score in sorted_themes[:5] if score > 0]
    
    # Se houver menos de 5 temas com score > 0, preencha com mais
    if len(top_themes) < 5:
        top_themes.extend([theme for theme, score in sorted_themes if theme not in top_themes][:5-len(top_themes)])
    
    return top_themes[:5]

def generate_prompts(music_title, lyrics_content):
    """Gera 5 prompts diferentes e temáticos para uma música"""
    themes = analyze_lyrics(lyrics_content)
    prompts = []
    
    import random
    
    for i, theme in enumerate(themes[:5]):
        # Selecione elemento e cor aleatoriamente
        element = random.choice(ELEMENTS.get(theme, ELEMENTS['power']))
        accent_color = random.choice(ACCENT_COLORS.get(theme, ACCENT_COLORS['power']))
        
        # Gere o prompt usando o template
        template = PROMPT_TEMPLATES.get(theme, PROMPT_TEMPLATES['power'])
        prompt = template.format(element=element, accent_color=accent_color)
        
        # Adicione contexto da música
        prompt += f" Inspired by the music '{music_title}'. Create a music video visualization."
        
        prompts.append({
            'prompt_number': i + 1,
            'theme': theme,
            'element': element,
            'accent_color': accent_color,
            'content': prompt
        })
    
    return prompts

def process_all_lyrics(lyrics_dir, output_dir):
    """Processa todas as letras e gera 5 prompts por música"""
    lyrics_path = Path(lyrics_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    lyrics_files = list(lyrics_path.glob('*.txt'))
    total_files = len(lyrics_files)
    
    print(f"\n{'='*80}")
    print(f"PROCESSANDO {total_files} MÚSICAS")
    print(f"{'='*80}\n")
    
    for idx, lyrics_file in enumerate(lyrics_files, 1):
        try:
            music_title = lyrics_file.stem
            
            with open(lyrics_file, 'r', encoding='utf-8') as f:
                lyrics_content = f.read()
            
            # Gere 5 prompts
            prompts = generate_prompts(music_title, lyrics_content)
            
            # Salve cada prompt em um arquivo separado
            for prompt_data in prompts:
                prompt_num = prompt_data['prompt_number']
                filename = f"{music_title}_prompt_{prompt_num}.txt"
                filepath = output_path / filename
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(prompt_data['content'])
            
            # Salve também um JSON com metadados
            json_filename = f"{music_title}_metadata.json"
            json_filepath = output_path / json_filename
            
            with open(json_filepath, 'w', encoding='utf-8') as f:
                json.dump({
                    'title': music_title,
                    'prompts': prompts
                }, f, ensure_ascii=False, indent=2)
            
            print(f"[{idx}/{total_files}] ✅ {music_title}")
            print(f"  → 5 prompts gerados (temas: {', '.join([p['theme'] for p in prompts])})")
        
        except Exception as e:
            print(f"[{idx}/{total_files}] ❌ ERRO em {lyrics_file.name}: {str(e)}")
    
    print(f"\n{'='*80}")
    print(f"✅ PROCESSAMENTO CONCLUÍDO!")
    print(f"📊 Total de músicas: {total_files}")
    print(f"📝 Total de prompts: {total_files * 5}")
    print(f"📁 Salvos em: {output_dir}")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    # Defina os diretórios
    LYRICS_DIR = r'C:\Users\abstt\suno-automation\extracted_lyrics'
    OUTPUT_DIR = r'C:\Users\abstt\suno-automation\advanced_prompts'
    
    # Execute o processamento
    process_all_lyrics(LYRICS_DIR, OUTPUT_DIR)
