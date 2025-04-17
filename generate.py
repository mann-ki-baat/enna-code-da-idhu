import json
import os

def text_to_brainfuck(text):
    bf = ""
    for char in text:
        bf += "+" * ord(char) + "[>]" + "." + "\n"
    return bf

# Load global message
with open("message.json") as f:
    config = json.load(f)

message = config["message"]

# Template folder
template_dir = "templates"

# Output base folder
output_base = "."

for template_file in os.listdir(template_dir):
    if not template_file.endswith(".template"):
        continue

    lang = template_file.replace(".template", "")
    lang_dir = os.path.join(output_base, lang)
    os.makedirs(lang_dir, exist_ok=True)

    # Read template
    with open(os.path.join(template_dir, template_file)) as f:
        template = f.read()

    if lang == "brainfuck":
        output = text_to_brainfuck(message)
        out_file = os.path.join(lang_dir, "hello.bf")
    elif lang == "c":
        out_file = os.path.join(lang_dir, "hello.c")
        output = template.replace("{{MESSAGE}}", message)
    elif lang == "bash":
        out_file = os.path.join(lang_dir, "hello.sh")
        output = template.replace("{{MESSAGE}}", message)
    elif lang == "basic":
        out_file = os.path.join(lang_dir, "hello.bas")
        output = template.replace("{{MESSAGE}}", message)
    else:
        ext = {
            "python": "py",
            "javascript": "js",
            "ruby": "rb",
            "java": "java",
            "go": "go",
            "rust": "rs"
        }.get(lang, lang)
        out_file = os.path.join(lang_dir, f"hello.{ext}")
        output = template.replace("{{MESSAGE}}", message)

    with open(out_file, "w") as f:
        f.write(output)

print("✨ All files generated from templates!")