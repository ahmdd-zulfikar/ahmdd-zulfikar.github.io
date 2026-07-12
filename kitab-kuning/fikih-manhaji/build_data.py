import json
import re

text_data = [
    {
        'type': 'title',
        'ar': 'الصلاة',
        'id': 'Shalat',
        'words': [('الصلاة', 'Shalat', 'ص ل ي', 'Ibadah khusus, secara etimologi berarti doa.')]
    },
    {
        'type': 'heading',
        'ar': 'معنى الصلاة :',
        'id': 'Makna Shalat :',
        'words': [
            ('معنى', 'Makna/Arti', 'ع ن ي', ''),
            ('الصلاة', 'Shalat', 'ص ل ي', ''),
            (':', ':', '', '')
        ]
    },
    {
        'type': 'paragraph',
        'ar': 'تطلق كلمة الصلاة في اللغة العربية على الدعاء بخير. قال الله تعالى: ﴿وَصَلِّ عَلَيْهِمْ إِنَّ صَلَاتَكَ سَكَنٌ لَّهُمْ﴾ (سورة التوبة: الآية 103). أي ادع الله لهم بالمغفرة.',
        'id': 'Kata shalat dalam bahasa Arab digunakan untuk makna mendoakan kebaikan. Allah Ta\'ala berfirman: "Dan mendoalah untuk mereka. Sesungguhnya doa kamu itu (menjadi) ketenteraman jiwa bagi mereka." (Surat At-Taubah: Ayat 103). Artinya, berdoalah kepada Allah untuk memohonkan ampunan bagi mereka.',
        'words': [
            ('تطلق', 'Digunakan/Diucapkan', 'ط ل ق', ''),
            ('كلمة', 'Kata', 'ك ل م', ''),
            ('الصلاة', 'Shalat', 'ص ل ي', ''),
            ('في', 'Di/Dalam', '', ''),
            ('اللغة', 'Bahasa', 'ل غ و', ''),
            ('العربية', 'Arab', 'ع ر ب', ''),
            ('على', 'Atas/Untuk', '', ''),
            ('الدعاء', 'Doa', 'د ع و', 'Memohon kepada Allah'),
            ('بخير.', 'Dengan kebaikan.', 'خ ي ر', ''),
            ('قال', 'Telah berfirman', 'ق و ل', ''),
            ('الله', 'Allah', '', ''),
            ('تعالى:', 'Yang Maha Tinggi:', 'ع ل و', ''),
            ('﴿وَصَلِّ', 'Dan berdoalah', 'ص ل ي', 'Fi\'il Amr (Kata kerja perintah)'),
            ('عَلَيْهِمْ', 'Untuk mereka', '', ''),
            ('إِنَّ', 'Sesungguhnya', '', ''),
            ('صَلَاتَكَ', 'Doamu', 'ص ل ي', ''),
            ('سَكَنٌ', 'Ketenteraman', 'س ك ن', ''),
            ('لَّهُمْ﴾', 'Bagi mereka﴾', '', ''),
            ('(سورة', '(Surat', 'س و ر', ''),
            ('التوبة:', 'At-Taubah:', 'ت و ب', ''),
            ('الآية', 'Ayat', 'أ ي ي', ''),
            ('103).', '103).', '', ''),
            ('أي', 'Yaitu/Artinya', '', ''),
            ('ادع', 'Berdoalah', 'د ع و', ''),
            ('الله', 'Kepada Allah', '', ''),
            ('لهم', 'Untuk mereka', '', ''),
            ('بالمغفرة.', 'Dengan ampunan.', 'غ ف ر', '')
        ]
    },
    {
        'type': 'heading',
        'ar': 'أما في اصطلاح الفقهاء: فتطلق كلمة الصلاة على أقوال وأفعال مخصوصة، تفتتح بالتكبير وتختتم بالتسليم. سميت صلاة لأنها تشتمل على الدعاء ولأنه الجزء الغالب فيها؛ إطلاقاً لاسم الجزء على الكل.',
        'id': 'Adapun menurut istilah ahli fikih: Kata shalat digunakan untuk perkataan dan perbuatan tertentu, yang diawali dengan takbir dan diakhiri dengan salam. Dinamakan shalat karena di dalamnya memuat doa dan karena doa adalah bagian yang dominan di dalamnya; hal ini merupakan penyebutan nama sebagian untuk makna keseluruhan.',
        'words': [
            ('أما', 'Adapun', '', ''),
            ('في', 'Di/Dalam', '', ''),
            ('اصطلاح', 'Istilah', 'ص ل ح', ''),
            ('الفقهاء:', 'Para ahli fikih:', 'ف ق ه', ''),
            ('فتطلق', 'Maka digunakan', 'ط ل ق', ''),
            ('كلمة', 'Kata', 'ك ل م', ''),
            ('الصلاة', 'Shalat', 'ص ل ي', ''),
            ('على', 'Untuk', '', ''),
            ('أقوال', 'Perkataan', 'ق و ل', 'Bentuk jamak dari Qaul'),
            ('وأفعال', 'Dan perbuatan', 'ف ع ل', 'Bentuk jamak dari Fi\'il'),
            ('مخصوصة،', 'Tertentu,', 'خ ص ص', ''),
            ('تفتتح', 'Diawali', 'ف ت ح', ''),
            ('بالتكبير', 'Dengan takbir', 'ك ب ر', 'Mengucapkan Allahu Akbar'),
            ('وتختتم', 'Dan diakhiri', 'خ ت م', ''),
            ('بالتسليم.', 'Dengan salam.', 'س ل م', 'Mengucapkan Assalamu\'alaikum'),
            ('سميت', 'Dinamakan', 'س م و', ''),
            ('صلاة', 'Shalat', 'ص ل ي', ''),
            ('لأنها', 'Karena ia', '', ''),
            ('تشتمل', 'Mencakup/Memuat', 'ش م ل', ''),
            ('على', 'Atas', '', ''),
            ('الدعاء', 'Doa', 'د ع و', ''),
            ('ولأنه', 'Dan karena ia (doa)', '', ''),
            ('الجزء', 'Bagian', 'ج ز أ', ''),
            ('الغالب', 'Yang dominan', 'غ ل ب', ''),
            ('فيها؛', 'Di dalamnya;', '', ''),
            ('إطلاقاً', 'Sebagai penyebutan', 'ط ل ق', ''),
            ('لاسم', 'Bagi nama', 'س م و', ''),
            ('الجزء', 'Sebagian', 'ج ز أ', ''),
            ('على', 'Atas', '', ''),
            ('الكل.', 'Keseluruhan.', 'ك ل ل', '')
        ]
    },
    {
        'type': 'heading',
        'ar': 'حكمتها :',
        'id': 'Hikmahnya :',
        'words': [
            ('حكمتها', 'Hikmahnya', 'ح ك م', ''),
            (':', ':', '', '')
        ]
    },
    {
        'type': 'paragraph',
        'ar': 'للصلاة حكم وأسرار كثيرة نلخصها فيما يلي :',
        'id': 'Shalat memiliki banyak hikmah dan rahasia yang kami ringkas sebagai berikut :',
        'words': [
            ('للصلاة', 'Bagi shalat', 'ص ل ي', ''),
            ('حكم', 'Banyak hikmah', 'ح ك م', 'Jamak dari Hikmah'),
            ('وأسرار', 'Dan rahasia', 'س ر ر', 'Jamak dari Sirr'),
            ('كثيرة', 'Yang banyak', 'ك ث ر', ''),
            ('نلخصها', 'Kami meringkasnya', 'ل خ ص', ''),
            ('فيما', 'Pada apa yang', '', ''),
            ('يلي', 'Berikut ini', 'و ل ي', ''),
            (':', ':', '', '')
        ]
    },
    {
        'type': 'paragraph',
        'ar': 'أولاً: أن ينتبه الإنسان إلى هويته الحقيقية، وهي أنه عبد مملوك لله عز وجل، ثم أن يظل متذكراً لها، بحيث كلما أنسته مشاغل الدنيا وعلاقاته بالآخرين هذه الحقيقة جاءت الصلاة فذكرته من جديد بأنه عبد مملوك لله عز وجل.',
        'id': 'Pertama: Agar manusia menyadari identitas aslinya, yaitu bahwa ia adalah hamba yang dimiliki oleh Allah Azza wa Jalla. Kemudian agar ia selalu mengingatnya, sehingga setiap kali kesibukan dunia dan hubungannya dengan orang lain membuatnya lupa akan hakikat ini, datanglah shalat untuk mengingatkannya kembali bahwa ia adalah hamba yang dimiliki oleh Allah Azza wa Jalla.',
        'words': [
            ('أولاً:', 'Pertama:', 'أ و ل', ''),
            ('أن', 'Bahwa/Agar', '', ''),
            ('ينتبه', 'Menyadari', 'ن ب ه', ''),
            ('الإنسان', 'Manusia', 'أ ن س', ''),
            ('إلى', 'Kepada/Akan', '', ''),
            ('هويته', 'Identitasnya', 'ه و ي', ''),
            ('الحقيقية،', 'Yang hakiki/asli,', 'ح ق ق', ''),
            ('وهي', 'Dan ia adalah', '', ''),
            ('أنه', 'Bahwa dia', '', ''),
            ('عبد', 'Seorang hamba', 'ع ب د', ''),
            ('مملوك', 'Yang dimiliki', 'م ل ك', ''),
            ('لله', 'Bagi Allah', '', ''),
            ('عز', 'Maha Perkasa', 'ع ز ز', ''),
            ('وجل،', 'Dan Maha Agung,', 'ج ل ل', ''),
            ('ثم', 'Kemudian', '', ''),
            ('أن', 'Agar', '', ''),
            ('يظل', 'Ia tetap/selalu', 'ظ ل ل', ''),
            ('متذكراً', 'Mengingat', 'ذ ك ر', ''),
            ('لها،', 'Kepadanya (identitas),', '', ''),
            ('بحيث', 'Sehingga', 'ح ي ث', ''),
            ('كلما', 'Setiap kali', 'ك ل ل', ''),
            ('أنسته', 'Membuatnya lupa', 'ن س ي', ''),
            ('مشاغل', 'Kesibukan', 'ش غ ل', ''),
            ('الدنيا', 'Dunia', 'د ن و', ''),
            ('وعلاقاته', 'Dan hubungannya', 'ع ل ق', ''),
            ('بالآخرين', 'Dengan orang lain', 'أ خ ر', ''),
            ('هذه', 'Ini', '', ''),
            ('الحقيقة', 'Hakikat/Kenyataan', 'ح ق ق', ''),
            ('جاءت', 'Datanglah', 'ج ي أ', ''),
            ('الصلاة', 'Shalat', 'ص ل ي', ''),
            ('فذكرته', 'Lalu mengingatkannya', 'ذ ك ر', ''),
            ('من', 'Dari', '', ''),
            ('جديد', 'Baru (kembali)', 'ج د د', ''),
            ('بأنه', 'Bahwasanya ia', '', ''),
            ('عبد', 'Hamba', 'ع ب د', ''),
            ('مملوك', 'Yang dimiliki', 'م ل ك', ''),
            ('لله', 'Oleh Allah', '', ''),
            ('عز', 'Maha Perkasa', 'ع ز ز', ''),
            ('وجل.', 'Dan Maha Agung.', 'ج ل ل', '')
        ]
    },
    {
        'type': 'paragraph',
        'ar': 'ثانياً: أن يستقر في نفس الإنسان أنه لا يوجد معين ومنعم حقيقي إلا الله عز وجل وإن كان يرى في الدنيا وسائط وأسباباً كثيرة يبدو - في الظاهر - أنها هي التي تعين وتنعم؛ ولكن الحقيقة أن الله سخرها جميعاً',
        'id': 'Kedua: Agar tertanam dalam jiwa manusia bahwa tidak ada penolong dan pemberi nikmat yang hakiki selain Allah Azza wa Jalla. Meskipun ia melihat di dunia banyak perantara dan sebab yang tampak secara lahiriah membantu dan memberi nikmat; akan tetapi hakikatnya Allah-lah yang menundukkan semuanya itu.',
        'words': [
            ('ثانياً:', 'Kedua:', 'ث ن ي', ''),
            ('أن', 'Agar', '', ''),
            ('يستقر', 'Tertanam/Menetap', 'ق ر ر', ''),
            ('في', 'Dalam', '', ''),
            ('نفس', 'Jiwa', 'ن ف س', ''),
            ('الإنسان', 'Manusia', 'أ ن س', ''),
            ('أنه', 'Bahwa sesungguhnya', '', ''),
            ('لا', 'Tidak', '', ''),
            ('يوجد', 'Ada/Ditemukan', 'و ج د', ''),
            ('معين', 'Penolong', 'ع و ن', ''),
            ('ومنعم', 'Dan Pemberi Nikmat', 'ن ع م', ''),
            ('حقيقي', 'Yang Hakiki', 'ح ق ق', ''),
            ('إلا', 'Kecuali', '', ''),
            ('الله', 'Allah', '', ''),
            ('عز', 'Maha Perkasa', 'ع ز ز', ''),
            ('وجل', 'Dan Maha Agung', 'ج ل ل', ''),
            ('وإن', 'Dan meskipun', '', ''),
            ('كان', 'Adanya (ia)', 'ك و ن', ''),
            ('يرى', 'Melihat', 'ر أ ي', ''),
            ('في', 'Di', '', ''),
            ('الدنيا', 'Dunia', 'د ن و', ''),
            ('وسائط', 'Perantara', 'و س ط', ''),
            ('وأسباباً', 'Dan sebab-sebab', 'س ب ب', ''),
            ('كثيرة', 'Yang banyak', 'ك ث ر', ''),
            ('يبدو', 'Tampak', 'ب د و', ''),
            ('-', '-', '', ''),
            ('في', 'Pada', '', ''),
            ('الظاهر', 'Sisi lahiriah', 'ظ ه ر', ''),
            ('-', '-', '', ''),
            ('أنها', 'Bahwa ia (sebab)', '', ''),
            ('هي', 'Dialah', '', ''),
            ('التي', 'Yang', '', ''),
            ('تعين', 'Menolong', 'ع و ن', ''),
            ('وتنعم؛', 'Dan memberi nikmat;', 'ن ع م', ''),
            ('ولكن', 'Akan tetapi', '', ''),
            ('الحقيقة', 'Hakikatnya', 'ح ق ق', ''),
            ('أن', 'Bahwa', '', ''),
            ('الله', 'Allah-lah', '', ''),
            ('سخرها', 'Yang menundukkannya', 'س خ ر', ''),
            ('جميعاً', 'Semuanya', 'ج م ع', '')
        ]
    }
]

blocks = []
for item in text_data:
    words_arr = []
    for w_text, w_trans, w_root, w_expl in item['words']:
        words_arr.append({
            'text': w_text,
            'translation': w_trans,
            'root': w_root,
            'explanation': w_expl
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
print('data.js updated with full translations.')
