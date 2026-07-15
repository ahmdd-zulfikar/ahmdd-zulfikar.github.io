import os

base_dir = r"D:\Project\ahmdd-zulfikar.github.io\mtsn6-demak\2026-2027"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    content = content.replace('href="../../IPA"', 'href="../../akidah-akhlak"')
    content = content.replace('href="../../IPA/', 'href="../../akidah-akhlak/')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_file(filepath)

print("Finished replacing paths.")
