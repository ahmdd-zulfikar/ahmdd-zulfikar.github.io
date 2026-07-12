import json
import re

text_data = [
    {
        'type': 'title',
        'ar': 'الصلاة',
        'id': 'Shalat',
        'words': [('الصلاة', 'Shalat', 'ص ل ي', 'Ibadah khusus, secara etimologi berarti doa.', '', '', 'Mubtada', '')]
    },
    {
        'type': 'heading',
        'ar': 'معنى الصلاة :',
        'id': 'Makna Shalat :',
        'words': [
            ('معنى', 'Makna/Arti', 'ع ن ي', '', '', '', 'Khabar', ''),
            ('الصلاة', 'Shalat', 'ص ل ي', '', '', '', 'Mudhaf Ilaih', ''),
            (':', ':', '', '', '', '', '', '')
        ]
    },
    {
        'type': 'paragraph',
        'ar': 'تطلق كلمة الصلاة في اللغة العربية على الدعاء بخير. قال الله تعالى: ﴿وَصَلِّ عَلَيْهِمْ إِنَّ صَلَاتَكَ سَكَنٌ لَّهُمْ﴾ (سورة التوبة: الآية 103). أي ادع الله لهم بالمغفرة.',
        'id': 'Kata shalat dalam bahasa Arab digunakan untuk makna mendoakan kebaikan. Allah Ta\'ala berfirman: "Dan mendoalah untuk mereka. Sesungguhnya doa kamu itu (menjadi) ketenteraman jiwa bagi mereka." (Surat At-Taubah: Ayat 103). Artinya, berdoalah kepada Allah untuk memohonkan ampunan bagi mereka.',
        'words': [
            ('تطلق', 'Digunakan/Diucapkan', 'ط ل ق', '', '', '', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mujarrad'),
            ('كلمة', 'Kata', 'ك ل م', '', '', '', 'Na\'ib Fa\'il', ''),
            ('الصلاة', 'Shalat', 'ص ل ي', '', '', '', 'Mudhaf Ilaih', ''),
            ('في', 'Di/Dalam', '', '', '', '', 'Huruf Jar', ''),
            ('اللغة', 'Bahasa', 'ل غ و', '', '', '', 'Majrur', ''),
            ('العربية', 'Arab', 'ع ر ب', '', '', '', 'Na\'at', ''),
            ('على', 'Atas/Untuk', '', '', '', '', 'Huruf Jar', ''),
            ('الدعاء', 'Doa', 'د ع و', 'Memohon kepada Allah', '', '', 'Majrur', ''),
            ('بخير.', 'Dengan kebaikan.', 'خ ي ر', '', 'Baa (huruf jar) bersambung dengan kata khair', '', 'Jar Majrur', ''),
            ('قال', 'Telah berfirman', 'ق و ل', '', '', '', 'Fi\'il Madhi', 'Tsulasi Mujarrad'),
            ('الله', 'Allah', '', '', '', '', 'Fa\'il', ''),
            ('تعالى:', 'Yang Maha Tinggi:', 'ع ل و', '', '', '', 'Fi\'il Madhi (Haal)', 'Tsulasi Mazid'),
            ('﴿وَصَلِّ', 'Dan berdoalah', 'ص ل ي', 'Fi\'il Amr', 'Wawu (athaf) bersambung dengan fi\'il amr sholli', '', 'Fi\'il Amr', 'Tsulasi Mazid'),
            ('عَلَيْهِمْ', 'Untuk mereka', '', '', 'Huruf jar (ala) bersambung dengan dhamir (hum)', 'Dhamir (hum) merujuk pada kaum muslimin', 'Jar Majrur', ''),
            ('إِنَّ', 'Sesungguhnya', '', '', '', '', 'Amil Nawasikh', ''),
            ('صَلَاتَكَ', 'Doamu', 'ص ل ي', '', 'Kata (shalah) bersambung dengan dhamir muttasil (ka)', 'Dhamir (ka) merujuk pada Nabi Muhammad SAW', 'Isim Inna', ''),
            ('سَكَنٌ', 'Ketenteraman', 'س ك ن', '', '', '', 'Khabar Inna', ''),
            ('لَّهُمْ﴾', 'Bagi mereka﴾', '', '', 'Huruf lam (jar) bersambung dengan dhamir (hum)', 'Dhamir (hum) merujuk pada kaum muslimin', 'Jar Majrur', ''),
            ('(سورة', '(Surat', 'س و ر', '', '', '', 'Khabar dari mubtada mahdzuf', ''),
            ('التوبة:', 'At-Taubah:', 'ت و ب', '', '', '', 'Mudhaf Ilaih', ''),
            ('الآية', 'Ayat', 'أ ي ي', '', '', '', 'Badal', ''),
            ('103).', '103).', '', '', '', '', '', ''),
            ('أي', 'Yaitu/Artinya', '', '', '', '', 'Huruf Tafsir', ''),
            ('ادع', 'Berdoalah', 'د ع و', '', '', '', 'Fi\'il Amr', 'Tsulasi Mujarrad'),
            ('الله', 'Kepada Allah', '', '', '', '', 'Maf\'ul Bih', ''),
            ('لهم', 'Untuk mereka', '', '', 'Lam (jar) bersambung dengan dhamir hum', 'Merujuk pada kaum muslimin', 'Jar Majrur', ''),
            ('بالمغفرة.', 'Dengan ampunan.', 'غ ف ر', '', 'Baa (jar) bersambung dengan isim al-maghfirah', '', 'Jar Majrur', '')
        ]
    },
    {
        'type': 'heading',
        'ar': 'أما في اصطلاح الفقهاء: فتطلق كلمة الصلاة على أقوال وأفعال مخصوصة، تفتتح بالتكبير وتختتم بالتسليم. سميت صلاة لأنها تشتمل على الدعاء ولأنه الجزء الغالب فيها؛ إطلاقاً لاسم الجزء على الكل.',
        'id': 'Adapun menurut istilah ahli fikih: Kata shalat digunakan untuk perkataan dan perbuatan tertentu, yang diawali dengan takbir dan diakhiri dengan salam. Dinamakan shalat karena di dalamnya memuat doa dan karena doa adalah bagian yang dominan di dalamnya; hal ini merupakan penyebutan nama sebagian untuk makna keseluruhan.',
        'words': [
            ('أما', 'Adapun', '', '', '', '', 'Huruf Syarat', ''),
            ('في', 'Di/Dalam', '', '', '', '', 'Huruf Jar', ''),
            ('اصطلاح', 'Istilah', 'ص ل ح', '', '', '', 'Majrur', ''),
            ('الفقهاء:', 'Para ahli fikih:', 'ف ق ه', '', '', '', 'Mudhaf Ilaih', ''),
            ('فتطلق', 'Maka digunakan', 'ط ل ق', '', 'Fa (jawab) bersambung dengan fi\'il tutlaqu', '', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mujarrad'),
            ('كلمة', 'Kata', 'ك ل م', '', '', '', 'Na\'ib Fa\'il', ''),
            ('الصلاة', 'Shalat', 'ص ل ي', '', '', '', 'Mudhaf Ilaih', ''),
            ('على', 'Untuk', '', '', '', '', 'Huruf Jar', ''),
            ('أقوال', 'Perkataan', 'ق و ل', 'Bentuk jamak dari Qaul', '', '', 'Majrur', ''),
            ('وأفعال', 'Dan perbuatan', 'ف ع ل', 'Bentuk jamak dari Fi\'il', 'Wawu (athaf) bersambung dengan isim af\'al', '', 'Ma\'thuf', ''),
            ('مخصوصة،', 'Tertentu,', 'خ ص ص', '', '', '', 'Na\'at', ''),
            ('تفتتح', 'Diawali', 'ف ت ح', '', '', '', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mazid (Ifta\'ala)'),
            ('بالتكبير', 'Dengan takbir', 'ك ب ر', 'Mengucapkan Allahu Akbar', 'Baa (jar) bersambung dengan isim at-takbir', '', 'Jar Majrur', ''),
            ('وتختتم', 'Dan diakhiri', 'خ ت م', '', 'Wawu (athaf) bersambung dengan fi\'il', '', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mazid (Ifta\'ala)'),
            ('بالتسليم.', 'Dengan salam.', 'س ل م', 'Mengucapkan Assalamu\'alaikum', 'Baa (jar) bersambung dengan isim at-taslim', '', 'Jar Majrur', ''),
            ('سميت', 'Dinamakan', 'س م و', '', '', '', 'Fi\'il Madhi Majhul', 'Tsulasi Mazid'),
            ('صلاة', 'Shalat', 'ص ل ي', '', '', '', 'Na\'ib Fa\'il / Maf\'ul Tsani', ''),
            ('لأنها', 'Karena ia', '', '', 'Huruf Inna dan Lam bersambung dengan Dhamir ha', 'Merujuk pada As-Shalah', 'Amil Nawasikh', ''),
            ('تشتمل', 'Mencakup/Memuat', 'ش م ل', '', '', '', 'Fi\'il Mudhari\'', 'Tsulasi Mazid (Ifta\'ala)'),
            ('على', 'Atas', '', '', '', '', 'Huruf Jar', ''),
            ('الدعاء', 'Doa', 'د ع و', '', '', '', 'Majrur', ''),
            ('ولأنه', 'Dan karena ia (doa)', '', '', 'Wawu, Lam, Inna bersambung Dhamir hu', 'Merujuk pada Ad-Du\'a', 'Amil Nawasikh', ''),
            ('الجزء', 'Bagian', 'ج ز أ', '', '', '', 'Khabar Inna', ''),
            ('الغالب', 'Yang dominan', 'غ ل ب', '', '', '', 'Na\'at', ''),
            ('فيها؛', 'Di dalamnya;', '', '', 'Huruf fii bersambung dhamir ha', 'Merujuk pada As-Shalah', 'Jar Majrur', ''),
            ('إطلاقاً', 'Sebagai penyebutan', 'ط ل ق', '', '', '', 'Maf\'ul Mutlaq / Maf\'ul Li Ajlih', ''),
            ('لاسم', 'Bagi nama', 'س م و', '', 'Huruf lam (jar) bersambung dengan isim', '', 'Jar Majrur', ''),
            ('الجزء', 'Sebagian', 'ج ز أ', '', '', '', 'Mudhaf Ilaih', ''),
            ('على', 'Atas', '', '', '', '', 'Huruf Jar', ''),
            ('الكل.', 'Keseluruhan.', 'ك ل ل', '', '', '', 'Majrur', '')
        ]
    }
]

blocks = []
for item in text_data:
    words_arr = []
    for w_text, w_trans, w_root, w_expl, w_joined, w_pronoun, w_irab, w_verb in item['words']:
        words_arr.append({
            'text': w_text,
            'translation': w_trans,
            'root': w_root,
            'explanation': w_expl,
            'joined_explanation': w_joined,
            'pronoun_ref': w_pronoun,
            'irab': w_irab,
            'verb_type': w_verb
        })
    blocks.append({
        'type': item['type'],
        'ar': item['ar'],
        'id': item['id'],
        'words': words_arr
    })

pages = [
    {
        'pageNumber': 99,
        'blocks': blocks
    }
]

js_content = 'const fikihData = ' + json.dumps(pages, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('data.js updated with rich metadata.')
