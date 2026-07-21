import re

filepath = r"D:\Project\ahmdd-zulfikar.github.io\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the CSS block
css_block = re.search(r'/\*\s*Animations\s*\*/.*?@keyframes fadeIn.*?\}\s*\}', content, re.DOTALL)
if css_block:
    content = content.replace(css_block.group(0), '')

# Remove classes from HTML
content = re.sub(r'\s*\bfade-in\b', '', content)
content = re.sub(r'\s*\bdelay-\d+\b', '', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Animations removed.")
