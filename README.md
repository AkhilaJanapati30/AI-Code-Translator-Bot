# AI Code Translator Bot

A Python-based code translator that uses local AI (via [Ollama](https://ollama.com)) to translate code between programming languages. The bot provides both the translated code and a brief explanation of key differences between the source and target language implementations.

## Features

- **Multi-language support**: Translate between Python, JavaScript, Java, C++, C#, Go, Rust, TypeScript, PHP, Ruby, Swift, Kotlin, C, R, Scala, and more
- **Structured output**: Returns translated code plus an explanation of important semantic or syntactic differences
- **Interactive CLI**: Paste code, get translations, optionally save to file, and run multiple translations in one session
- **Script mode**: Run one-off translations with hardcoded source/target and code (useful for demos or automation)
- **Runs locally**: Uses Ollama, so no API keys or cloud dependency—everything runs on your machine

## Prerequisites

1. **Python 3.7+**
2. **Ollama** installed and running on your system  
   - Install from: [https://ollama.com](https://ollama.com)  
   - Ensure the Ollama service is running (e.g. `ollama serve` or the desktop app).
3. **Model**: The project uses **Qwen 2.5 Coder 7B** via Ollama. Pull it once:

   ```bash
   ollama pull qwen2.5-coder:7b
   ```

## Packages to Install

From the project root:

```bash
pip install ollama
```

Or use a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate
pip install ollama
```

### Dependency Summary

| Package | Purpose |
|--------|---------|
| `ollama` | Python client for the Ollama API (local LLM inference) |

Standard library modules used: `sys` (in `translatorBot.py` only).

## Models Used

- **Primary model**: `qwen2.5-coder:7b`  
  - Used in both `translator.py` and `translatorBot.py` for code translation.  
  - You can switch to another Ollama model by changing the `model` argument in the `ollama.chat()` call in the respective file.

## Project Structure

```
AI-Code-Translator-Bot/
├── README.md
├── translator.py       # One-off translation with config at top of file
├── translatorBot.py    # Interactive CLI translator with save option
└── Code_Translator_Bot_Presentation.pptx   # Project presentation
```

## Usage

### Interactive bot (`translatorBot.py`)

Run the interactive translator: choose source and target languages, paste code, and optionally save the result.

```bash
python translatorBot.py
```

- When prompted, enter **source language** (e.g. `Python`) and **target language** (e.g. `Java`).
- Paste your code, then type **END** on a new line when finished.
- The bot prints the translated code and an explanation.
- Optionally save to a file (`y` when asked) and continue with another translation or exit.

### Script / demo (`translator.py`)

Run a single translation with predefined settings. Edit the constants at the top of `translator.py` to change source/target language and the code snippet:

```python
SOURCE_LANGUAGE = "Python"
TARGET_LANGUAGE = "Java"
CODE_TO_TRANSLATE = """
def fibonacci(n):
    ...
"""
```

Then run:

```bash
python translator.py
```

Output includes the source code, translated code, and explanation.

## Example Output Format

The model is prompted to respond in this format:

- **TRANSLATED CODE:**  
  The code in the target language.
- **EXPLANATION:**  
  A short description of main differences (e.g. syntax, types, idioms).

The scripts parse this structure and print the two parts separately.

## Presentation

A project overview and demo can be found in **Code_Translator_Bot_Presentation.pptx**.

## License

Use and modify as needed for your project. If you use or extend this code, attribution is appreciated.
