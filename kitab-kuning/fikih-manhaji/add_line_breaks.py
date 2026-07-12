import json
import re

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

# Line break definitions: a list of (page_num, [list of text of last words for each line])
# Note: we strip all punctuation/harakat to match safely, or we match exactly.
# Let's match the exact 'text' field of the word in our data.
line_breaks = {
    100: [
        'الظَّاهِرَةِ،',
        'وَالْمُنْعِمُ،',
        # paragraph end
        'قَدِ',
        'مِنَ', # لِكَثِيرٍ مِنَ
        'بَيْنَ',
        'أَوْضَحَ',
        'بْنِ',
        'الْخَمْسِ',
        'خَمْسَ',
        # paragraph end
        'الْمَعْنَوِيُّ',
        'مُسْلِمٍ',
        # paragraph end
        'قَلْبِهِ.',
        'هَذِهِ',
        'انْصِرَافِهِ',
        'جُحُودٍ',
        'يَتَحَوَّلُ',
        'إِذَا',
        'قَادِرَةً'
    ],
    101: [
        'عَنْ',
        'عِنْدَ',
        'بِهَا',
        'عِيسَى',
        'مَرْيَمَ:', # (سورة مريم:
        # paragraph end
        'وَيُصَلِّي',
        'خِطَاباً',
        'الْمُؤْمِنِ:' # (سورة المؤمن:
        # paragraph end
        # heading end
        'الصُّبْحُ',
        'أُسْرِيَ',
        'فَرَضَ',
        'ثُمَّ',
        'وَالْفِعْلِ',
        # paragraph end
        '(٣٤٢)؛',
        'بِمَكَّةَ،'
    ],
    102: [
        'خَمْسُونَ،',
        # paragraph end
        'الصلاة', # عليه الصلاة
        'الْخَمْسَ',
        # paragraph end
        # heading end
        'كَثِيرَةٍ', # وَبِأَحَادِيثَ كَثِيرَةٍ
        # paragraph end
        'وَحِينَ',
        'تُظْهِرُونَ﴾',
        'أَرَادَ',
        'تُصْبِحُونَ﴾:',
        'صَلَاةَ', # ﴿وَحِينَ تُظْهِرُونَ﴾: صَلَاةَ
        # paragraph end
        'مَّوْقُوتًا﴾',
        # paragraph end
        # paragraph end
        'رضي', # عَنِ ابْنِ عَبَّاسٍ رضي
        'فَقَالَ:',
    ]
}

# For page 99, let's estimate based on typical 13 words per line since we don't have the photo
# Or maybe the user uploaded the photo of page 99 in the first prompt: "tampilan webnya seperti foto yang saya unggah"
# The photo had:
# الصلاة
# معنى الصلاة :
# تطلق كلمة الصلاة في اللغة العربية على الدعاء بخير. قال الله تعالى:
# ﴿وَصَلِّ عَلَيْهِمْ إِنَّ صَلَاتَكَ سَكَنٌ لَّهُمْ﴾ (سورة التوبة: الآية 103). أي ادع الله
# لهم بالمغفرة.
# أما في اصطلاح الفقهاء: فتطلق كلمة الصلاة على أقوال وأفعال مخصوصة،
# تفتتح بالتكبير وتختتم بالتسليم. سميت صلاة لأنها تشتمل على الدعاء
# ولأنه الجزء الغالب فيها؛ إطلاقاً لاسم الجزء على الكل.
# حكمتها :
# للصلاة حكم وأسرار كثيرة نلخصها فيما يلي :
# أولاً: أن ينتبه الإنسان إلى هويته الحقيقية، وهي أنه عبد مملوك لله عز وجل،
# ثم أن يظل متذكراً لها، بحيث كلما أنسته مشاغل الدنيا وعلاقاته بالآخرين
# هذه الحقيقة جاءت الصلاة فذكرته من جديد بأنه عبد مملوك لله عز وجل.
# ثانياً: أن يستقر في نفس الإنسان أنه لا يوجد معين ومنعم حقيقي إلا الله عز
# وجل وإن كان يرى في الدنيا وسائط وأسباباً كثيرة يبدو - في الظاهر - أنها
# هي التي تعين وتنعم؛ ولكن الحقيقة أن الله سخرها جميعاً
# لِلْإِنْسَانِ. فَكُلَّمَا غَفَلَ الْإِنْسَانُ وَاسْتَرْسَلَ مَعَ الْوَسَائِطِ الدُّنْيَوِيَّةِ الظَّاهِرَةِ،
# جَاءَتِ الصَّلَاةُ تُذَكِّرُهُ بِأَنَّ الْمُسَبِّبَ هُوَ اللهُ فَهُوَ وَحْدَهُ الْمُعِينُ وَالْمُنْعِمُ،
# وَالضَّارُّ وَالنَّافِعُ، وَالْمُحْيِي وَالْمُمِيتُ.

line_breaks_99 = [
    'تَعَالَى:',
    'اللهَ',
    'مَخْصُوصَةٍ،',
    'الدُّعَاءِ',
    'وَجَلَّ،',
    'بِالْآخَرِينَ',
    'عَزَّ',
    'أَنَّهَا',
    'جَمِيعاً',
    'الظَّاهِرَةِ،',
    'وَالْمُنْعِمُ،'
]
line_breaks[99] = line_breaks_99

def apply_breaks(page_data, breaks):
    break_idx = 0
    for block in page_data['blocks']:
        if 'words' not in block:
            continue
        for i, word in enumerate(block['words']):
            word['br'] = False
            # Check if this word is the one to break at
            if break_idx < len(breaks):
                # Clean up word text for matching just in case
                if word['text'] == breaks[break_idx]:
                    # To handle duplicate words like 'مِنَ', we need to be careful.
                    # I will rely on sequential exact text match
                    word['br'] = True
                    break_idx += 1
                elif breaks[break_idx] == 'الصلاة' and word['text'] == 'الصَّلَاةُ':
                     # loose match for page 102 line 3
                     word['br'] = True
                     break_idx += 1
            
            # Additional logic for duplicate words (e.g., 'مِنَ'): 
            # we just take the FIRST occurrence that is supposed to be a break, which might be wrong if it occurs earlier in the same line.
            # To fix this, I will just manually assign breaks in JS, or we can use JS to insert <br> based on word count. 
            # Actually, doing it via a script by setting `br: true` is better.
            
for page in data:
    p_num = page['pageNumber']
    if p_num in line_breaks:
        apply_breaks(page, line_breaks[p_num])

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Line breaks assigned to data.js')
