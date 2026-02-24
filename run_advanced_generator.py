#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run Advanced Prompt Generator
Easy execution script for generating advanced prompts
"""

import sys
import subprocess
from pathlib import Path

# Add script directory to path
script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

def main():
    print("\n" + "="*80)
    print("GERADOR AVANÇADO DE PROMPTS PARA WHISK AI")
    print("="*80)
    print()
    print("Importando módulos necessários...")
    
    try:
        # Importe o módulo avançado
        from advanced_prompt_generator import process_all_lyrics
        
        print("✅ Módulo carregado com sucesso!\n")
        
        # Defina os diretórios
        LYRICS_DIR = r'C:\Users\abstt\suno-automation\extracted_lyrics'
        OUTPUT_DIR = r'C:\Users\abstt\suno-automation\advanced_prompts'
        
        print(f"📁 Diretório de letras: {LYRICS_DIR}")
        print(f"📁 Diretório de saída: {OUTPUT_DIR}\n")
        
        # Verifique se o diretório de letras existe
        lyrics_path = Path(LYRICS_DIR)
        if not lyrics_path.exists():
            print(f"❌ ERRO: Diretório de letras não encontrado!")
            print(f"   Caminho esperado: {LYRICS_DIR}")
            print(f"   Certifique-se de que o script 'run_simple.py' foi executado primeiro.")
            return False
        
        # Conte arquivos de letra
        lyrics_files = list(lyrics_path.glob('*.txt'))
        if not lyrics_files:
            print(f"❌ ERRO: Nenhum arquivo de letra encontrado em {LYRICS_DIR}")
            return False
        
        print(f"📊 Encontrados {len(lyrics_files)} arquivos de letra")
        print(f"🎯 Serão gerados {len(lyrics_files) * 5} prompts (5 por música)\n")
        
        print("Iniciando processamento...\n")
        
        # Execute o processamento
        process_all_lyrics(LYRICS_DIR, OUTPUT_DIR)
        
        print("\n" + "="*80)
        print("✅ PROCESSAMENTO FINALIZADO COM SUCESSO!")
        print("="*80)
        print(f"\n📝 Próximas etapas:")
        print(f"   1. Abra a pasta: {OUTPUT_DIR}")
        print(f"   2. Você verá arquivos como: NOME_MUSICA_prompt_1.txt até prompt_5.txt")
        print(f"   3. Cada arquivo contém um prompt pronto para usar no Whisk AI")
        print(f"   4. Visite: https://labs.google/fx/tools/whisk")
        print(f"   5. Cole os prompts um por um ou em lote para gerar imagens")
        print(f"\n💡 Dica: Para processar mais rápido, você pode:\n")
        print(f"   - Usar o navegador para abrir múltiplas abas do Whisk")
        print(f"   - Colar vários prompts simultaneamente (se Whisk permitir batch)")
        print(f"   - Fazer download das imagens em lote\n")
        
        return True
        
    except ImportError as e:
        print(f"❌ ERRO de importação: {str(e)}")
        print(f"\nCertifique-se de que o arquivo 'advanced_prompt_generator.py' está no mesmo diretório.")
        return False
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {str(e)}")
        print(f"\nFaça um screenshot desta mensagem e envie para análise.")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    
    if not success:
        print("\n" + "="*80)
        print("❌ Executionfalhou. Verifique os erros acima.")
        print("="*80)
        sys.exit(1)
    else:
        print("\nPressione ENTER para fechar...")
        input()
