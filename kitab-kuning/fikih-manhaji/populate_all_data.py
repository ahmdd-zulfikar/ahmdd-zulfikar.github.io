import json

pages = [
    {
        'pageNumber': 99,
        'blocks': [
            {
                'type': 'title',
                'ar': 'الصلاة',
                'id': 'Shalat',
                'words': [{'text': 'الصلاة', 'translation': 'Shalat', 'root': 'ص ل ي', 'explanation': 'Ibadah khusus, secara etimologi berarti doa.', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mubtada', 'verb_type': '-', 'fail_ref': '-'}]
            },
            {
                'type': 'heading',
                'ar': 'معنى الصلاة :',
                'id': 'Makna Shalat :',
                'words': [
                    {'text': 'معنى', 'translation': 'Makna/Arti', 'root': 'ع ن ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Khabar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الصلاة', 'translation': 'Shalat', 'root': 'ص ل ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': ':', 'translation': ':', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': '-', 'verb_type': '-', 'fail_ref': '-'}
                ]
            },
            {
                'type': 'paragraph',
                'ar': 'تطلق كلمة الصلاة في اللغة العربية على الدعاء بخير. قال الله تعالى: ﴿وَصَلِّ عَلَيْهِمْ إِنَّ صَلَاتَكَ سَكَنٌ لَّهُمْ﴾ (سورة التوبة: الآية 103). أي ادع الله لهم بالمغفرة.',
                'id': 'Kata shalat dalam bahasa Arab digunakan untuk makna mendoakan kebaikan. Allah Ta\'ala berfirman: "Dan mendoalah untuk mereka. Sesungguhnya doa kamu itu (menjadi) ketenteraman jiwa bagi mereka." (Surat At-Taubah: Ayat 103). Artinya, berdoalah kepada Allah untuk memohonkan ampunan bagi mereka.',
                'words': [
                    {'text': 'تطلق', 'translation': 'Digunakan/Diucapkan', 'root': 'ط ل ق', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\' Majhul', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Kalimat (kata shalat)'},
                    {'text': 'كلمة', 'translation': 'Kata', 'root': 'ك ل م', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'ib Fa\'il', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الصلاة', 'translation': 'Shalat', 'root': 'ص ل ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'في', 'translation': 'Di/Dalam', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'اللغة', 'translation': 'Bahasa', 'root': 'ل غ و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'العربية', 'translation': 'Arab', 'root': 'ع ر ب', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'على', 'translation': 'Atas/Untuk', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الدعاء', 'translation': 'Doa', 'root': 'د ع و', 'explanation': 'Memohon kepada Allah', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'بخير.', 'translation': 'Dengan kebaikan.', 'root': 'خ ي ر', 'explanation': '-', 'joined_explanation': 'Baa (huruf jar) bersambung dengan kata khair', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'قال', 'translation': 'Telah berfirman', 'root': 'ق و ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Allah'},
                    {'text': 'الله', 'translation': 'Allah', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fa\'il', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'تعالى:', 'translation': 'Yang Maha Tinggi:', 'root': 'ع ل و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi (Haal)', 'verb_type': 'Tsulasi Mazid', 'fail_ref': 'Dhamir Mustatir (Huwa) merujuk ke Allah'},
                    {'text': '﴿وَصَلِّ', 'translation': 'Dan berdoalah', 'root': 'ص ل ي', 'explanation': 'Fi\'il Amr', 'joined_explanation': 'Wawu (athaf) bersambung dengan fi\'il amr sholli', 'pronoun_ref': '-', 'irab': 'Fi\'il Amr', 'verb_type': 'Tsulasi Mazid', 'fail_ref': 'Dhamir Mustatir (Anta) merujuk ke Nabi Muhammad SAW'},
                    {'text': 'عَلَيْهِمْ', 'translation': 'Untuk mereka', 'root': '-', 'explanation': '-', 'joined_explanation': 'Huruf jar (ala) bersambung dengan dhamir (hum)', 'pronoun_ref': 'Dhamir (hum) merujuk pada kaum muslimin', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'إِنَّ', 'translation': 'Sesungguhnya', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'صَلَاتَكَ', 'translation': 'Doamu', 'root': 'ص ل ي', 'explanation': '-', 'joined_explanation': 'Kata (shalah) bersambung dengan dhamir muttasil (ka)', 'pronoun_ref': 'Dhamir (ka) merujuk pada Nabi Muhammad SAW', 'irab': 'Isim Inna', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'سَكَنٌ', 'translation': 'Ketenteraman', 'root': 'س ك ن', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Khabar Inna', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لَّهُمْ﴾', 'translation': 'Bagi mereka﴾', 'root': '-', 'explanation': '-', 'joined_explanation': 'Huruf lam (jar) bersambung dengan dhamir (hum)', 'pronoun_ref': 'Dhamir (hum) merujuk pada kaum muslimin', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': '(سورة', 'translation': '(Surat', 'root': 'س و ر', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Khabar dari mubtada mahdzuf', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'التوبة:', 'translation': 'At-Taubah:', 'root': 'ت و ب', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الآية', 'translation': 'Ayat', 'root': 'أ ي ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Badal', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': '103).', 'translation': '103).', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': '-', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أي', 'translation': 'Yaitu/Artinya', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Tafsir', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'ادع', 'translation': 'Berdoalah', 'root': 'د ع و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Amr', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Dhamir Mustatir (Anta) merujuk ke Nabi Muhammad SAW'},
                    {'text': 'الله', 'translation': 'Kepada Allah', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Maf\'ul Bih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لهم', 'translation': 'Untuk mereka', 'root': '-', 'explanation': '-', 'joined_explanation': 'Lam (jar) bersambung dengan dhamir hum', 'pronoun_ref': 'Merujuk pada kaum muslimin', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'بالمغفرة.', 'translation': 'Dengan ampunan.', 'root': 'غ ف ر', 'explanation': '-', 'joined_explanation': 'Baa (jar) bersambung dengan isim al-maghfirah', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'}
                ]
            },
            {
                'type': 'paragraph',
                'ar': 'أما في اصطلاح الفقهاء: فتطلق كلمة الصلاة على أقوال وأفعال مخصوصة، تفتتح بالتكبير وتختتم بالتسليم. سميت صلاة لأنها تشتمل على الدعاء ولأنه الجزء الغالب فيها؛ إطلاقاً لاسم الجزء على الكل.',
                'id': 'Adapun menurut istilah ahli fikih: Kata shalat digunakan untuk perkataan dan perbuatan tertentu, yang diawali dengan takbir dan diakhiri dengan salam. Dinamakan shalat karena di dalamnya memuat doa dan karena doa adalah bagian yang dominan di dalamnya; hal ini merupakan penyebutan nama sebagian untuk makna keseluruhan.',
                'words': [
                    {'text': 'أما', 'translation': 'Adapun', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Syarat', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'في', 'translation': 'Di/Dalam', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'اصطلاح', 'translation': 'Istilah', 'root': 'ص ل ح', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الفقهاء:', 'translation': 'Para ahli fikih:', 'root': 'ف ق ه', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'فتطلق', 'translation': 'Maka digunakan', 'root': 'ط ل ق', 'explanation': '-', 'joined_explanation': 'Fa (jawab) bersambung dengan fi\'il tutlaqu', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\' Majhul', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Kalimat (kata shalat)'},
                    {'text': 'كلمة', 'translation': 'Kata', 'root': 'ك ل م', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'ib Fa\'il', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الصلاة', 'translation': 'Shalat', 'root': 'ص ل ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'على', 'translation': 'Untuk', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أقوال', 'translation': 'Perkataan', 'root': 'ق و ل', 'explanation': 'Bentuk jamak dari Qaul', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'وأفعال', 'translation': 'Dan perbuatan', 'root': 'ف ع ل', 'explanation': 'Bentuk jamak dari Fi\'il', 'joined_explanation': 'Wawu (athaf) bersambung dengan isim af\'al', 'pronoun_ref': '-', 'irab': 'Ma\'thuf', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'مخصوصة،', 'translation': 'Tertentu,', 'root': 'خ ص ص', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'تفتتح', 'translation': 'Diawali', 'root': 'ف ت ح', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\' Majhul', 'verb_type': 'Tsulasi Mazid (Ifta\'ala)', 'fail_ref': 'Dhamir Mustatir (Hiya) merujuk ke Shalat'},
                    {'text': 'بالتكبير', 'translation': 'Dengan takbir', 'root': 'ك ب ر', 'explanation': 'Mengucapkan Allahu Akbar', 'joined_explanation': 'Baa (jar) bersambung dengan isim at-takbir', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'وتختتم', 'translation': 'Dan diakhiri', 'root': 'خ ت م', 'explanation': '-', 'joined_explanation': 'Wawu (athaf) bersambung dengan fi\'il', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\' Majhul', 'verb_type': 'Tsulasi Mazid (Ifta\'ala)', 'fail_ref': 'Dhamir Mustatir (Hiya) merujuk ke Shalat'},
                    {'text': 'بالتسليم.', 'translation': 'Dengan salam.', 'root': 'س ل م', 'explanation': 'Mengucapkan Assalamu\'alaikum', 'joined_explanation': 'Baa (jar) bersambung dengan isim at-taslim', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'سميت', 'translation': 'Dinamakan', 'root': 'س م و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi Majhul', 'verb_type': 'Tsulasi Mazid', 'fail_ref': 'Dhamir Mustatir (Hiya) merujuk ke Shalat'},
                    {'text': 'صلاة', 'translation': 'Shalat', 'root': 'ص ل ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'ib Fa\'il / Maf\'ul Tsani', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لأنها', 'translation': 'Karena ia', 'root': '-', 'explanation': '-', 'joined_explanation': 'Huruf Inna dan Lam bersambung dengan Dhamir ha', 'pronoun_ref': 'Merujuk pada As-Shalah', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'تشتمل', 'translation': 'Mencakup/Memuat', 'root': 'ش م ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\'', 'verb_type': 'Tsulasi Mazid (Ifta\'ala)', 'fail_ref': 'Dhamir Mustatir (Hiya) merujuk ke Shalat'},
                    {'text': 'على', 'translation': 'Atas', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الدعاء', 'translation': 'Doa', 'root': 'د ع و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'ولأنه', 'translation': 'Dan karena ia (doa)', 'root': '-', 'explanation': '-', 'joined_explanation': 'Wawu, Lam, Inna bersambung Dhamir hu', 'pronoun_ref': 'Merujuk pada Ad-Du\'a', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الجزء', 'translation': 'Bagian', 'root': 'ج ز أ', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Khabar Inna', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الغالب', 'translation': 'Yang dominan', 'root': 'غ ل ب', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'فيها؛', 'translation': 'Di dalamnya;', 'root': '-', 'explanation': '-', 'joined_explanation': 'Huruf fii bersambung dhamir ha', 'pronoun_ref': 'Merujuk pada As-Shalah', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'إطلاقاً', 'translation': 'Sebagai penyebutan', 'root': 'ط ل ق', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Maf\'ul Mutlaq / Maf\'ul Li Ajlih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لاسم', 'translation': 'Bagi nama', 'root': 'س م و', 'explanation': '-', 'joined_explanation': 'Huruf lam (jar) bersambung dengan isim', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الجزء', 'translation': 'Sebagian', 'root': 'ج ز أ', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'على', 'translation': 'Atas', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الكل.', 'translation': 'Keseluruhan.', 'root': 'ك ل ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'}
                ]
            },
            {
                'type': 'heading',
                'ar': 'حكمتها :',
                'id': 'Hikmahnya :',
                'words': [
                    {'text': 'حكمتها', 'translation': 'Hikmahnya', 'root': 'ح ك م', 'explanation': '-', 'joined_explanation': 'Bersambung dengan dhamir ha', 'pronoun_ref': 'Merujuk ke Shalat', 'irab': 'Mubtada Muakhkhar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': ':', 'translation': ':', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': '-', 'verb_type': '-', 'fail_ref': '-'}
                ]
            },
            {
                'type': 'paragraph',
                'ar': 'للصلاة حكم وأسرار كثيرة نلخصها فيما يلي :',
                'id': 'Shalat memiliki banyak hikmah dan rahasia yang kami ringkas sebagai berikut :',
                'words': [
                    {'text': 'للصلاة', 'translation': 'Bagi shalat', 'root': 'ص ل ي', 'explanation': '-', 'joined_explanation': 'Huruf lam jar bersambung isim shalat', 'pronoun_ref': '-', 'irab': 'Jar Majrur (Khabar Muqaddam)', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'حكم', 'translation': 'Banyak hikmah', 'root': 'ح ك م', 'explanation': 'Jamak dari Hikmah', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mubtada Muakhkhar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'وأسرار', 'translation': 'Dan rahasia', 'root': 'س ر ر', 'explanation': 'Jamak dari Sirr', 'joined_explanation': 'Wawu athaf bersambung asrar', 'pronoun_ref': '-', 'irab': 'Ma\'thuf', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'كثيرة', 'translation': 'Yang banyak', 'root': 'ك ث ر', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'نلخصها', 'translation': 'Kami meringkasnya', 'root': 'ل خ ص', 'explanation': '-', 'joined_explanation': 'Bersambung dhamir ha', 'pronoun_ref': 'Dhamir ha merujuk ke hikam wa asrar', 'irab': 'Fi\'il mudhari\'', 'verb_type': 'Tsulasi Mazid', 'fail_ref': 'Dhamir mustatir (Nahnu)'},
                    {'text': 'فيما', 'translation': 'Pada apa yang', 'root': '-', 'explanation': '-', 'joined_explanation': 'Huruf fii bersambung isim maushul ma', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'يلي', 'translation': 'Berikut ini', 'root': 'و ل ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il mudhari\'', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Dhamir mustatir (Huwa) merujuk ke ma'},
                    {'text': ':', 'translation': ':', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': '-', 'verb_type': '-', 'fail_ref': '-'}
                ]
            },
            {
                'type': 'paragraph',
                'ar': 'أولاً: أن ينتبه الإنسان إلى هويته الحقيقية، وهي أنه عبد مملوك لله عز وجل، ثم أن يظل متذكراً لها، بحيث كلما أنسته مشاغل الدنيا وعلاقاته بالآخرين هذه الحقيقة جاءت الصلاة فذكرته من جديد بأنه عبد مملوك لله عز وجل.',
                'id': 'Pertama: Agar manusia menyadari identitas aslinya, yaitu bahwa ia adalah hamba yang dimiliki oleh Allah Azza wa Jalla. Kemudian agar ia selalu mengingatnya, sehingga setiap kali kesibukan dunia dan hubungannya dengan orang lain membuatnya lupa akan hakikat ini, datanglah shalat untuk mengingatkannya kembali bahwa ia adalah hamba yang dimiliki oleh Allah Azza wa Jalla.',
                'words': [
                    {'text': 'أولاً:', 'translation': 'Pertama:', 'root': 'أ و ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Hal / Maf\'ul Muthlaq', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أن', 'translation': 'Bahwa/Agar', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Mashdariyyah', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'ينتبه', 'translation': 'Menyadari', 'root': 'ن ب ه', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il mudhari\' manshub', 'verb_type': 'Tsulasi Mazid (Ifta\'ala)', 'fail_ref': 'Al-Insan (Manusia)'},
                    {'text': 'الإنسان', 'translation': 'Manusia', 'root': 'أ ن س', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fa\'il', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'إلى', 'translation': 'Kepada/Akan', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'هويته', 'translation': 'Identitasnya', 'root': 'ه و ي', 'explanation': '-', 'joined_explanation': 'Bersambung dhamir hu', 'pronoun_ref': 'Dhamir hu merujuk ke al-insan', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الحقيقية،', 'translation': 'Yang hakiki/asli,', 'root': 'ح ق ق', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'وهي', 'translation': 'Dan ia adalah', 'root': '-', 'explanation': '-', 'joined_explanation': 'Wawu athaf bersambung dhamir hiya', 'pronoun_ref': 'Dhamir hiya merujuk ke huwiyah', 'irab': 'Mubtada\'', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أنه', 'translation': 'Bahwa dia', 'root': '-', 'explanation': '-', 'joined_explanation': 'Inna bersambung dhamir hu', 'pronoun_ref': 'Dhamir hu merujuk ke al-insan', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'عبد', 'translation': 'Seorang hamba', 'root': 'ع ب د', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Khabar Inna', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'مملوك', 'translation': 'Yang dimiliki', 'root': 'م ل ك', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لله', 'translation': 'Bagi Allah', 'root': '-', 'explanation': '-', 'joined_explanation': 'Lam jar bersambung lafadz Allah', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'عز', 'translation': 'Maha Perkasa', 'root': 'ع ز ز', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Allah'},
                    {'text': 'وجل،', 'translation': 'Dan Maha Agung,', 'root': 'ج ل ل', 'explanation': '-', 'joined_explanation': 'Wawu athaf bersambung fiil jalla', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Allah'},
                    {'text': 'ثم', 'translation': 'Kemudian', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Athaf', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أن', 'translation': 'Agar', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Mashdariyyah', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'يظل', 'translation': 'Ia tetap/selalu', 'root': 'ظ ل ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il mudhari\' naqish', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Al-Insan (Manusia)'},
                    {'text': 'متذكراً', 'translation': 'Mengingat', 'root': 'ذ ك ر', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Khabar yadhallu', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لها،', 'translation': 'Kepadanya (identitas),', 'root': '-', 'explanation': '-', 'joined_explanation': 'Lam jar bersambung dhamir ha', 'pronoun_ref': 'Dhamir ha merujuk ke huwiyah', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'بحيث', 'translation': 'Sehingga', 'root': 'ح ي ث', 'explanation': '-', 'joined_explanation': 'Baa jar bersambung haitsu', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'كلما', 'translation': 'Setiap kali', 'root': 'ك ل ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Syarat', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أنسته', 'translation': 'Membuatnya lupa', 'root': 'ن س ي', 'explanation': '-', 'joined_explanation': 'Bersambung dhamir hu', 'pronoun_ref': 'Dhamir hu merujuk ke al-insan', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mazid (Af\'ala)', 'fail_ref': 'Masyaghil (Kesibukan)'},
                    {'text': 'مشاغل', 'translation': 'Kesibukan', 'root': 'ش غ ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fa\'il', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الدنيا', 'translation': 'Dunia', 'root': 'د ن و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'وعلاقاته', 'translation': 'Dan hubungannya', 'root': 'ع ل ق', 'explanation': '-', 'joined_explanation': 'Wawu athaf + isim + dhamir hu', 'pronoun_ref': 'Dhamir hu merujuk ke al-insan', 'irab': 'Ma\'thuf', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'بالآخرين', 'translation': 'Dengan orang lain', 'root': 'أ خ ر', 'explanation': '-', 'joined_explanation': 'Baa jar bersambung al-akharin', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'هذه', 'translation': 'Ini', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Isim Isyarah (Maf\'ul bih)', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الحقيقة', 'translation': 'Hakikat/Kenyataan', 'root': 'ح ق ق', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Badal', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'جاءت', 'translation': 'Datanglah', 'root': 'ج ي أ', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'As-Shalah'},
                    {'text': 'الصلاة', 'translation': 'Shalat', 'root': 'ص ل ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fa\'il', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'فذكرته', 'translation': 'Lalu mengingatkannya', 'root': 'ذ ك ر', 'explanation': '-', 'joined_explanation': 'Fa athaf + fiil + dhamir hu', 'pronoun_ref': 'Dhamir hu merujuk ke al-insan', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mazid (Fa\'ala)', 'fail_ref': 'As-Shalah'},
                    {'text': 'من', 'translation': 'Dari', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'جديد', 'translation': 'Baru (kembali)', 'root': 'ج د د', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'بأنه', 'translation': 'Bahwasanya ia', 'root': '-', 'explanation': '-', 'joined_explanation': 'Baa jar + inna + dhamir hu', 'pronoun_ref': 'Dhamir hu merujuk ke al-insan', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'عبد', 'translation': 'Hamba', 'root': 'ع ب د', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Khabar Inna', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'مملوك', 'translation': 'Yang dimiliki', 'root': 'م ل ك', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لله', 'translation': 'Oleh Allah', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Jar Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'عز', 'translation': 'Maha Perkasa', 'root': 'ع ز ز', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Allah'},
                    {'text': 'وجل.', 'translation': 'Dan Maha Agung.', 'root': 'ج ل ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Allah'}
                ]
            },
            {
                'type': 'paragraph',
                'ar': 'ثانياً: أن يستقر في نفس الإنسان أنه لا يوجد معين ومنعم حقيقي إلا الله عز وجل وإن كان يرى في الدنيا وسائط وأسباباً كثيرة يبدو - في الظاهر - أنها هي التي تعين وتنعم؛ ولكن الحقيقة أن الله سخرها جميعاً',
                'id': 'Kedua: Agar tertanam dalam jiwa manusia bahwa tidak ada penolong dan pemberi nikmat yang hakiki selain Allah Azza wa Jalla. Meskipun ia melihat di dunia banyak perantara dan sebab yang tampak secara lahiriah membantu dan memberi nikmat; akan tetapi hakikatnya Allah-lah yang menundukkan semuanya itu.',
                'words': [
                    {'text': 'ثانياً:', 'translation': 'Kedua:', 'root': 'ث ن ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Hal / Maf\'ul Muthlaq', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أن', 'translation': 'Agar', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Mashdariyyah', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'يستقر', 'translation': 'Tertanam/Menetap', 'root': 'ق ر ر', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\'', 'verb_type': 'Tsulasi Mazid (Istaf\'ala)', 'fail_ref': 'Dhamir Mustatir (Huwa) merujuk ke keadaan'},
                    {'text': 'في', 'translation': 'Dalam', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'نفس', 'translation': 'Jiwa', 'root': 'ن ف س', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الإنسان', 'translation': 'Manusia', 'root': 'أ ن س', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mudhaf Ilaih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أنه', 'translation': 'Bahwa sesungguhnya', 'root': '-', 'explanation': '-', 'joined_explanation': 'Inna + dhamir hu', 'pronoun_ref': 'Dhamir hu (Dhamir Sya\'n)', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'لا', 'translation': 'Tidak', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Nafi', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'يوجد', 'translation': 'Ada/Ditemukan', 'root': 'و ج د', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\' Majhul', 'verb_type': 'Tsulasi Mujarrad (Majhul)', 'fail_ref': '-'},
                    {'text': 'معين', 'translation': 'Penolong', 'root': 'ع و ن', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'ib Fa\'il', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'ومنعم', 'translation': 'Dan Pemberi Nikmat', 'root': 'ن ع م', 'explanation': '-', 'joined_explanation': 'Wawu athaf + isim', 'pronoun_ref': '-', 'irab': 'Ma\'thuf', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'حقيقي', 'translation': 'Yang Hakiki', 'root': 'ح ق ق', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'إلا', 'translation': 'Kecuali', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Istitsna\'', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الله', 'translation': 'Allah', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Mustatsna / Badal', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'عز', 'translation': 'Maha Perkasa', 'root': 'ع ز ز', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Allah'},
                    {'text': 'وجل', 'translation': 'Dan Maha Agung', 'root': 'ج ل ل', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Allah'},
                    {'text': 'وإن', 'translation': 'Dan meskipun', 'root': '-', 'explanation': '-', 'joined_explanation': 'Wawu hal + in syarat', 'pronoun_ref': '-', 'irab': 'Huruf Syarat', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'كان', 'translation': 'Adanya (ia)', 'root': 'ك و ن', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Madhi Naqish', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Al-Insan'},
                    {'text': 'يرى', 'translation': 'Melihat', 'root': 'ر أ ي', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\'', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Al-Insan'},
                    {'text': 'في', 'translation': 'Di', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الدنيا', 'translation': 'Dunia', 'root': 'د ن و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'وسائط', 'translation': 'Perantara', 'root': 'و س ط', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Maf\'ul Bih', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'وأسباباً', 'translation': 'Dan sebab-sebab', 'root': 'س ب ب', 'explanation': '-', 'joined_explanation': 'Wawu athaf + isim', 'pronoun_ref': '-', 'irab': 'Ma\'thuf', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'كثيرة', 'translation': 'Yang banyak', 'root': 'ك ث ر', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Na\'at', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'يبدو', 'translation': 'Tampak', 'root': 'ب د و', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\'', 'verb_type': 'Tsulasi Mujarrad', 'fail_ref': 'Dhamir Mustatir (Huwa)'},
                    {'text': '-', 'translation': '-', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': '-', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'في', 'translation': 'Pada', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Huruf Jar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الظاهر', 'translation': 'Sisi lahiriah', 'root': 'ظ ه ر', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Majrur', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': '-', 'translation': '-', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': '-', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أنها', 'translation': 'Bahwa ia (sebab)', 'root': '-', 'explanation': '-', 'joined_explanation': 'Anna + dhamir ha', 'pronoun_ref': 'Dhamir ha merujuk ke wasa\'ith wa asbab', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'هي', 'translation': 'Dialah', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Dhamir Fashl / Mubtada', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'التي', 'translation': 'Yang', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Isim Maushul / Khabar', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'تعين', 'translation': 'Menolong', 'root': 'ع و ن', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\'', 'verb_type': 'Tsulasi Mazid (Af\'ala)', 'fail_ref': 'wasa\'ith wa asbab'},
                    {'text': 'وتنعم؛', 'translation': 'Dan memberi nikmat;', 'root': 'ن ع م', 'explanation': '-', 'joined_explanation': 'Wawu athaf + fiil', 'pronoun_ref': '-', 'irab': 'Fi\'il Mudhari\'', 'verb_type': 'Tsulasi Mazid (Af\'ala)', 'fail_ref': 'wasa\'ith wa asbab'},
                    {'text': 'ولكن', 'translation': 'Akan tetapi', 'root': '-', 'explanation': '-', 'joined_explanation': 'Wawu athaf + lakinna', 'pronoun_ref': '-', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الحقيقة', 'translation': 'Hakikatnya', 'root': 'ح ق ق', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Isim Lakinna', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'أن', 'translation': 'Bahwa', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Amil Nawasikh', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'الله', 'translation': 'Allah-lah', 'root': '-', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Isim Anna', 'verb_type': '-', 'fail_ref': '-'},
                    {'text': 'سخرها', 'translation': 'Yang menundukkannya', 'root': 'س خ ر', 'explanation': '-', 'joined_explanation': 'Bersambung dhamir ha', 'pronoun_ref': 'Dhamir ha merujuk ke wasa\'ith wa asbab', 'irab': 'Fi\'il Madhi', 'verb_type': 'Tsulasi Mazid (Fa\'ala)', 'fail_ref': 'Allah'},
                    {'text': 'جميعاً', 'translation': 'Semuanya', 'root': 'ج م ع', 'explanation': '-', 'joined_explanation': '-', 'pronoun_ref': '-', 'irab': 'Hal / Taukid', 'verb_type': '-', 'fail_ref': '-'}
                ]
            }
        ]
    }
]

js_content = 'const fikihData = ' + json.dumps(pages, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('data.js accurately fully populated for every word.')
