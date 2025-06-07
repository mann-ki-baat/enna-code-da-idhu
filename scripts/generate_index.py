import os

# Path to the output directory
DOCS_DIR = "docs"
OUTPUT_FILE = os.path.join(DOCS_DIR, "index.html")

# Get list of language folders (excluding styles, hidden folders, etc.)
language_dirs = [
    d for d in os.listdir(DOCS_DIR)
    if os.path.isdir(os.path.join(DOCS_DIR, d))
       and not d.startswith(".")
       and d != "styles"
]

# Sort alphabetically
language_dirs.sort()

# HTML Template
html_start = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>A Museum of Hello World Programs</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>
    <div class="container">
        <h1>🎉 A Museum of Hello World Programs 🎉</h1>
        <p class="subtitle">Because one "Hello, World!" is never enough.</p>
        <div class="grid">
'''

html_end = '''
        </div>
    </div>
</body>
</html>
'''

# Generate grid tiles for each language
tiles_html = ""
for lang in language_dirs:
    lang_label = lang.replace("_", " ").capitalize()
    tiles_html += f'            <a class="lang-tile" href="{lang}/index.html">{lang_label}</a>\n'

# Write to index.html
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html_start + tiles_html + html_end)

print(f"✅ index.html generated with {len(language_dirs)} languages.")