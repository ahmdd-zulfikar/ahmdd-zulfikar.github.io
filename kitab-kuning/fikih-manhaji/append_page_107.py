import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_107 = []

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

# Para 1 (Continuation of Waqtu Fajar from page 106)
# Text:
# رَسُولُ اللهِ ﷺ : «وَقْتُ صَلَاةِ الصُّبْحِ مِنْ طُلُوعِ الْفَجْرِ مَا لَمْ تَطْلُعِ
# الشَّمْسُ» (رواه مسلم: ٦١٢).
p1_words = [
    ('رَسُولُ', 'Rasul', 'ر س ل', '-', '-', '-', 'Fa\'il (dari qala di halaman sblm)', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«وَقْتُ', '«Waktu', 'و ق ت', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('صَلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الصُّبْحِ', 'Shubuh', 'ص ب ح', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مِنْ', 'Bermula dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('طُلُوعِ', 'Terbitnya', 'ط ل ع', '-', '-', '-', 'Majrur / Khabar', '-', '-'),
    ('الْفَجْرِ', 'Fajar', 'ف ج ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَا', 'Selama belum', '-', '-', '-', '-', 'Huruf Mashdariyah Zharfiyah', '-', '-'),
    ('لَمْ', 'Belum (tidak)', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('تَطْلُعِ', 'Terbit/Muncullah', 'ط ل ع', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('الشَّمْسُ»', 'Matahari»', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('مسلم:', 'Muslim:', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٦١٢).', '612).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'تَطْلُعِ' (12)
blocks_107.append({
    'type': 'paragraph',
    'ar': 'رَسُولُ اللهِ ﷺ : «وَقْتُ صَلَاةِ الصُّبْحِ مِنْ طُلُوعِ الْفَجْرِ مَا لَمْ تَطْلُعِ الشَّمْسُ» (رواه مسلم: ٦١٢).',
    'id': 'Rasulullah SAW bersabda: "Waktu pelaksanaan shalat Shubuh adalah mulai terbitnya fajar selama matahari belum terbit" (HR. Muslim: 612).',
    'words': make_words(p1_words, [12])
})

# Heading: «الظُّهْرُ»:
h1_words = [
    ('«الظُّهْرُ»:', '«Waktu Zhuhur»:', 'ظ ه ر', '-', '-', '-', 'Mubtada\'', '-', '-')
]
blocks_107.append({'type': 'heading', 'ar': '«الظُّهْرُ»:', 'id': 'Waktu Shalat Zhuhur:', 'words': make_words(h1_words, [])})

# Para 2 (Waqtu Zhuhur Explanation)
# يَبْدَأُ وَقْتُهُ بِانْحِرَافِ الشَّمْسِ عَنْ مُنْتَصَفِ السَّمَاءِ نَحْوَ الْغُرُوبِ
# - وَيُسَمُّونَهُ الزَّوَالَ - حَيْثُ يَظْهَرُ لِلشَّاخِصِ عِنْدَئِذٍ ظِلٌّ يَسِيرٌ يَبْدَأُ بِالِامْتِدَادِ
# نَحْوَ جِهَةِ الشَّرْقِ - وَيُسَمُّونَهُ ظِلَّ الزَّوَالِ - . وَيَمْتَدُّ وَقْتُهُ إِلَى أَنْ يَصِيرَ
# طُولُ ظِلِّ الشَّيْءِ مِثْلَهُ، عِلَاوَةً عَلَى ظِلِّ الزَّوَالِ الَّذِي كَانَ عَلَامَةً عَلَى أَوَّلِ
# وَقْتِ الظُّهْرِ.
p2_words = [
    ('يَبْدَأُ', 'Ia mulai masuk', 'ب د أ', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Waqtuhu'),
    ('وَقْتُهُ', 'Waktunya', 'و ق ت', '-', 'Waqtu + hu', 'hu merujuk ke shalat zhuhur', 'Fa\'il', '-', '-'),
    ('بِانْحِرَافِ', 'Dengan tergelincirnya', 'ح ر ف', '-', 'Baa jar + Inhiraf', '-', 'Jar Majrur', '-', '-'),
    ('الشَّمْسِ', 'Matahari', 'ش م س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مُنْتَصَفِ', 'Tengah-tengah', 'ن ص ف', '-', '-', '-', 'Majrur', '-', '-'),
    ('السَّمَاءِ', 'Langit (Puncak)', 'س م و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('نَحْوَ', 'Ke arah', 'ن ح و', '-', '-', '-', 'Zharf Makan', '-', '-'),
    ('الْغُرُوبِ', 'Tenggelam (Barat)', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('وَيُسَمُّونَهُ', 'Dan mereka (ulama) menamakannya', 'س م و', '-', 'Wawu + Yusammuna + hu', 'hu merujuk ke peristiwa tergelincir', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Ulama (Wawu)'),
    ('الزَّوَالَ', 'Zawal', 'ز و ل', '-', '-', '-', 'Maf\'ul Bih Tsani', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('حَيْثُ', 'Yang mana (sekiranya)', 'ح ي ث', '-', '-', '-', 'Zharf', '-', '-'),
    ('يَظْهَرُ', 'Tampaklah', 'ظ ه ر', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Zhillun'),
    ('لِلشَّاخِصِ', 'Bagi suatu benda tegak lurus', 'ش خ ص', '-', 'Lam jar + Syakhis', '-', 'Jar Majrur', '-', '-'),
    ('عِنْدَئِذٍ', 'Pada saat itu', 'ع ن د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('ظِلٌّ', 'Sebuah bayangan', 'ظ ل ل', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('يَسِيرٌ', 'Kecil/pendek', 'ي س ر', '-', '-', '-', 'Na\'at', '-', '-'),
    ('يَبْدَأُ', 'Yang mulai', 'ب د أ', '-', '-', '-', 'Fi\'il Mudhari\' (Sifat)', 'Tsulasi Mujarrad', 'Zhillun'),
    ('بِالِامْتِدَادِ', 'Memanjang', 'م د د', '-', 'Baa jar + Imtidad', '-', 'Jar Majrur', '-', '-'),
    ('نَحْوَ', 'Ke arah', 'ن ح و', '-', '-', '-', 'Zharf Makan', '-', '-'),
    ('جِهَةِ', 'Sisi', 'ج ه ه', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّرْقِ', 'Timur', 'ش ر ق', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('وَيُسَمُّونَهُ', 'Dan mereka (ulama) menamakannya', 'س م و', '-', 'Wawu + Yusammuna + hu', 'hu merujuk ke bayangan tersebut', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Ulama (Wawu)'),
    ('ظِلَّ', 'Bayangan', 'ظ ل ل', '-', '-', '-', 'Maf\'ul Bih Tsani', '-', '-'),
    ('الزَّوَالِ', 'Zawal', 'ز و ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('.', '.', '-', '-', '-', '-', '-', '-', '-'),
    ('وَيَمْتَدُّ', 'Dan membentanglah/berlanjutlah', 'م د د', '-', 'Wawu + Yamtaddu', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Waqtuhu'),
    ('وَقْتُهُ', 'Waktunya (zhuhur)', 'و ق ت', '-', 'Waqtu + hu', 'hu merujuk ke zhuhur', 'Fa\'il', '-', '-'),
    ('إِلَى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('يَصِيرَ', 'Menjadi', 'ص ي ر', '-', '-', '-', 'Fi\'il Mudhari\' Naqish (Manshub)', 'Tsulasi Mujarrad', 'Thulu Zhill'),
    ('طُولُ', 'Panjang', 'ط و ل', '-', '-', '-', 'Isim Yashira', '-', '-'),
    ('ظِلِّ', 'Bayangan', 'ظ ل ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّيْءِ', 'Sesuatu (benda)', 'ش ي أ', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مِثْلَهُ،', 'Sama dengannya (benda tsb),', 'م ث ل', '-', 'Mitsla + hu', 'hu merujuk ke benda', 'Khabar Yashira', '-', '-'),
    ('عِلَاوَةً', 'Sebagai tambahan', 'ع ل و', '-', '-', '-', 'Hal', '-', '-'),
    ('عَلَى', 'Di luar (selain dari)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ظِلِّ', 'Bayangan', 'ظ ل ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('الزَّوَالِ', 'Zawal (bayangan pertama tadi)', 'ز و ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الَّذِي', 'Yang mana', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('كَانَ', 'Tadinya adalah', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Zhill Zawwal'),
    ('عَلَامَةً', 'Sebuah tanda', 'ع ل م', '-', '-', '-', 'Khabar Kana', '-', '-'),
    ('عَلَى', 'Bagi', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَوَّلِ', 'Awal masuknya', 'أ و ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الظُّهْرِ.', 'Zhuhur.', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-')
]
# Breaks: 'الْغُرُوبِ' (8), 'بِالِامْتِدَادِ' (20), 'يَصِيرَ' (34), 'أَوَّلِ' (48)
blocks_107.append({
    'type': 'paragraph',
    'ar': 'يَبْدَأُ وَقْتُهُ بِانْحِرَافِ الشَّمْسِ عَنْ مُنْتَصَفِ السَّمَاءِ نَحْوَ الْغُرُوبِ - وَيُسَمُّونَهُ الزَّوَالَ - حَيْثُ يَظْهَرُ لِلشَّاخِصِ عِنْدَئِذٍ ظِلٌّ يَسِيرٌ يَبْدَأُ بِالِامْتِدَادِ نَحْوَ جِهَةِ الشَّرْقِ - وَيُسَمُّونَهُ ظِلَّ الزَّوَالِ - . وَيَمْتَدُّ وَقْتُهُ إِلَى أَنْ يَصِيرَ طُولُ ظِلِّ الشَّيْءِ مِثْلَهُ، عِلَاوَةً عَلَى ظِلِّ الزَّوَالِ الَّذِي كَانَ عَلَامَةً عَلَى أَوَّلِ وَقْتِ الظُّهْرِ.',
    'id': 'Waktu Zhuhur mulai masuk ketika matahari tergelincir dari titik tengah langit (puncak) bergeser ke arah tenggelamnya (barat) — ulama menyebut peristiwa tergelincirnya ini dengan istilah "Zawal" — yakni ketika mulai muncul bayangan kecil/pendek bagi suatu benda yang tegak lurus, di mana bayangan tersebut mulai memanjang ke arah timur — yang ulama sebut dengan "Bayangan Zawal". Waktu ini akan membentang (berlanjut terus) sampai panjang bayangan suatu benda sama dengan tinggi benda aslinya, diluar hitungan "Bayangan Zawal" yang telah menjadi penanda awal waktu zhuhur tadi.',
    'words': make_words(p2_words, [8, 20, 34, 48])
})


# Para 3 (Dalil Zhuhur)
# رَوَى مُسْلِمٌ (٦١٢) أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «وَقْتُ الظُّهْرِ إِذَا زَالَتِ
# الشَّمْسُ، وَكَانَ ظِلُّ الرَّجُلِ كَطُولِهِ، مَا لَمْ يَحْضُرِ الْعَصْرُ».
p3_words = [
    ('رَوَى', 'Telah meriwayatkan', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Muslim'),
    ('مُسْلِمٌ', 'Muslim', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٦١٢)', '(612)', '-', '-', '-', '-', '-', '-', '-'),
    ('أَنَّ', 'Bahwa sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('رَسُولَ', 'Rasul', 'ر س ل', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('قَالَ:', 'Telah bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi (Khabar Anna)', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«وَقْتُ', '«Waktu', 'و ق ت', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الظُّهْرِ', 'Zhuhur', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('إِذَا', 'Adalah ketika', '-', '-', '-', '-', 'Zharf Zaman / Khabar', '-', '-'),
    ('زَالَتِ', 'Telah tergelincir', 'ز و ل', '-', 'Zalat + Ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('الشَّمْسُ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('وَكَانَ', 'Dan menjadilah', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Zhill'),
    ('ظِلُّ', 'Bayangan', 'ظ ل ل', '-', '-', '-', 'Isim Kana', '-', '-'),
    ('الرَّجُلِ', 'Seseorang (benda)', 'ر ج ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('كَطُولِهِ،', 'Sama seperti tinggi badannya,', 'ط و ل', '-', 'Kaf jar + Thul + hi', 'hi merujuk ke seseorang/benda', 'Jar Majrur / Khabar Kana', '-', '-'),
    ('مَا', 'Selama belum', '-', '-', '-', '-', 'Huruf Mashdariyah Zharfiyah', '-', '-'),
    ('لَمْ', 'Belum', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَحْضُرِ', 'Tiba/Hadir', 'ح ض ر', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mujarrad', 'Al-Ashr'),
    ('الْعَصْرُ».', 'Waktu Ashar».', 'ع ص ر', '-', '-', '-', 'Fa\'il', '-', '-')
]
# Breaks: 'زَالَتِ' (11)
blocks_107.append({
    'type': 'paragraph',
    'ar': 'رَوَى مُسْلِمٌ (٦١٢) أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «وَقْتُ الظُّهْرِ إِذَا زَالَتِ الشَّمْسُ، وَكَانَ ظِلُّ الرَّجُلِ كَطُولِهِ، مَا لَمْ يَحْضُرِ الْعَصْرُ».',
    'id': 'Muslim telah meriwayatkan (612) bahwasanya Rasulullah SAW bersabda: "Waktu pelaksanaan shalat Zhuhur adalah ketika matahari telah tergelincir (ke arah barat), dan (waktunya berlangsung) hingga bayangan seseorang menjadi sama panjang dengan ukuran tinggi badannya, selama waktu shalat Ashar belum tiba".',
    'words': make_words(p3_words, [11])
})


# Heading: «الْعَصْرُ»:
h2_words = [
    ('«الْعَصْرُ»:', '«Waktu Ashar»:', 'ع ص ر', '-', '-', '-', 'Mubtada\'', '-', '-')
]
blocks_107.append({'type': 'heading', 'ar': '«الْعَصْرُ»:', 'id': 'Waktu Shalat Ashar:', 'words': make_words(h2_words, [])})

# Para 4 (Waqtu Ashar)
# يَبْتَدِىءُ وَقْتُهُ بِنِهَايَةِ وَقْتِ الظُّهْرِ، وَيَسْتَمِرُّ حَتَّى تَغْرُبَ الشَّمْسُ، دَلَّ
# عَلَى ذَلِكَ قَوْلُهُ ﷺ : «وَمَنْ أَدْرَكَ رَكْعَةً مِنَ الْعَصْرِ قَبْلَ أَنْ تَغْرُبَ الشَّمْسُ
# فَقَدْ أَدْرَكَ الْعَصْرَ» (رواه البخاري: ٥٥٤؛ ومسلم: ٦٠٨).
p4_words = [
    ('يَبْتَدِىءُ', 'Ia mulai masuk', 'ب د أ', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Waqtuhu'),
    ('وَقْتُهُ', 'Waktunya', 'و ق ت', '-', 'Waqtu + hu', 'hu merujuk ke shalat ashar', 'Fa\'il', '-', '-'),
    ('بِنِهَايَةِ', 'Seiring berakhirnya', 'ن ه ي', '-', 'Baa jar + Nihayah', '-', 'Jar Majrur', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الظُّهْرِ،', 'Zhuhur,', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَيَسْتَمِرُّ', 'Dan akan terus berlanjut', 'م ر ر', '-', 'Wawu + Yastamirru', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Waqtuhu'),
    ('حَتَّى', 'Sampai', '-', '-', '-', '-', 'Huruf Jar / Ghayah', '-', '-'),
    ('تَغْرُبَ', 'Terbenamnya', 'غ ر ب', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('الشَّمْسُ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('دَلَّ', 'Telah menunjukkan', 'د ل ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Qauluhu'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ذَلِكَ', 'Hal tersebut', 'ذ ل ك', '-', '-', '-', 'Majrur', '-', '-'),
    ('قَوْلُهُ', 'Sabda beliau', 'ق و ل', '-', 'Qaulu + hu', 'hu merujuk ke Nabi', 'Fa\'il', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«وَمَنْ', '«Dan barangsiapa yang', '-', '-', 'Wawu + Man', '-', 'Isim Syarat', '-', '-'),
    ('أَدْرَكَ', 'Mendapati (masih sempat melakukan)', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mazid', 'Man'),
    ('رَكْعَةً', 'Satu rakaat', 'ر ك ع', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْعَصْرِ', 'Shalat ashar', 'ع ص ر', '-', '-', '-', 'Majrur', '-', '-'),
    ('قَبْلَ', 'Sebelum', 'ق ب ل', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('تَغْرُبَ', 'Akan terbenamnya', 'غ ر ب', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('الشَّمْسُ', 'Matahari', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa (Jawab) + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('أَدْرَكَ', 'Ia telah mendapati', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mazid', 'Man'),
    ('الْعَصْرَ»', 'Shalat ashar seutuhnya»', 'ع ص ر', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('البخاري:', 'Al-Bukhari:', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٥٥٤؛', '554;', '-', '-', '-', '-', '-', '-', '-'),
    ('ومسلم:', 'Dan Muslim:', 'س ل م', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('٦٠٨).', '608).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'دَلَّ' (9), 'الشَّمْسُ' (23)
blocks_107.append({
    'type': 'paragraph',
    'ar': 'يَبْتَدِىءُ وَقْتُهُ بِنِهَايَةِ وَقْتِ الظُّهْرِ، وَيَسْتَمِرُّ حَتَّى تَغْرُبَ الشَّمْسُ، دَلَّ عَلَى ذَلِكَ قَوْلُهُ ﷺ : «وَمَنْ أَدْرَكَ رَكْعَةً مِنَ الْعَصْرِ قَبْلَ أَنْ تَغْرُبَ الشَّمْسُ فَقَدْ أَدْرَكَ الْعَصْرَ» (رواه البخاري: ٥٥٤؛ ومسلم: ٦٠٨).',
    'id': 'Waktunya (Ashar) mulai masuk seketika usainya batas waktu Zhuhur, dan akan terus berlanjut hingga matahari terbenam seutuhnya. Hal ini ditunjukkan (dalilnya) oleh sabda beliau SAW: "Dan barangsiapa yang (masih) mendapati satu rakaat (yang sah) dari shalat Ashar sebelum matahari terbenam, maka sungguh ia telah mendapati shalat Ashar secara utuh (tidak dianggap terlewat/qadha)" (HR. Al-Bukhari: 554; dan Muslim: 608).',
    'words': make_words(p4_words, [9, 23])
})

# Para 5 (Al-Ikhtiyar li waqtil Ashar)
# وَلَكِنَّ الِاخْتِيَارَ أَنْ لَا يُؤَخِّرَهَا الْمُصَلِّي عَنْ مَصِيرِ ظِلِّ الشَّيْءِ مِثْلَيْهِ
# عِلَاوَةً عَلَى ظِلِّ الزَّوَالِ؛ لِمَا مَرَّ مَعَكَ فِي حَدِيثِ الْمَوَاقِيتِ، وَلِقَوْلِهِ ﷺ :
# «وَوَقْتُ الْعَصْرِ مَا لَمْ تَصْفَرَّ الشَّمْسُ» (رواه مسلم: ٦١٢). وَهُوَ مَحْمُولٌ
# عَلَى الْوَقْتِ الْمُخْتَارِ.
p5_words = [
    ('وَلَكِنَّ', 'Akan tetapi sesungguhnya', 'ل ك ن', '-', 'Wawu + Lakinna', '-', 'Amil Nawasikh', '-', '-'),
    ('الِاخْتِيَارَ', 'Hal yang ideal/pilihan utama', 'خ ي ر', '-', '-', '-', 'Isim Lakinna', '-', '-'),
    ('أَنْ', 'Ialah hendaknya', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('لَا', 'Janganlah', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يُؤَخِّرَهَا', 'Mengakhirkannya', 'أ خ ر', '-', 'Yu\'akkhira + ha', 'ha merujuk ke shalat', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mazid', 'Al-Mushalli'),
    ('الْمُصَلِّي', 'Orang yang shalat', 'ص ل ي', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَنْ', 'Hingga melebihi (dari)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مَصِيرِ', 'Proses menjadinya', 'ص ي ر', '-', '-', '-', 'Majrur / Mashdar', '-', '-'),
    ('ظِلِّ', 'Bayangan', 'ظ ل ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّيْءِ', 'Suatu benda', 'ش ي أ', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مِثْلَيْهِ', 'Dua kali lipat ukuran (benda tsb)', 'م ث ل', 'Mutsanna', 'Mitslai + hi', 'hi merujuk ke benda', 'Khabar dari mashdar / Hal', '-', '-'),
    ('عِلَاوَةً', 'Sebagai tambahan', 'ع ل و', '-', '-', '-', 'Hal', '-', '-'),
    ('عَلَى', 'Selain dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ظِلِّ', 'Bayangan', 'ظ ل ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('الزَّوَالِ؛', 'Zawal;', 'ز و ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لِمَا', 'Karena dalil yang', '-', '-', 'Lam ta\'lil + Ma maushul', '-', 'Jar Majrur', '-', '-'),
    ('مَرَّ', 'Telah berlalu (disebutkan)', 'م ر ر', '-', '-', '-', 'Fi\'il Madhi (Shilah)', 'Tsulasi Mujarrad', 'Ma (Dalil)'),
    ('مَعَكَ', 'Bersamamu', 'م ع ي', '-', 'Ma\'a + ka', 'ka merujuk ke pembaca', 'Zharf Makan', '-', '-'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('حَدِيثِ', 'Hadits', 'ح د ث', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْمَوَاقِيتِ،', 'Tentang waktu-waktu (shalat Abu Musa),', 'و ق ت', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَلِقَوْلِهِ', 'Dan karena sabda beliau', 'ق و ل', '-', 'Wawu + Lam + Qaul + hi', 'hi merujuk ke Nabi', 'Jar Majrur', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«وَوَقْتُ', '«Dan waktu', 'و ق ت', '-', 'Wawu + Waqtu', '-', 'Mubtada\'', '-', '-'),
    ('الْعَصْرِ', 'Shalat Ashar', 'ع ص ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَا', 'Selama', '-', '-', '-', '-', 'Huruf Mashdariyah Zharfiyah', '-', '-'),
    ('لَمْ', 'Belum (tidak)', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('تَصْفَرَّ', 'Menguning', 'ص ف ر', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mazid', 'Asy-Syamsu'),
    ('الشَّمْسُ»', 'Matahari»', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('مسلم:', 'Muslim:', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٦١٢).', '612).', '-', '-', '-', '-', '-', '-', '-'),
    ('وَهُوَ', 'Dan hal ini (hadits)', '-', '-', 'Wawu + Hua', 'Hua merujuk ke batas waktu di hadits', 'Mubtada\'', '-', '-'),
    ('مَحْمُولٌ', 'Diarahkan pemaknaannya', 'ح م ل', '-', '-', '-', 'Khabar', '-', '-'),
    ('عَلَى', 'Kepada batas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْوَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْمُخْتَارِ.', 'Al-Mukhtar (pilihan/ideal).', 'خ ي ر', '-', '-', '-', 'Na\'at', '-', '-')
]
# Breaks: 'مِثْلَيْهِ' (10), 'ﷺ :' (23), 'مَحْمُولٌ' (34)
blocks_107.append({
    'type': 'paragraph',
    'ar': 'وَلَكِنَّ الِاخْتِيَارَ أَنْ لَا يُؤَخِّرَهَا الْمُصَلِّي عَنْ مَصِيرِ ظِلِّ الشَّيْءِ مِثْلَيْهِ عِلَاوَةً عَلَى ظِلِّ الزَّوَالِ؛ لِمَا مَرَّ مَعَكَ فِي حَدِيثِ الْمَوَاقِيتِ، وَلِقَوْلِهِ ﷺ : «وَوَقْتُ الْعَصْرِ مَا لَمْ تَصْفَرَّ الشَّمْسُ» (رواه مسلم: ٦١٢). وَهُوَ مَحْمُولٌ عَلَى الْوَقْتِ الْمُخْتَارِ.',
    'id': 'Akan tetapi hal yang ikhtiyar (idealnya/pilihan utama) bagi orang yang shalat adalah jangan sampai ia mengakhirkannya (menunda Ashar) hingga panjang bayangan suatu benda mencapai dua kali lipat panjang bendanya (di luar panjang "Bayangan Zawal"). Hal ini didasarkan pada Hadits Al-Mawaqit (Hadits Abu Musa) yang telah lalu penyebutannya kepadamu, dan juga berdasar pada sabda beliau SAW: "Dan waktu shalat Ashar berlanjut selama matahari belum menguning" (HR. Muslim: 612). Pembatasan dalam hadits ini secara khusus diarahkan pada kategori "Waktu Mukhtar" (waktu pilihan yang dianjurkan).',
    'words': make_words(p5_words, [10, 23, 34])
})


# Heading: «الْمَغْرِبُ»:
h3_words = [
    ('«الْمَغْرِبُ»:', '«Waktu Maghrib»:', 'غ ر ب', '-', '-', '-', 'Mubtada\'', '-', '-')
]
blocks_107.append({'type': 'heading', 'ar': '«الْمَغْرِبُ»:', 'id': 'Waktu Shalat Maghrib:', 'words': make_words(h3_words, [])})

# Para 6 (Waqtu Maghrib)
# يَبْتَدِىءُ وَقْتُهُ بِغُرُوبِ الشَّمْسِ، وَيَمْتَدُّ حَتَّى يَغِيبَ الشَّفَقُ الْأَحْمَرُ
# وَلَا يَبْقَى لَهُ أَثَرٌ فِي جِهَةِ الْغَرْبِ.
p6_words = [
    ('يَبْتَدِىءُ', 'Ia mulai masuk', 'ب د أ', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Waqtuhu'),
    ('وَقْتُهُ', 'Waktunya', 'و ق ت', '-', 'Waqtu + hu', 'hu merujuk ke shalat maghrib', 'Fa\'il', '-', '-'),
    ('بِغُرُوبِ', 'Dengan terbenamnya', 'غ ر ب', '-', 'Baa jar + Ghurub', '-', 'Jar Majrur', '-', '-'),
    ('الشَّمْسِ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَيَمْتَدُّ', 'Dan membentang (berlanjut)', 'م د د', '-', 'Wawu + Yamtaddu', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Waqtuhu'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar / Ghayah', '-', '-'),
    ('يَغِيبَ', 'Hilang/lenyapnya', 'غ ي ب', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Asy-Syafaq'),
    ('الشَّفَقُ', 'Mega', 'ش ف ق', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('الْأَحْمَرُ', 'Merah', 'ح م ر', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَلَا', 'Dan tidak ada lagi', '-', '-', 'Wawu + Laa', '-', 'Huruf Nafi', '-', '-'),
    ('يَبْقَى', 'Tersisa', 'ب ق ي', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Atsarun'),
    ('لَهُ', 'Baginya (mega merah)', '-', '-', 'Lam jar + hu', 'hu merujuk ke mega', 'Jar Majrur', '-', '-'),
    ('أَثَرٌ', 'Jejak sedikitpun', 'أ ث ر', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('فِي', 'Di', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('جِهَةِ', 'Sisi ufuk', 'ج ه ه', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْغَرْبِ.', 'Barat.', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-')
]
# Breaks: 'الْأَحْمَرُ' (8)
blocks_107.append({
    'type': 'paragraph',
    'ar': 'يَبْتَدِىءُ وَقْتُهُ بِغُرُوبِ الشَّمْسِ، وَيَمْتَدُّ حَتَّى يَغِيبَ الشَّفَقُ الْأَحْمَرُ وَلَا يَبْقَى لَهُ أَثَرٌ فِي جِهَةِ الْغَرْبِ.',
    'id': 'Waktunya (Maghrib) masuk seketika matahari terbenam (hilangnya bulatan matahari di ufuk secara utuh), dan berlanjut hingga hilangnya cahaya mega merah (syafaq), dan tak ada lagi jejak semburat merah sedikitpun yang tersisa di ufuk bagian barat.',
    'words': make_words(p6_words, [8])
})


data.append({
    'pageNumber': 107,
    'blocks': blocks_107
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 107 appended to data.js successfully.')
