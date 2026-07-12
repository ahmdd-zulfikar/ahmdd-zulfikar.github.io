import json
import re

# We will load the existing data.js
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract json
json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

# Simple heuristic mapping for missing data to ensure it's not empty
for page in data:
    for block in page['blocks']:
        for word in block['words']:
            if not word.get('root'):
                word['root'] = '-'
            if not word.get('explanation'):
                word['explanation'] = '-'
            if not word.get('joined_explanation'):
                word['joined_explanation'] = '-'
            if not word.get('pronoun_ref'):
                word['pronoun_ref'] = '-'
            if not word.get('irab'):
                word['irab'] = '-'
            if not word.get('verb_type'):
                word['verb_type'] = '-'
                
            # Initialize fail_ref
            word['fail_ref'] = '-'
            
            # Very basic fail_ref injection for known verbs in the text
            text = word['text']
            if 'تطلق' in text or 'فتطلق' in text:
                word['fail_ref'] = 'Kalimat (kata shalat)'
            elif 'قال' in text:
                word['fail_ref'] = 'Allah'
            elif 'تعالى' in text:
                word['fail_ref'] = 'Dhamir Mustatir (Huwa) merujuk ke Allah'
            elif 'وصَلِّ' in text or 'ادع' in text:
                word['fail_ref'] = 'Dhamir Mustatir (Anta) merujuk ke Nabi Muhammad SAW'
            elif 'تفتتح' in text or 'تختتم' in text or 'تشتمل' in text or 'جاءت' in text:
                word['fail_ref'] = 'Dhamir Mustatir (Hiya) merujuk ke Shalat'
            elif 'سميت' in text:
                word['fail_ref'] = 'Dhamir Mustatir (Hiya) merujuk ke Shalat'
            elif 'ينتبه' in text or 'يستقر' in text or 'يظل' in text or 'يرى' in text:
                word['fail_ref'] = 'Al-Insan (Manusia)'
            elif 'أنسته' in text:
                word['fail_ref'] = 'Masyaghil (Kesibukan)'
            elif 'يبدو' in text:
                word['fail_ref'] = 'Dhamir Mustatir (Huwa) merujuk pada keadaan'
            elif 'تعين' in text or 'وتنعم' in text:
                word['fail_ref'] = 'Dhamir Mustatir (Hiya) merujuk pada perantara/sebab'
            elif 'سخرها' in text:
                word['fail_ref'] = 'Allah'

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('data.js updated with permanent fields and fail_ref.')
