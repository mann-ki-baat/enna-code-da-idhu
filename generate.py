import os
import json
import html

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

print(f"Generating site in: {output_root}")
os.makedirs(output_root, exist_ok=True)

# For language extension mapping
extension_map = {
    "python": "py",
    "javascript": "js",
    "c": "c",
    "bash": "sh",
    "basic": "bas",
    "brainfuck": "bf"
}

language_blocks = []

for filename in os.listdir(template_dir):
    if not filename.endswith(".template"):
        continue

    lang = filename[:-9]  # remove .template
    extension = extension_map.get(lang, lang)

    # Read the template and generate code
    with open(os.path.join(template_dir, filename), 'r', encoding='utf-8') as f:
        template = f.read()

    code = template.replace("{{message}}", message)
    if lang == "brainfuck":
        code = text_to_brainfuck(message)

    lang_output_dir = os.path.join(output_root, lang)
    os.makedirs(lang_output_dir, exist_ok=True)
    file_path = os.path.join(lang_output_dir, f"hello.{extension}")

    with open(file_path, 'w', encoding='utf-8') as out:
        out.write(code)

    print(f"Written to: {file_path}")

    # Add code block for index.html
    escaped_code = html.escape(code)
    language_blocks.append(f"""
    <details>
      <summary><strong>{lang.title()}</strong> — <a href="{lang}/hello.{extension}" target="_blank">View raw</a></summary>
      <pre><code>{escaped_code}</code></pre>
    </details>
    """)

# Build index.html
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Enna Code Da Idhu?</title>
  <style>
    body {{
      font-family: monospace;
      background: black;
      color: lime;
      padding: 2em;
    }}
    h1 {{
      color: cyan;
      text-shadow: 0 0 5px blue;
    }}
    details {{
      margin: 1em 0;
      border: 1px solid lime;
      padding: 0.5em;
    }}
    summary {{
      cursor: pointer;
      font-size: 1.1em;
    }}
    pre {{
      background: #111;
      padding: 1em;
      overflow-x: auto;
      color: white;
    }}
    a {{
      color: orange;
    }}
  </style>
</head>
<body>
  <h1>Enna Code Da Idhu?</h1>
  <p>A museum of Hello World programs in as many languages as I can possibly find.</p>

  {"".join(language_blocks)}

</body>
</html>
"""

with open(os.path.join(output_root, "index.html"), 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Homepage generated: docs/index.html")