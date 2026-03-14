import ollama
import sys

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

def get_multiline_input():
    print("Paste your code (type 'END' on a new line when done):")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        except EOFError:
            break
    return '\n'.join(lines)

def main():
    print("\nCODE TRANSLATOR BOT")
    print("Supported: Python, JavaScript, Java, C++, C#, Go, Rust, TypeScript, PHP, Ruby, Swift, Kotlin, C, R, Scala\n")
    
    while True:
        # Get source language
        source_lang = input("Source language (or 'quit' to exit): ").strip()
        if source_lang.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!\n")
            break
        
        # Get target language
        target_lang = input("Target language: ").strip()
        
        # Get code
        print()
        code = get_multiline_input()
        
        if not code.strip():
            print("\nNo code provided. Try again.\n")
            continue
        
        # Translate
        print(f"\nTranslating from {source_lang} to {target_lang}...\n")
        result = translate_code(code, source_lang, target_lang)
        
        # Parse and display
        translated_code, explanation = parse_response(result)
        
        print(f"TRANSLATED CODE ({target_lang}):")
        print(translated_code)
        print()
        
        if explanation:
            print("EXPLANATION:")
            print(explanation)
        
        print()
        
        # Ask if user wants to save
        save = input("Save to file? (y/n): ").strip().lower()
        if save == 'y':
            filename = input("Filename: ").strip()
            try:
                with open(filename, 'w') as f:
                    f.write(translated_code)
                print(f"Saved to {filename}\n")
            except Exception as e:
                print(f"Error: {e}\n")
        
        # Continue or exit
        another = input("Translate another? (y/n): ").strip().lower()
        if another != 'y':
            print("\nGoodbye!\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!\n")
        sys.exit(0)
