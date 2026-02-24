# Advanced Prompt Generator Guide

## 🎯 O que é o Gerador Avançado de Prompts?

Este gerador analisa o conteúdo e emoção das letras das músicas e cria **5 prompts únicos e temáticos** por música, aumentando drasticamente a qualidade e variedade das imagens geradas no Whisk AI.

### Comparação:

**Gerador Básico:**
- 1 prompt por música
- Genérico e simples
- Resultado: 255 prompts (1 × 255 músicas)

**Gerador Avançado:**
- 5 prompts por música
- Temáticos e personalizados por emoção
- Resultado: **1.275 prompts** (5 × 255 músicas)
- **5 imagens diferentes por música** (2 variações por prompt)

---

## 📊 Como Funciona

### Passo 1: Análise da Letra
```
Música MP3 → Extrair Letra → Analisar Conteúdo Temático
```

### Passo 2: Identificar 10 Temas Possíveis

O gerador busca palavras-chave em 10 categorias:

| Tema | Palavras-Chave | Exemplo |
|------|---|---|
| **Darkness** | escuro, noite, sombra | Paisagem escura e misteriosa |
| **Power** | força, poder, forte | Explosão de energia |
| **Energy** | energi, elétrico, vibrant | Raios luminosos pulsantes |
| **Emotion** | sinto, coração, alma, dor | Cena emocional expressiva |
| **Movement** | dança, movimento, voo | Dinâmica e fluxo |
| **Destruction** | quebra, destruir, estrago | Cataclismo visual |
| **Light** | luz, brilho, luminoso | Manifestação de luz divina |
| **Cosmic** | espaço, estrela, universo | Cenário galáctico |
| **Nature** | natureza, floresta, água | Paisagem selvagem |
| **Technological** | digital, futuro, ciber | Estética futurista |

### Passo 3: Gerar 5 Prompts Personalizados

Para cada um dos 5 temas principais encontrados:

```python
Tema + Elemento + Cor + Contexto = PROMPT ÚNICO
```

**Exemplo Real:**
```
Música: "PRESSURE BUILT ME"

Temas Detectados: [Power, Destruction, Energy, Darkness, Emotion]

Prompt 1 (Power):
"Powerful, explosive scene showing raw force and shockwave. 
Dynamic energy waves in red. Intense lighting creating dramatic shadows..."

Prompt 2 (Destruction):
"Cataclysmic scene showing fracturing reality breaking and transforming. 
Explosive impact with orange light. Debris and energy bursting outward..."

Prompt 3 (Energy):
"Vibrant, pulsing energy visualization with electric discharge in motion. 
Neon cyan patterns and glowing geometric shapes..."

(... e mais 2 prompts únicos)
```

---

## 🚀 Como Usar

### Pré-requisitos
1. Você já executou `run_simple.py` e tem 255 arquivos em:
   - `C:\Users\abstt\suno-automation\extracted_lyrics\`

### Execução

#### Opção 1: Linha de Comando (Recomendado)

1. Abra PowerShell ou CMD
2. Navegue até a pasta do projeto:
   ```powershell
   cd C:\Users\abstt\suno-automation
   ```

3. Execute o gerador:
   ```powershell
   python run_advanced_generator.py
   ```

4. Aguarde a execução (aproximadamente 2-5 minutos para 255 músicas)

#### Opção 2: Executar Diretamente em Python

```python
from advanced_prompt_generator import process_all_lyrics

process_all_lyrics(
    r'C:\Users\abstt\suno-automation\extracted_lyrics',
    r'C:\Users\abstt\suno-automation\advanced_prompts'
)
```

### Saída Esperada

Após a execução, você terá uma pasta `advanced_prompts` contendo:

```
advanced_prompts/
├── MUSICA_1_prompt_1.txt       # Prompt 1 da música 1
├── MUSICA_1_prompt_2.txt       # Prompt 2 da música 1
├── MUSICA_1_prompt_3.txt       # Prompt 3 da música 1
├── MUSICA_1_prompt_4.txt       # Prompt 4 da música 1
├── MUSICA_1_prompt_5.txt       # Prompt 5 da música 1
├── MUSICA_1_metadata.json      # Metadados (temas, cores, elementos)
├── MUSICA_2_prompt_1.txt
├── MUSICA_2_prompt_2.txt
├── ...
└── MUSICA_255_prompt_5.txt

Total: ~1.275 arquivos .txt + 255 arquivos .json
```

---

## 🎬 Próximas Etapas - Usar no Whisk AI

### Método 1: Upload Manual (Mais Controle)

1. Acesse [https://labs.google/fx/tools/whisk](https://labs.google/fx/tools/whisk)
2. Abra vários prompts do arquivo
3. Cola cada prompt no Whisk
4. Clique em "Gerar" (seta)
5. Whisk gera 2 imagens por prompt
6. Faça download das imagens

### Método 2: Batch Processing (Se Whisk Permitir)

1. Use um script para fazer upload automático
2. Salve o JSON de cada música para manter rastreabilidade
3. Baixe todas as imagens de uma só vez

---

## 📈 Métricas & Performance

| Métrica | Valor |
|---------|-------|
| Músicas processadas | 255 |
| Prompts por música | 5 |
| **Total de prompts** | **1.275** |
| Imagens por prompt (Whisk) | 2 |
| **Total de imagens** | **2.550** |
| Tempo de execução | 2-5 min |
| Temas analisados | 10 |
| Tamanho médio do arquivo | ~500 bytes |

---

## 🔍 Exemplo de Prompt Gerado

```
Vibrant, pulsing energy visualization with plasma flow in motion. 
Neon cyan patterns and glowing geometric shapes. Synchronized with 
intense beat. Professional 4K quality. Inspired by the music 
'PRESSURE BUILT ME'. Create a music video visualization.
```

---

## 🛠️ Troubleshooting

### Problema: "Nenhum arquivo de letra encontrado"
**Solução:** Execute `run_simple.py` primeiro para extrair as letras

### Problema: Script não inicia
**Solução:** Certifique-se de que está na pasta correta:
```powershell
cd C:\Users\abstt\suno-automation
python run_advanced_generator.py
```

### Problema: Erro de encoding
**Solução:** O script usa UTF-8 automaticamente. Se persistir:
```powershell
chcp 65001  # Mude para UTF-8
python run_advanced_generator.py
```

---

## 📝 Arquivos de Saída

### Arquivo de Prompt (.txt)
```
[ARQUIVO: MUSICA_TITULO_prompt_1.txt]

Vibrant, pulsing energy visualization with plasma flow in motion...
```

### Arquivo de Metadados (.json)
```json
{
  "title": "MUSICA TITULO",
  "prompts": [
    {
      "prompt_number": 1,
      "theme": "energy",
      "element": "plasma flow",
      "accent_color": "cyan",
      "content": "Vibrant, pulsing..."
    },
    ...
  ]
}
```

---

## 🎨 Customização

Se quiser modificar os elementos, cores ou temas, edite o arquivo `advanced_prompt_generator.py`:

```python
# Adicione novas cores
ACCENT_COLORS['tema_novo'] = ['cor1', 'cor2', 'cor3']

# Adicione novos elementos
ELEMENTS['tema_novo'] = ['elemento1', 'elemento2']

# Modifique templates
PROMPT_TEMPLATES['tema_novo'] = "Seu template customizado com {element} e {accent_color}"
```

---

## 📞 Suporte

Para problemas ou dúvidas:
1. Verifique a saída do console para mensagens de erro
2. Confirme que os diretórios existem
3. Teste com 1 música primeiro para validar o setup

---

**Última atualização:** Fevereiro 24, 2026
**Versão:** 2.0 - Advanced Prompt Generator
