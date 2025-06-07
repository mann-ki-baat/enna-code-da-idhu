import os
import json

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "docs"
MESSAGE_FILE = "message.json"

def load_message():
    with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f).get("message", "Hello, World!")

def generate_files():
    message = load_message()
    for filename in os.listdir(TEMPLATE_DIR):
        if filename.endswith(".template"):
            lang_name = filename.replace(".template", "")
            output_filename = f"hello.{lang_name}"

            with open(os.path.join(TEMPLATE_DIR, filename), "r", encoding="utf-8") as template_file:
                content = template_file.read().replace("{{MESSAGE}}", message)

            with open(os.path.join(OUTPUT_DIR, output_filename), "w", encoding="utf-8") as output_file:
                output_file.write(content)

            print(f"Generated: {output_filename}")

if __name__ == "__main__":
    generate_files()