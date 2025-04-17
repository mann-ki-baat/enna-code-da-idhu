import os
import json

def text_to_brainfuck(text):
    bf = ""
    for char in text:
        bf += "+" * ord(char) + "[>]" + "." + "\n"
    return bf

# Load the message
with open('message.json', 'r', encoding='utf-8') as f:
    message_data = json.load(f)

message = message_data["message"]

template_dir = "templates"
output_root = "docs"

print(f"Output folder: {output_root}")
os.makedirs(output_root, exist_ok=True)

for filename in os.listdir(template_dir):
    if not filename.endswith(".template"):
        continue

    lang = filename[:-9]  # remove extension
    extension = {
        "python": "py",
        "javascript": "js",
        "c": "c",
        "bash": "sh",
        "basic": "bas",
        "brainfuck": "bf"
    }.get(lang, lang)  # fallback to lang if not mapped

    with open(os.path.join(template_dir, filename), 'r', encoding='utf-8') as f:
        template = f.read()

    code = template.replace("{{message}}", message)

    if lang == "brainfuck":
        code = text_to_brainfuck(message)

    lang_output_dir = os.path.join(output_root, lang)
    os.makedirs(lang_output_dir, exist_ok=True)

    with open(os.path.join(lang_output_dir, f"hello.{extension}"), 'w', encoding='utf-8') as out:
        out.write(code)

    print(f"Generated: {lang}/hello.{extension}")

print("✨ All files generated from templates!")