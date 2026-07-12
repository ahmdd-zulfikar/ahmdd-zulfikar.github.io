import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_104 = []

def make_words(word_tuples, break_indices):
    words = []
    for i, t in enumerate(word_tuples):
        words.append({
            'text': t[0],
            'translation': t[1],
            'root': t[2],
            'explanation': t[3],
            'joined_explanation': t[4],
            'pronoun_ref': t[5],
            'irab': t[6],
            'verb_type': t[7],
            'fail_ref': t[8],
            'br': (i in break_indices)
        })
    return words

# Para 1 (Continuation of Hadith Ummu Aiman from page 103)
# Text:
# رَسُولُ اللهِ ﷺ قَالَ: «لَا تَتْرُكِي الصَّلَاةَ مُتَعَمِّداً، فَإِنَّهُ مَنْ تَرَكَ الصَّلَاةَ
# مُتَعَمِّداً فَقَدْ بَرِئَتْ مِنْهُ ذِمَّةُ اللَّهِ وَرَسُولِهِ». وَرُوِيَ مِثْلُهُ عَنْ مُعَاذٍ رضي الله
# عَنْهُ (٥/ ٢٣٨).
p1_words = [
    ('رَسُولَ', 'Rasul', 'ر س ل', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('قَالَ:', 'Telah bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi (Khabar Anna)', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«لَا', '«Janganlah', '-', '-', '-', '-', 'Laa Nahiyah', '-', '-'),
    ('تَتْرُكِي', 'Engkau tinggalkan', 'ت ر ك', '-', 'Bersambung Ya Muannats Mukhatabah', 'ya merujuk ke Ummu Aiman', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mujarrad', 'Engkau (Anti)'),
    ('الصَّلَاةَ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('مُتَعَمِّداً،', 'Dengan sengaja,', 'ع م د', '-', '-', '-', 'Hal', '-', '-'),
    ('فَإِنَّهُ', 'Maka sesungguhnya', '-', '-', 'Fa + Inna + hu', 'hu merujuk ke sya\'n (keadaan)', 'Amil Nawasikh', '-', '-'),
    ('مَنْ', 'Barangsiapa yang', '-', '-', '-', '-', 'Isim Syarat', '-', '-'),
    ('تَرَكَ', 'Telah meninggalkan', 'ت ر ك', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Man (Siapa saja)'),
    ('الصَّلَاةَ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('مُتَعَمِّداً', 'Dengan sengaja', 'ع م د', '-', '-', '-', 'Hal', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa (Jawab) + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('بَرِئَتْ', 'Telah lepas', 'ب ر أ', '-', 'Bersambung ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Dzimmah (Jaminan)'),
    ('مِنْهُ', 'Darinya', '-', '-', 'Min + hu', 'hu merujuk ke orang yang meninggalkan', 'Jar Majrur', '-', '-'),
    ('ذِمَّةُ', 'Jaminan perlindungan', 'ذ م م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('اللَّهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَرَسُولِهِ».', 'Dan Rasul-Nya».', 'ر س ل', '-', 'Wawu + Rasul + hi', 'hi merujuk ke Allah', 'Ma\'thuf', '-', '-'),
    ('وَرُوِيَ', 'Dan diriwayatkan', 'ر و ي', '-', 'Wawu + Ruwiya', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Hadits'),
    ('مِثْلُهُ', 'Yang semisalnya', 'م ث ل', '-', 'Bersambung dhamir hu', 'hu merujuk ke hadits di atas', 'Na\'ib Fa\'il', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مُعَاذٍ', 'Mu\'adz', 'ع و ذ', '-', '-', '-', 'Majrur', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَنْهُ', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Mu\'adz', 'Jar Majrur', '-', '-'),
    ('(٥/', '(Jilid 5 /', '-', '-', '-', '-', '-', '-', '-'),
    ('٢٣٨).', 'Hal 238).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'الصَّلَاةَ' (11), 'الله' (24)
blocks_104.append({
    'type': 'paragraph',
    'ar': 'رَسُولُ اللهِ ﷺ قَالَ: «لَا تَتْرُكِي الصَّلَاةَ مُتَعَمِّداً، فَإِنَّهُ مَنْ تَرَكَ الصَّلَاةَ مُتَعَمِّداً فَقَدْ بَرِئَتْ مِنْهُ ذِمَّةُ اللَّهِ وَرَسُولِهِ». وَرُوِيَ مِثْلُهُ عَنْ مُعَاذٍ رضي الله عَنْهُ (٥/ ٢٣٨).',
    'id': 'Bahwa Rasulullah SAW bersabda: "Janganlah engkau meninggalkan shalat dengan sengaja, karena sesungguhnya barangsiapa yang meninggalkan shalat dengan sengaja, maka lepaslah jaminan perlindungan Allah dan Rasul-Nya dari dirinya." Diriwayatkan pula hadits yang semisal dari Mu\'adz RA (Musnad Ahmad 5/238).',
    'words': make_words(p1_words, [11, 24])
})

# Heading 1
# حُكْمُ تَارِكِ الصَّلَاةِ :
h1_words = [
    ('حُكْمُ', 'Hukum bagi', 'ح ك م', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('تَارِكِ', 'Orang yang meninggalkan', 'ت ر ك', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_104.append({'type': 'heading', 'ar': 'حُكْمُ تَارِكِ الصَّلَاةِ :', 'id': 'Hukum Bagi Orang Yang Meninggalkan Shalat:', 'words': make_words(h1_words, [])})

# Para 2
# Text:
# تَارِكُ الصَّلَاةِ إِمَّا أَنْ يَكُونَ قَدْ تَرَكَهَا كَسَلًا وَتَهَاوُناً، أَوْ تَرَكَهَا جُحُوداً
# لَهَا، أَوْ اسْتِخْفَافاً بِهَا:
p2_words = [
    ('تَارِكُ', 'Orang yang meninggalkan', 'ت ر ك', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('إِمَّا', 'Ada kalanya', '-', '-', 'In + Ma', '-', 'Huruf Syarat/Tafshil', '-', '-'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('يَكُونَ', 'Ia berada dalam keadaan', 'ك و ن', '-', '-', '-', 'Fi\'il Mudhari\' Naqish', 'Tsulasi Mujarrad', 'Tarik (Orang tsb)'),
    ('قَدْ', 'Sungguh ia', '-', '-', '-', '-', 'Huruf Tahqiq', '-', '-'),
    ('تَرَكَهَا', 'Telah meninggalkannya', 'ت ر ك', '-', 'Taraka + ha', 'ha merujuk ke shalat', 'Fi\'il Madhi (Khabar Yakuna)', 'Tsulasi Mujarrad', 'Tarik'),
    ('كَسَلًا', 'Karena malas', 'ك س ل', '-', '-', '-', 'Maf\'ul liajlih / Hal', '-', '-'),
    ('وَتَهَاوُناً،', 'Dan menyepelekannya,', 'ه و ن', '-', 'Wawu + Tahawun', '-', 'Ma\'thuf', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('تَرَكَهَا', 'Telah meninggalkannya', 'ت ر ك', '-', 'Taraka + ha', 'ha merujuk ke shalat', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Tarik'),
    ('جُحُوداً', 'Karena mengingkari (kewajibannya)', 'ج ح د', '-', '-', '-', 'Maf\'ul liajlih / Hal', '-', '-'),
    ('لَهَا،', 'Terhadapnya,', '-', '-', 'Lam jar + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('اسْتِخْفَافاً', 'Karena meremehkannya', 'خ ف ف', '-', '-', '-', 'Ma\'thuf / Maf\'ul liajlih', '-', '-'),
    ('بِهَا:', 'Dengannya:', '-', '-', 'Baa jar + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-')
]
# Breaks: 'جُحُوداً' (11)
blocks_104.append({
    'type': 'paragraph',
    'ar': 'تَارِكُ الصَّلَاةِ إِمَّا أَنْ يَكُونَ قَدْ تَرَكَهَا كَسَلًا وَتَهَاوُناً، أَوْ تَرَكَهَا جُحُوداً لَهَا، أَوْ اسْتِخْفَافاً بِهَا:',
    'id': 'Orang yang meninggalkan shalat adakalanya ia meninggalkannya karena malas dan menyepelekan, atau ia meninggalkannya karena mengingkari kewajibannya, atau karena merendahkannya:',
    'words': make_words(p2_words, [11])
})

# Para 3
# Text:
# فَأَمَّا مَنْ تَرَكَهَا جَاحِداً لِوُجُوبِهَا، أَوْ مُسْتَهْزِئاً بِهَا، فَإِنَّهُ يَكْفُرُ بِذَلِكَ
# وَيَرْتَدُّ عَنِ الْإِسْلَامِ. فَيَجِبُ عَلَى الْحَاكِمِ أَنْ يَأْمُرَهُ بِالتَّوْبَةِ، فَإِنْ تَابَ وَأَقَامَ
# الصَّلَاةَ فَذَاكَ، وَإِلَّا قُتِلَ عَلَى أَنَّهُ مُرْتَدٌّ، وَلَا يَجُوزُ غُسْلُهُ وَلَا تَكْفِينُهُ
# وَلَا الصَّلَاةُ عَلَيْهِ، كَمَا لَا يَجُوزُ دَفْنُهُ فِي مَقَابِرِ الْمُسْلِمِينَ، لِأَنَّهُ لَيْسَ مِنْهُمْ .
p3_words = [
    ('فَأَمَّا', 'Maka adapun', '-', '-', 'Fa + Amma', '-', 'Huruf Syarat & Tafshil', '-', '-'),
    ('مَنْ', 'Orang yang', '-', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('تَرَكَهَا', 'Meninggalkannya', 'ت ر ك', '-', 'Taraka + ha', 'ha merujuk ke shalat', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Man'),
    ('جَاحِداً', 'Dalam keadaan mengingkari', 'ج ح د', '-', '-', '-', 'Hal', '-', '-'),
    ('لِوُجُوبِهَا،', 'Akan kewajibannya,', 'و ج ب', '-', 'Lam jar + Wujub + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('مُسْتَهْزِئاً', 'Memperolok-olok', 'ه ز أ', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('بِهَا،', 'Dengannya,', '-', '-', 'Baa jar + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('فَإِنَّهُ', 'Maka sesungguhnya ia', '-', '-', 'Fa (jawab) + Inna + hu', 'hu merujuk ke orang tersebut', 'Amil Nawasikh', '-', '-'),
    ('يَكْفُرُ', 'Telah kafir', 'ك ف ر', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar Inna)', 'Tsulasi Mujarrad', 'Hua'),
    ('بِذَلِكَ', 'Dengan perbuatannya itu', 'ذ ل ك', '-', 'Baa jar + Dzalika', '-', 'Jar Majrur', '-', '-'),
    ('وَيَرْتَدُّ', 'Dan murtad (keluar)', 'ر د د', '-', 'Wawu + Yartaddu', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Hua'),
    ('عَنِ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْإِسْلَامِ.', 'Agama Islam.', 'س ل م', '-', '-', '-', 'Majrur', '-', '-'),
    ('فَيَجِبُ', 'Maka wajib', 'و ج ب', '-', 'Fa + Yajibu', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'An Ya\'murahu (Mashdar Muawwal)'),
    ('عَلَى', 'Bagi', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْحَاكِمِ', 'Hakim (Pemerintah)', 'ح ك م', '-', '-', '-', 'Majrur', '-', '-'),
    ('أَنْ', 'Untuk', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('يَأْمُرَهُ', 'Memerintahkannya', 'أ م ر', '-', 'Ya\'mura + hu', 'hu merujuk ke orang tersebut', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Al-Hakim'),
    ('بِالتَّوْبَةِ،', 'Untuk bertaubat,', 'ت و ب', '-', 'Baa jar + Taubah', '-', 'Jar Majrur', '-', '-'),
    ('فَإِنْ', 'Maka jika', '-', '-', 'Fa + In', '-', 'Huruf Syarat', '-', '-'),
    ('تَابَ', 'Ia bertaubat', 'ت و ب', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Orang tersebut'),
    ('وَأَقَامَ', 'Dan mendirikan', 'ق و م', '-', 'Wawu + Aqama', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Orang tersebut'),
    ('الصَّلَاةَ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('فَذَاكَ،', 'Maka itulah (yang diharapkan),', 'ذ ل ك', '-', 'Fa + Dza + ka', '-', 'Khabar dari mubtada mahdzuf', '-', '-'),
    ('وَإِلَّا', 'Dan jika tidak (bertaubat)', '-', '-', 'Wawu + In + Laa', '-', 'Huruf Syarat Nafi', '-', '-'),
    ('قُتِلَ', 'Ia dibunuh (dieksekusi mati)', 'ق ت ل', '-', '-', '-', 'Fi\'il Madhi Majhul (Jawab)', 'Tsulasi Mujarrad', 'Orang tersebut'),
    ('عَلَى', 'Atas dasar', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنَّهُ', 'Bahwa ia', '-', '-', 'Anna + hu', 'hu merujuk ke orang tersebut', 'Amil Nawasikh', '-', '-'),
    ('مُرْتَدٌّ،', 'Adalah orang murtad,', 'ر د د', '-', '-', '-', 'Khabar Anna', '-', '-'),
    ('وَلَا', 'Dan tidak', '-', '-', 'Wawu + Laa', '-', 'Huruf Nafi', '-', '-'),
    ('يَجُوزُ', 'Boleh', 'ج و ز', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Ghusluhu (Memandikannya)'),
    ('غُسْلُهُ', 'Memandikannya (jenazahnya)', 'غ س ل', '-', 'Ghuslu + hu', 'hu merujuk ke mayat murtad', 'Fa\'il', '-', '-'),
    ('وَلَا', 'Dan tidak', '-', '-', 'Wawu + Laa', '-', 'Huruf Nafi', '-', '-'),
    ('تَكْفِينُهُ', 'Mengafaninya', 'ك ف ن', '-', 'Takfinu + hu', 'hu merujuk ke mayat murtad', 'Ma\'thuf', '-', '-'),
    ('وَلَا', 'Dan tidak pula', '-', '-', 'Wawu + Laa', '-', 'Huruf Nafi', '-', '-'),
    ('الصَّلَاةُ', 'Menyalatkannya', 'ص ل ي', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('عَلَيْهِ،', 'Atasnya,', '-', '-', 'Ala + hi', 'hi merujuk ke mayat murtad', 'Jar Majrur', '-', '-'),
    ('كَمَا', 'Sebagaimana pula', '-', '-', 'Kaf jar + Ma', '-', 'Jar Majrur', '-', '-'),
    ('لَا', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَجُوزُ', 'Boleh', 'ج و ز', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Dafnuhu'),
    ('دَفْنُهُ', 'Menguburkannya', 'د ف ن', '-', 'Dafnu + hu', 'hu merujuk ke mayat murtad', 'Fa\'il', '-', '-'),
    ('فِي', 'Di', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مَقَابِرِ', 'Pemakaman', 'ق ب ر', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('الْمُسْلِمِينَ،', 'Orang-orang muslim,', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لِأَنَّهُ', 'Karena sesungguhnya ia', '-', '-', 'Lam ta\'lil + Anna + hu', 'hu merujuk ke mayat murtad', 'Amil Nawasikh', '-', '-'),
    ('لَيْسَ', 'Bukanlah', 'ل ي س', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Hua (merujuk ke mayat murtad)'),
    ('مِنْهُمْ', 'Bagian dari mereka (muslimin)', '-', '-', 'Min + hum', 'hum merujuk ke muslimin', 'Jar Majrur / Khabar Laisa', '-', '-'),
    ('.', '.', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'بِذَلِكَ' (10), 'وَأَقَامَ' (22), 'تَكْفِينُهُ' (34)
blocks_104.append({
    'type': 'paragraph',
    'ar': 'فَأَمَّا مَنْ تَرَكَهَا جَاحِداً لِوُجُوبِهَا، أَوْ مُسْتَهْزِئاً بِهَا، فَإِنَّهُ يَكْفُرُ بِذَلِكَ وَيَرْتَدُّ عَنِ الْإِسْلَامِ. فَيَجِبُ عَلَى الْحَاكِمِ أَنْ يَأْمُرَهُ بِالتَّوْبَةِ، فَإِنْ تَابَ وَأَقَامَ الصَّلَاةَ فَذَاكَ، وَإِلَّا قُتِلَ عَلَى أَنَّهُ مُرْتَدٌّ، وَلَا يَجُوزُ غُسْلُهُ وَلَا تَكْفِينُهُ وَلَا الصَّلَاةُ عَلَيْهِ، كَمَا لَا يَجُوزُ دَفْنُهُ فِي مَقَابِرِ الْمُسْلِمِينَ، لِأَنَّهُ لَيْسَ مِنْهُمْ .',
    'id': 'Maka adapun orang yang meninggalkannya (shalat) dalam keadaan mengingkari kewajibannya atau memperolok-oloknya, maka sungguh ia telah kafir dengan sebab hal itu dan murtad keluar dari Islam. Maka wajib bagi pemerintah/hakim untuk memerintahkannya bertaubat; Jika ia bertaubat dan kembali mendirikan shalat maka itulah yang diharapkan, namun jika ia enggan maka ia dijatuhi hukuman mati atas statusnya sebagai orang murtad. Jenazahnya tidak boleh dimandikan, tidak boleh dikafani, dan tidak boleh dishalatkan, sebagaimana juga ia tidak boleh dikuburkan di pemakaman kaum muslimin, karena ia bukanlah bagian dari mereka.',
    'words': make_words(p3_words, [10, 22, 34])
})

# Para 4
# Text:
# وَأَمَّا إِنْ تَرَكَهَا كَسَلًا، وَهُوَ يَعْتَقِدُ وُجُوبَهَا، فَإِنَّهُ يُكَلَّفُ مِنْ قِبَلِ
# الْحَاكِمِ بِقَضَائِهَا وَالتَّوْبَةِ عَنْ مَعْصِيَةِ التَّرْكِ. فَإِنْ لَمْ يَنْهَضْ إِلَى قَضَائِهَا وَجَبَ
# قَتْلُهُ حَدّاً، أَيْ يُعْتَبَرُ قَتْلُهُ حَدّاً مِنَ الْحُدُودِ الْمَشْرُوعَةِ لِعُصَاةِ الْمُسْلِمِينَ،
# وَعُقُوبَةً عَلَى تَرْكِهِ فَرِيضَةً يُقَاتَلُ عَلَيْهَا. وَلَكِنَّهُ يُعْتَبَرُ مُسْلِماً بَعْدَ قَتْلِهِ وَيُعَامَلُ
# فِي تَجْهِيزِهِ وَدَفْنِهِ وَمِيرَاثِهِ مُعَامَلَةَ الْمُسْلِمِينَ لِأَنَّهُ مِنْهُمْ .
p4_words = [
    ('وَأَمَّا', 'Dan adapun', '-', '-', 'Wawu + Amma', '-', 'Huruf Syarat & Tafshil', '-', '-'),
    ('إِنْ', 'Jika', '-', '-', '-', '-', 'Huruf Syarat', '-', '-'),
    ('تَرَكَهَا', 'Ia meninggalkannya', 'ت ر ك', '-', 'Taraka + ha', 'ha merujuk ke shalat', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Hua'),
    ('كَسَلًا،', 'Karena malas semata,', 'ك س ل', '-', '-', '-', 'Maf\'ul liajlih / Hal', '-', '-'),
    ('وَهُوَ', 'Sementara ia', '-', '-', 'Wawu hal + Hua', 'Hua merujuk ke pelaku', 'Mubtada\'', '-', '-'),
    ('يَعْتَقِدُ', 'Masih meyakini', 'ع ق د', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mazid', 'Hua'),
    ('وُجُوبَهَا،', 'Kewajibannya,', 'و ج ب', '-', 'Wujub + ha', 'ha merujuk ke shalat', 'Maf\'ul Bih', '-', '-'),
    ('فَإِنَّهُ', 'Maka sesungguhnya ia', '-', '-', 'Fa (Jawab) + Inna + hu', 'hu merujuk ke pelaku', 'Amil Nawasikh', '-', '-'),
    ('يُكَلَّفُ', 'Diberi tuntutan', 'ك ل ف', '-', '-', '-', 'Fi\'il Mudhari\' Majhul (Khabar Inna)', 'Tsulasi Mazid', 'Hua'),
    ('مِنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('قِبَلِ', 'Pihak', 'ق ب ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْحَاكِمِ', 'Hakim (Pemerintah)', 'ح ك م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('بِقَضَائِهَا', 'Untuk mengqadhanya (menggantinya)', 'ق ض ي', '-', 'Baa jar + Qadha\' + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('وَالتَّوْبَةِ', 'Dan bertaubat', 'ت و ب', '-', 'Wawu + Taubah', '-', 'Ma\'thuf', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مَعْصِيَةِ', 'Maksiat (dosa)', 'ع ص ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('التَّرْكِ.', 'Meninggalkan (shalat).', 'ت ر ك', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَإِنْ', 'Maka jika', '-', '-', 'Fa + In', '-', 'Huruf Syarat', '-', '-'),
    ('لَمْ', 'Ia tidak', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَنْهَضْ', 'Bangkit (segera)', 'ن ه ض', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mujarrad', 'Hua'),
    ('إِلَى', 'Menuju', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('قَضَائِهَا', 'Mengqadhanya', 'ق ض ي', '-', 'Qadha\' + ha', 'ha merujuk ke shalat', 'Majrur', '-', '-'),
    ('وَجَبَ', 'Wajiblah', 'و ج ب', '-', '-', '-', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mujarrad', 'Qatluhu'),
    ('قَتْلُهُ', 'Untuk membunuhnya', 'ق ت ل', '-', 'Qatlu + hu', 'hu merujuk ke pelaku', 'Fa\'il', '-', '-'),
    ('حَدّاً،', 'Sebagai hukuman had (pidana Islam),', 'ح د د', '-', '-', '-', 'Hal', '-', '-'),
    ('أَيْ', 'Yaitu', '-', '-', '-', '-', 'Huruf Tafsir', '-', '-'),
    ('يُعْتَبَرُ', 'Dianggap', 'ع ب ر', '-', '-', '-', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mazid', 'Qatluhu'),
    ('قَتْلُهُ', 'Hukuman matinya itu', 'ق ت ل', '-', 'Qatlu + hu', 'hu merujuk ke pelaku', 'Na\'ib Fa\'il', '-', '-'),
    ('حَدّاً', 'Sebagai pidana', 'ح د د', '-', '-', '-', 'Maf\'ul Tsani / Hal', '-', '-'),
    ('مِنَ', 'Dari (kategori)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْحُدُودِ', 'Hukuman-hukuman pidana', 'ح د د', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('الْمَشْرُوعَةِ', 'Yang disyariatkan', 'ش ر ع', '-', '-', '-', 'Na\'at', '-', '-'),
    ('لِعُصَاةِ', 'Bagi para pembuat maksiat', 'ع ص ي', 'Jamak', 'Lam jar + \'Ushat', '-', 'Jar Majrur', '-', '-'),
    ('الْمُسْلِمِينَ،', 'Dari kaum muslimin,', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَعُقُوبَةً', 'Dan sebagai sanksi', 'ع ق ب', '-', 'Wawu + Uqubah', '-', 'Ma\'thuf', '-', '-'),
    ('عَلَى', 'Atas perbuatannya', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('تَرْكِهِ', 'Meninggalkan', 'ت ر ك', '-', 'Tarki + hi', 'hi merujuk ke pelaku', 'Majrur', '-', '-'),
    ('فَرِيضَةً', 'Sebuah hal yang fardhu', 'ف ر ض', '-', '-', '-', 'Maf\'ul bih dari mashdar', '-', '-'),
    ('يُقَاتَلُ', 'Yang pantas diperangi', 'ق ت ل', '-', '-', '-', 'Fi\'il Mudhari\' Majhul (Sifat)', 'Tsulasi Mazid', 'Orang (Hua)'),
    ('عَلَيْهَا.', 'Atas (meninggalkan) nya.', '-', '-', 'Ala + ha', 'ha merujuk ke faridhah', 'Jar Majrur', '-', '-'),
    ('وَلَكِنَّهُ', 'Namun sesungguhnya ia', 'ل ك ن', '-', 'Wawu + Lakinna + hu', 'hu merujuk ke pelaku', 'Amil Nawasikh', '-', '-'),
    ('يُعْتَبَرُ', 'Tetap dianggap', 'ع ب ر', '-', '-', '-', 'Fi\'il Mudhari\' Majhul (Khabar)', 'Tsulasi Mazid', 'Hua'),
    ('مُسْلِماً', 'Sebagai seorang muslim', 'س ل م', '-', '-', '-', 'Maf\'ul Tsani / Hal', '-', '-'),
    ('بَعْدَ', 'Setelah', 'ب ع د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('قَتْلِهِ', 'Kematian/eksekusinya', 'ق ت ل', '-', 'Qatli + hi', 'hi merujuk ke pelaku', 'Mudhaf Ilaih', '-', '-'),
    ('وَيُعَامَلُ', 'Dan ia diperlakukan', 'ع م ل', '-', 'Wawu + Yu\'amalu', '-', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mazid', 'Hua'),
    ('فِي', 'Dalam urusan', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('تَجْهِيزِهِ', 'Pengurusannya', 'ج ه ز', '-', 'Tajhizi + hi', 'hi merujuk ke pelaku', 'Majrur', '-', '-'),
    ('وَدَفْنِهِ', 'Dan pemakamannya', 'د ف ن', '-', 'Wawu + Dafni + hi', '-', 'Ma\'thuf', '-', '-'),
    ('وَمِيرَاثِهِ', 'Dan warisannya', 'و ر ث', '-', 'Wawu + Miratsi + hi', '-', 'Ma\'thuf', '-', '-'),
    ('مُعَامَلَةَ', 'Dengan perlakuan', 'ع م ل', '-', '-', '-', 'Maf\'ul Muthlaq', '-', '-'),
    ('الْمُسْلِمِينَ', 'Kaum muslimin pada umumnya', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لِأَنَّهُ', 'Karena sesungguhnya ia', '-', '-', 'Lam ta\'lil + Anna + hu', 'hu merujuk ke pelaku', 'Amil Nawasikh', '-', '-'),
    ('مِنْهُمْ', 'Masih bagian dari mereka.', '-', '-', 'Min + hum', 'hum merujuk ke muslimin', 'Jar Majrur / Khabar Anna', '-', '-'),
    ('.', '.', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'قِبَلِ' (11), 'وَجَبَ' (22), 'الْمُسْلِمِينَ،' (33), 'وَيُعَامَلُ' (45)
blocks_104.append({
    'type': 'paragraph',
    'ar': 'وَأَمَّا إِنْ تَرَكَهَا كَسَلًا، وَهُوَ يَعْتَقِدُ وُجُوبَهَا، فَإِنَّهُ يُكَلَّفُ مِنْ قِبَلِ الْحَاكِمِ بِقَضَائِهَا وَالتَّوْبَةِ عَنْ مَعْصِيَةِ التَّرْكِ. فَإِنْ لَمْ يَنْهَضْ إِلَى قَضَائِهَا وَجَبَ قَتْلُهُ حَدّاً، أَيْ يُعْتَبَرُ قَتْلُهُ حَدّاً مِنَ الْحُدُودِ الْمَشْرُوعَةِ لِعُصَاةِ الْمُسْلِمِينَ، وَعُقُوبَةً عَلَى تَرْكِهِ فَرِيضَةً يُقَاتَلُ عَلَيْهَا. وَلَكِنَّهُ يُعْتَبَرُ مُسْلِماً بَعْدَ قَتْلِهِ وَيُعَامَلُ فِي تَجْهِيزِهِ وَدَفْنِهِ وَمِيرَاثِهِ مُعَامَلَةَ الْمُسْلِمِينَ لِأَنَّهُ مِنْهُمْ .',
    'id': 'Dan adapun jika ia meninggalkan shalat hanya karena kemalasan semata, sementara ia masih meyakini penuh kewajibannya, maka ia dituntut oleh hakim (pemerintah) untuk segera mengqadhanya (menggantinya) serta bertaubat dari maksiat tersebut. Jika ia tetap tidak mau bangkit untuk mengqadhanya maka ia wajib dieksekusi mati sebagai hukuman (Had). Artinya hukuman matinya itu dianggap sebagai bentuk pidana Islam yang sah bagi pelaku maksiat dari kalangan kaum muslimin, dan sebagai sanksi atas tindakannya mengabaikan hal fardhu yang layak diperangi. Akan tetapi, ia masih dianggap berstatus sebagai seorang muslim (bukan murtad) setelah kematiannya, sehingga urusan penyiapan jenazah, pemakaman, dan pembagian warisannya tetap diperlakukan selayaknya kaum muslimin pada umumnya, karena ia masih bagian dari mereka.',
    'words': make_words(p4_words, [11, 22, 33, 45])
})

# Para 5
# Text:
# رَوَى الْبُخَارِيُّ (٢٥)؛ وَمُسْلِمٌ (٢٢)، عَنِ ابْنِ عُمَرَ رضي الله
# عَنْهُمَا: أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «أُمِرْتُ أَنْ أُقَاتِلَ النَّاسَ حَتَّى يَشْهَدُوا أَنْ
# لَا إِلَهَ إِلَّا اللَّهُ وَأَنَّ مُحَمَّداً رَّسُولُ اللَّهِ وَيُقِيمُوا الصَّلَاةَ وَيُؤْتُوا الزَّكَاةَ، فَإِذَا
# فَعَلُوا ذَلِكَ عَصَمُوا مِنِّي دِمَاءَهُمْ وَأَمْوَالَهُمْ إِلَّا بِحَقِّ الْإِسْلَامِ، وَحِسَابُهُمْ
# عَلَى اللَّهِ» .
p5_words = [
    ('رَوَى', 'Telah meriwayatkan', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Bukhari'),
    ('الْبُخَارِيُّ', 'Al-Bukhari', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٢٥)؛', '(25);', '-', '-', '-', '-', '-', '-', '-'),
    ('وَمُسْلِمٌ', 'Dan Muslim', 'س ل م', '-', 'Wawu + Muslim', '-', 'Ma\'thuf', '-', '-'),
    ('(٢٢)،', '(22),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنِ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ابْنِ', 'Ibnu (Putra)', 'ب ن ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('عُمَرَ', 'Umar', 'ع م ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَنْهُمَا:', 'Atas keduanya:', '-', '-', 'An + huma', 'huma merujuk ke Ibnu Umar dan ayahnya', 'Jar Majrur', '-', '-'),
    ('أَنَّ', 'Bahwa', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('رَسُولَ', 'Rasul', 'ر س ل', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('قَالَ:', 'Telah bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi (Khabar Anna)', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«أُمِرْتُ', '«Aku diperintahkan', 'أ م ر', '-', 'Umira + tu', 'tu merujuk ke Rasulullah', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Aku (Tu)'),
    ('أَنْ', 'Untuk', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('أُقَاتِلَ', 'Memerangi', 'ق ت ل', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Aku (Ana)'),
    ('النَّاسَ', 'Manusia (Kafir)', 'ن و س', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar / Nashab', '-', '-'),
    ('يَشْهَدُوا', 'Mereka bersaksi', 'ش ه د', '-', 'Yasyhadu + Wawu Jama\'ah', 'Wawu merujuk ke manusia', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Mereka (Wawu)'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('لَا', 'Tidak ada', '-', '-', '-', '-', 'Laa Nafi Lil Jinsi', '-', '-'),
    ('إِلَهَ', 'Tuhan', 'أ ل ه', '-', '-', '-', 'Isim Laa', '-', '-'),
    ('إِلَّا', 'Kecuali', '-', '-', '-', '-', 'Huruf Istitsna\'', '-', '-'),
    ('اللَّهُ', 'Allah', '-', '-', '-', '-', 'Badal / Khabar', '-', '-'),
    ('وَأَنَّ', 'Dan bahwa', '-', '-', 'Wawu + Anna', '-', 'Amil Nawasikh', '-', '-'),
    ('مُحَمَّداً', 'Muhammad', 'ح م د', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('رَّسُولُ', 'Adalah utusan', 'ر س ل', '-', '-', '-', 'Khabar Anna', '-', '-'),
    ('اللَّهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَيُقِيمُوا', 'Dan mereka mendirikan', 'ق و م', '-', 'Wawu + Yuqimu + Wawu', '-', 'Fi\'il Mudhari\' (Ma\'thuf)', 'Tsulasi Mazid', 'Mereka (Wawu)'),
    ('الصَّلَاةَ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('وَيُؤْتُوا', 'Dan mereka menunaikan', 'أ ت ي', '-', 'Wawu + Yu\'tu + Wawu', '-', 'Fi\'il Mudhari\' (Ma\'thuf)', 'Tsulasi Mazid', 'Mereka (Wawu)'),
    ('الزَّكَاةَ،', 'Zakat,', 'ز ك و', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('فَإِذَا', 'Maka apabila', '-', '-', 'Fa + Idza', '-', 'Zharf Zaman / Syarat', '-', '-'),
    ('فَعَلُوا', 'Mereka telah melakukan', 'ف ع ل', '-', 'Fa\'alu + Wawu', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Mereka (Wawu)'),
    ('ذَلِكَ', 'Hal tersebut', 'ذ ل ك', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('عَصَمُوا', 'Mereka telah memelihara/melindungi', 'ع ص م', '-', 'Ashamu + Wawu', '-', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mujarrad', 'Mereka (Wawu)'),
    ('مِنِّي', 'Dariku', '-', '-', 'Min + Ni', '-', 'Jar Majrur', '-', '-'),
    ('دِمَاءَهُمْ', 'Darah mereka', 'د م و', '-', 'Dima\' + hum', 'hum merujuk ke mereka', 'Maf\'ul Bih', '-', '-'),
    ('وَأَمْوَالَهُمْ', 'Dan harta mereka', 'م و ل', '-', 'Wawu + Amwal + hum', '-', 'Ma\'thuf', '-', '-'),
    ('إِلَّا', 'Melainkan', '-', '-', '-', '-', 'Huruf Istitsna\'', '-', '-'),
    ('بِحَقِّ', 'Dengan hak (aturan pidana)', 'ح ق ق', '-', 'Baa jar + Haqq', '-', 'Jar Majrur', '-', '-'),
    ('الْإِسْلَامِ،', 'Islam,', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَحِسَابُهُمْ', 'Adapun hisab (perhitungan/niat hati) mereka', 'ح س ب', '-', 'Wawu + Hisab + hum', '-', 'Mubtada\'', '-', '-'),
    ('عَلَى', 'Adalah wewenang (atas)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('اللَّهِ»', 'Allah»', '-', '-', '-', '-', 'Majrur / Khabar', '-', '-'),
    ('.', '.', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'الله' (9), 'أَنْ' (17), 'فَإِذَا' (35), 'وَحِسَابُهُمْ' (45)
blocks_104.append({
    'type': 'paragraph',
    'ar': 'رَوَى الْبُخَارِيُّ (٢٥)؛ وَمُسْلِمٌ (٢٢)، عَنِ ابْنِ عُمَرَ رضي الله عَنْهُمَا: أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «أُمِرْتُ أَنْ أُقَاتِلَ النَّاسَ حَتَّى يَشْهَدُوا أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَأَنَّ مُحَمَّداً رَّسُولُ اللَّهِ وَيُقِيمُوا الصَّلَاةَ وَيُؤْتُوا الزَّكَاةَ، فَإِذَا فَعَلُوا ذَلِكَ عَصَمُوا مِنِّي دِمَاءَهُمْ وَأَمْوَالَهُمْ إِلَّا بِحَقِّ الْإِسْلَامِ، وَحِسَابُهُمْ عَلَى اللَّهِ» .',
    'id': 'Telah meriwayatkan Al-Bukhari (25) dan Muslim (22), dari Ibnu Umar RA: Bahwa Rasulullah SAW bersabda: "Aku diperintahkan untuk memerangi manusia hingga mereka bersaksi bahwa tidak ada Tuhan yang berhak disembah melainkan Allah dan Muhammad adalah utusan Allah, serta hingga mereka mendirikan shalat dan menunaikan zakat. Jika mereka melakukan hal itu, maka darah dan harta mereka terjaga (terlindungi) dariku melainkan dengan hak Islam (aturan pidana/qishash hukum Islam), adapun perhitungan niat batin mereka adalah wewenang Allah semata".',
    'words': make_words(p5_words, [9, 17, 35, 45])
})

# Para 6
# Text:
# دَلَّ الْحَدِيثُ عَلَى أَنَّ مَنْ أَقَرَّ بِالشَّهَادَتَيْنِ يُقَاتَلُ إِنْ لَمْ يَقِمِ الصَّلَاةَ،
p6_words = [
    ('دَلَّ', 'Telah menunjukkan', 'د ل ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Hadits'),
    ('الْحَدِيثُ', 'Hadits tersebut', 'ح د ث', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَلَى', 'Atas (fakta)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنَّ', 'Bahwa', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('مَنْ', 'Barangsiapa yang', '-', '-', '-', '-', 'Isim Anna (Syarat)', '-', '-'),
    ('أَقَرَّ', 'Telah ikrar/mengakui', 'ق ر ر', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mazid', 'Man (Siapa saja)'),
    ('بِالشَّهَادَتَيْنِ', 'Dengan dua kalimat syahadat', 'ش ه د', '-', 'Baa jar + Shahadataini', '-', 'Jar Majrur', '-', '-'),
    ('يُقَاتَلُ', 'Akan tetap diperangi', 'ق ت ل', '-', '-', '-', 'Fi\'il Mudhari\' Majhul (Khabar Anna)', 'Tsulasi Mazid', 'Hua'),
    ('إِنْ', 'Jika', '-', '-', '-', '-', 'Huruf Syarat', '-', '-'),
    ('لَمْ', 'Ia tidak', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَقِمِ', 'Mendirikan', 'ق و م', '-', '-', '-', 'Fi\'il Mudhari\' Majzum (Syarat)', 'Tsulasi Mazid', 'Hua'),
    ('الصَّلَاةَ،', 'Shalat,', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-')
]
# Breaks: none (last line of page)
blocks_104.append({
    'type': 'paragraph',
    'ar': 'دَلَّ الْحَدِيثُ عَلَى أَنَّ مَنْ أَقَرَّ بِالشَّهَادَتَيْنِ يُقَاتَلُ إِنْ لَمْ يَقِمِ الصَّلَاةَ،',
    'id': 'Hadits ini memberikan petunjuk kuat bahwa meskipun seseorang telah berikrar (mengakui) dua kalimat syahadat, ia tetap bisa diperangi apabila tidak mau mendirikan shalat,',
    'words': make_words(p6_words, [])
})


data.append({
    'pageNumber': 104,
    'blocks': blocks_104
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 104 appended to data.js successfully.')
