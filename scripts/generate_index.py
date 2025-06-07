import os

DOCS_DIR = "docs"
INDEX_FILE = os.path.join(DOCS_DIR, "index.html")

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>A Museum of Hello World Programs</title>
    <style>
        body {
            background-color: #111;
            color: #00FFAA;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            padding: 2rem;
        }
        h1 {
            font-size: 3em;
            text-shadow: 0 0 10px #0ff;
        }
        .lang-list {
            margin-top: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1rem;
        }
        a {
            color: #FFAA00;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.2s ease-in-out;
        }
        a:hover {
            color: #FFFFFF;
            text-shadow: 0 0 5px #FA0, 0 0 15px #FA0;
        }
    </style>
</head>
<body>
    <h1>🎉 A Museum of Hello World Programs 🎉</h1>
    <p>Because one "Hello, World!" is never enough.</p>
    <div class="lang-list">
"""

HTML_TAIL = """
    </div>
</body>
</html>
"""

def get_language_links():
    files = os.listdir(DOCS_DIR)
    links = []
    for filename in sorted(files):
        if filename == "index.html" or filename.startswith(".") or os.path.isdir(os.path.join(DOCS_DIR, filename)):
            continue
        lang_name = os.path.splitext(filename)[0].capitalize()
        links.append(f'<a href="{filename}" target="_blank">{lang_name}</a>')
    return links

def build_index():
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(HTML_HEAD)
        for link in get_language_links():
            f.write(f"{link}\n")
        f.write(HTML_TAIL)

if __name__ == "__main__":
    build_index()
    print(f"✅ index.html generated at {INDEX_FILE}")