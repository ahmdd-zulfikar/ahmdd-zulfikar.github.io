import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

# Page 99 is index 0, Page 100 is index 1
page_99 = data[0]
page_100 = data[1]

# Pop the first block from page 100
first_block_100 = page_100['blocks'].pop(0)

# Get the last block of page 99
last_block_99 = page_99['blocks'][-1]

# Append the words
last_block_99['words'].extend(first_block_100['words'])

# Merge the text strings
last_block_99['ar'] += ' ' + first_block_100['ar']
last_block_99['id'] += ' ' + first_block_100['id']

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Moved first paragraph from page 100 to page 99.')
