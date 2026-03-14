import ollama

# ==================== CONFIGURATION ====================
SOURCE_LANGUAGE = "Python"
TARGET_LANGUAGE = "Java"

CODE_TO_TRANSLATE = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
"""

# =======================================================

def translate_code(code, source_lang, target_lang):
    prompt = f"""Translate this {source_lang} code to {target_lang}.

Provide your response in this format:

TRANSLATED CODE:
[the translated code]

EXPLANATION:
[brief explanation of key differences]

{source_lang} code:
{code}
"""
    
    response = ollama.chat(
        model='qwen2.5-coder:7b',
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    return response['message']['content']

def parse_response(response):
    if "EXPLANATION:" in response:
        parts = response.split("EXPLANATION:")
        code_part = parts[0].replace("TRANSLATED CODE:", "").strip()
        explanation = parts[1].strip()
        return code_part, explanation
    else:
        return response.strip(), None

if __name__ == "__main__":
    print(f"\nTranslating from {SOURCE_LANGUAGE} to {TARGET_LANGUAGE}\n")
    
    # Display source code
    print(f"SOURCE CODE ({SOURCE_LANGUAGE}):")
    print(CODE_TO_TRANSLATE.strip())
    print()
    
    # Translate
    result = translate_code(CODE_TO_TRANSLATE, SOURCE_LANGUAGE, TARGET_LANGUAGE)
    
    # Display results
    translated_code, explanation = parse_response(result)
    
    print(f"TRANSLATED CODE ({TARGET_LANGUAGE}):")
    print(translated_code)
    print()
    
    if explanation:
        print("EXPLANATION:")
        print(explanation)
    else:
        print(result)
    
    print()