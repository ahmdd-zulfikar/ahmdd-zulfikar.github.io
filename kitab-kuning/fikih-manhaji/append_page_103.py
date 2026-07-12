import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_103 = []

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

# Para 1 (Continuation of Hadith Mu'adz from page 102)
# Text:
# أَطَاعُوا لِذَلِكَ فَأَعْلِمْهُمْ أَنَّ اللَّهَ قَدِ افْتَرَضَ عَلَيْهِمْ خَمْسَ صَلَوَاتٍ فِي كُلِّ
# يَوْمٍ وَلَيْلَةٍ...».
p1_words = [
    ('أَطَاعُوا', 'Mereka taat', 'ط و ع', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Penduduk Yaman (Wawu)'),
    ('لِذَلِكَ', 'Akan hal itu', 'ذ ل ك', '-', 'Lam jar + Dzalika', '-', 'Jar Majrur', '-', '-'),
    ('فَأَعْلِمْهُمْ', 'Maka beritahukanlah mereka', 'ع ل م', '-', 'Fa + A\'lim + hum', 'hum merujuk ke Penduduk Yaman', 'Fi\'il Amr', 'Tsulasi Mazid', 'Muadz (Anta)'),
    ('أَنَّ', 'Bahwa sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('اللَّهَ', 'Allah', '-', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('قَدِ', 'Sungguh', '-', '-', '-', '-', 'Huruf Tahqiq', '-', '-'),
    ('افْتَرَضَ', 'Telah mewajibkan', 'ف ر ض', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Allah'),
    ('عَلَيْهِمْ', 'Atas mereka', '-', '-', 'Ala + him', 'him merujuk ke Penduduk Yaman', 'Jar Majrur', '-', '-'),
    ('خَمْسَ', 'Lima', 'خ م س', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('صَلَوَاتٍ', 'Waktu shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فِي', 'Dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('كُلِّ', 'Setiap', 'ك ل ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('يَوْمٍ', 'Sehari', 'ي و م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَلَيْلَةٍ...».', 'Dan semalam...».', 'ل ي ل', '-', 'Wawu + Lailah', '-', 'Ma\'thuf', '-', '-')
]
# Breaks: 'كُلِّ' is index 11
blocks_103.append({
    'type': 'paragraph',
    'ar': 'أَطَاعُوا لِذَلِكَ فَأَعْلِمْهُمْ أَنَّ اللَّهَ قَدِ افْتَرَضَ عَلَيْهِمْ خَمْسَ صَلَوَاتٍ فِي كُلِّ يَوْمٍ وَلَيْلَةٍ...».',
    'id': 'Mereka mentaati seruan itu, maka beritahukanlah kepada mereka bahwa Allah sungguh telah mewajibkan atas mereka shalat lima waktu dalam sehari semalam...".',
    'words': make_words(p1_words, [11])
})

# Para 2
# Text:
# وَقَوْلُهُ ﷺ لِلْأَعْرَابِيِّ الَّذِي سَأَلَهُ عَمَّا يَجِبُ عَلَيْهِ مِنَ الصَّلَاةِ:
# «خَمْسُ صَلَوَاتٍ فِي الْيَوْمِ وَاللَّيْلَةِ»، قَالَ الْأَعْرَابِيُّ: هَلْ عَلَيَّ غَيْرُهَا؟
# قَالَ: «لَا إِلَّا أَنْ تَطَوَّعَ» (رواه البخاري: ٤٦؛ ومسلم: ١١).
p2_words = [
    ('وَقَوْلُهُ', 'Dan sabda beliau', 'ق و ل', '-', 'Wawu + Qaul + hu', 'hu merujuk ke Rasulullah', 'Mubtada\'', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('لِلْأَعْرَابِيِّ', 'Kepada seorang Arab Badui', 'ع ر ب', '-', 'Lam jar + A\'rabi', '-', 'Jar Majrur', '-', '-'),
    ('الَّذِي', 'Yang', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('سَأَلَهُ', 'Bertanya kepada beliau', 'س أ ل', '-', 'Bersambung dhamir hu', 'hu merujuk ke Rasulullah', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'A\'rabi'),
    ('عَمَّا', 'Tentang apa yang', '-', '-', 'An + Ma', '-', 'Jar Majrur', '-', '-'),
    ('يَجِبُ', 'Wajib', 'و ج ب', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Apa yang wajib (Ma)'),
    ('عَلَيْهِ', 'Atasnya', '-', '-', 'Ala + hi', 'hi merujuk ke A\'rabi', 'Jar Majrur', '-', '-'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الصَّلَاةِ:', 'Shalat:', 'ص ل ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('«خَمْسُ', '«Lima', 'خ م س', '-', '-', '-', 'Khabar (dari mubtada\' mahdzuf)', '-', '-'),
    ('صَلَوَاتٍ', 'Waktu shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فِي', 'Dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْيَوْمِ', 'Sehari', 'ي و م', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَاللَّيْلَةِ»،', 'Dan semalam»,', 'ل ي ل', '-', 'Wawu + Lailah', '-', 'Ma\'thuf', '-', '-'),
    ('قَالَ', 'Berkatalah', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'A\'rabi'),
    ('الْأَعْرَابِيُّ:', 'Orang Arab Badui itu:', 'ع ر ب', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('هَلْ', 'Apakah', '-', '-', '-', '-', 'Huruf Istifham', '-', '-'),
    ('عَلَيَّ', 'Atasku (wajib)', '-', '-', 'Ala + Ya', 'Ya merujuk ke A\'rabi', 'Jar Majrur / Khabar Muqaddam', '-', '-'),
    ('غَيْرُهَا؟', 'Selainnya?', 'غ ي ر', '-', 'Bersambung dhamir ha', 'ha merujuk ke Shalat 5 waktu', 'Mubtada\' Muakhkhar', '-', '-'),
    ('قَالَ:', 'Beliau bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«لَا', '«Tidak', '-', '-', '-', '-', 'Huruf Nafi/Jawab', '-', '-'),
    ('إِلَّا', 'Kecuali', '-', '-', '-', '-', 'Huruf Istitsna\'', '-', '-'),
    ('أَنْ', 'Bahwa (jika)', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('تَطَوَّعَ»', 'Engkau melakukan yang sunnah»', 'ط و ع', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'A\'rabi (Anta)'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('البخاري:', 'Al-Bukhari:', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٤٦؛', '46;', '-', '-', '-', '-', '-', '-', '-'),
    ('ومسلم:', 'Dan Muslim:', 'س ل م', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('١١).', '11).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'الصَّلَاةِ:' (9), 'غَيْرُهَا؟' (19)
blocks_103.append({
    'type': 'paragraph',
    'ar': 'وَقَوْلُهُ ﷺ لِلْأَعْرَابِيِّ الَّذِي سَأَلَهُ عَمَّا يَجِبُ عَلَيْهِ مِنَ الصَّلَاةِ: «خَمْسُ صَلَوَاتٍ فِي الْيَوْمِ وَاللَّيْلَةِ»، قَالَ الْأَعْرَابِيُّ: هَلْ عَلَيَّ غَيْرُهَا؟ قَالَ: «لَا إِلَّا أَنْ تَطَوَّعَ» (رواه البخاري: ٤٦؛ ومسلم: ١١).',
    'id': 'Dan (dalil berikutnya adalah) sabda Nabi SAW kepada seorang Arab Badui yang bertanya kepada beliau tentang apa yang diwajibkan atasnya dari shalat (beliau menjawab): "Lima waktu shalat dalam sehari semalam". Orang Arab Badui itu bertanya lagi: "Apakah ada kewajiban shalat lain atasku selain itu?" Beliau menjawab: "Tidak ada, kecuali engkau mengerjakan shalat sunnah." (HR. Bukhari no. 46; dan Muslim no. 11).',
    'words': make_words(p2_words, [9, 19])
})

# Heading 1
# مَكَانَتُهَا فِي الدِّينِ :
h1_words = [
    ('مَكَانَتُهَا', 'Kedudukannya', 'ك و ن', '-', 'Bersambung dhamir ha', 'ha merujuk ke Shalat', 'Mubtada\'', '-', '-'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الدِّينِ', 'Agama', 'د ي ن', '-', '-', '-', 'Majrur', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_103.append({'type': 'heading', 'ar': 'مَكَانَتُهَا فِي الدِّينِ :', 'id': 'Kedudukan Shalat Dalam Agama:', 'words': make_words(h1_words, [])})

# Para 3
# Text:
# الصَّلَاةُ أَفْضَلُ الْعِبَادَاتِ الْبَدَنِيَّةِ عَلَى الْإِطْلَاقِ؛ فَقَدْ جَاءَ رَجُلٌ يَسْأَلُ
# النَّبِيَّ ﷺ عَنْ أَفْضَلِ الْأَعْمَالِ فَقَالَ لَهُ: «الصَّلَاةُ» قَالَ: ثُمَّ مَهْ؟ قَالَ: «ثُمَّ
# الصَّلَاةُ» قَالَ: ثُمَّ مَهْ؟ قَالَ: «الصَّلَاةُ» ثَلَاثَ مَرَّاتٍ. (رواه
# ابن حبان: ٢٥٨).
p3_words = [
    ('الصَّلَاةُ', 'Shalat itu', 'ص ل ي', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('أَفْضَلُ', 'Paling utama(nya)', 'ف ض ل', '-', '-', '-', 'Khabar', '-', '-'),
    ('الْعِبَادَاتِ', 'Ibadah-ibadah', 'ع ب د', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْبَدَنِيَّةِ', 'Fisik/Badan', 'ب د ن', '-', '-', '-', 'Na\'at', '-', '-'),
    ('عَلَى', 'Secara', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْإِطْلَاقِ؛', 'Mutlak;', 'ط ل ق', '-', '-', '-', 'Majrur', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('جَاءَ', 'Telah datang', 'ج ي أ', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rajulun'),
    ('رَجُلٌ', 'Seorang pria', 'ر ج ل', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('يَسْأَلُ', 'Bertanya', 'س أ ل', '-', '-', '-', 'Fi\'il Mudhari\' (Hal)', 'Tsulasi Mujarrad', 'Rajulun'),
    ('النَّبِيَّ', 'Kepada Nabi', 'ن ب أ', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Tentang', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَفْضَلِ', 'Paling utama(nya)', 'ف ض ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْأَعْمَالِ', 'Amalan-amalan', 'ع م ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَقَالَ', 'Maka beliau bersabda', 'ق و ل', '-', 'Fa + Qala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('لَهُ:', 'Kepadanya:', '-', '-', 'Lam jar + hu', 'hu merujuk ke pria penanya', 'Jar Majrur', '-', '-'),
    ('«الصَّلَاةُ»', '«Shalat»', 'ص ل ي', '-', '-', '-', 'Khabar (mubtada mahdzuf)', '-', '-'),
    ('قَالَ:', 'Pria itu bertanya:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rajulun'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('مَهْ؟', 'Apa? (lalu apa lagi?)', '-', '-', '-', '-', 'Isim Istifham', '-', '-'),
    ('قَالَ:', 'Beliau bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«ثُمَّ', '«Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('الصَّلَاةُ»', 'Shalat»', 'ص ل ي', '-', '-', '-', 'Khabar (mubtada mahdzuf)', '-', '-'),
    ('قَالَ:', 'Pria itu bertanya:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rajulun'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('مَهْ؟', 'Apa? (lalu apa lagi?)', '-', '-', '-', '-', 'Isim Istifham', '-', '-'),
    ('قَالَ:', 'Beliau bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«الصَّلَاةُ»', '«Shalat»', 'ص ل ي', '-', '-', '-', 'Khabar (mubtada mahdzuf)', '-', '-'),
    ('ثَلَاثَ', 'Tiga', 'ث ل ث', '-', '-', '-', 'Maf\'ul Muthlaq / Na\'ib', '-', '-'),
    ('مَرَّاتٍ.', 'Kali.', 'م ر ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('ابن', 'Ibnu', 'ب ن ي', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('حبان:', 'Hibban:', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('٢٥٨).', '258).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'يَسْأَلُ' (9), '«ثُمَّ' (22), '(رواه' (31)
blocks_103.append({
    'type': 'paragraph',
    'ar': 'الصَّلَاةُ أَفْضَلُ الْعِبَادَاتِ الْبَدَنِيَّةِ عَلَى الْإِطْلَاقِ؛ فَقَدْ جَاءَ رَجُلٌ يَسْأَلُ النَّبِيَّ ﷺ عَنْ أَفْضَلِ الْأَعْمَالِ فَقَالَ لَهُ: «الصَّلَاةُ» قَالَ: ثُمَّ مَهْ؟ قَالَ: «ثُمَّ الصَّلَاةُ» قَالَ: ثُمَّ مَهْ؟ قَالَ: «الصَّلَاةُ» ثَلَاثَ مَرَّاتٍ. (رواه ابن حبان: ٢٥٨).',
    'id': 'Shalat adalah ibadah fisik (badaniyah) yang paling utama secara mutlak. Sungguh telah datang seorang pria bertanya kepada Nabi SAW tentang amal apakah yang paling utama, lalu beliau menjawab: "Shalat." Pria itu bertanya lagi: "Kemudian apa (amal apa lagi)?" Beliau menjawab: "Kemudian shalat." Pria itu bertanya lagi: "Kemudian apa?" Beliau menjawab: "Shalat." (Diucapkan) sampai tiga kali. (HR. Ibnu Hibban: 258).',
    'words': make_words(p3_words, [9, 22, 31])
})

# Para 4
# Text:
# وَقَدْ ثَبَتَ فِي الصَّحِيحَيْنِ أَنَّ الصَّلَاتَيْنِ يُؤَدِّيهِمَا الْمُسْلِمُ أَدَاءً سَلِيماً
# تَكُونَانِ كَفَّارَةً لِمَا بَيْنَهُمَا مِنَ الذُّنُوبِ؛ فَعِنْدَ الْبُخَارِيِّ (٥٠٥)، عَنْ
# أَبِي هُرَيْرَةَ رضي الله عنه قَالَ: قَالَ رَسُولُ اللهِ ﷺ : «الصَّلَوَاتُ الْخَمْسُ
# يَمْحُو اللَّهُ بِهَا الْخَطَايَا».
p4_words = [
    ('وَقَدْ', 'Dan sungguh', '-', '-', 'Wawu + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('ثَبَتَ', 'Telah tetap/shahih', 'ث ب ت', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Khabar (Isi Hadits)'),
    ('فِي', 'Dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الصَّحِيحَيْنِ', 'Kitab Shahihain (Bukhari Muslim)', 'ص ح ح', '-', '-', '-', 'Majrur', '-', '-'),
    ('أَنَّ', 'Bahwa', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('الصَّلَاتَيْنِ', 'Dua shalat', 'ص ل ي', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('يُؤَدِّيهِمَا', 'Yang ditunaikan', 'أ د ي', '-', 'Yu\'addi + huma', 'huma merujuk ke dua shalat', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Al-Muslim'),
    ('الْمُسْلِمُ', 'Oleh seorang muslim', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('أَدَاءً', 'Dengan penunaian', 'أ د ي', '-', '-', '-', 'Maf\'ul Muthlaq', '-', '-'),
    ('سَلِيماً', 'Yang sempurna/baik', 'س ل م', '-', '-', '-', 'Na\'at', '-', '-'),
    ('تَكُونَانِ', 'Keduanya menjadi', 'ك و ن', '-', 'Takunu + Alif Itsnain', 'Alif merujuk ke dua shalat', 'Fi\'il Mudhari\' Naqish (Khabar Anna)', 'Tsulasi Mujarrad', 'Keduanya (Alif)'),
    ('كَفَّارَةً', 'Penghapus (dosa)', 'ك ف ر', '-', '-', '-', 'Khabar Takunu', '-', '-'),
    ('لِمَا', 'Bagi apa-apa (dosa)', '-', '-', 'Lam jar + Ma', '-', 'Jar Majrur', '-', '-'),
    ('بَيْنَهُمَا', 'Di antara keduanya', 'ب ي ن', '-', 'Baina + huma', 'huma merujuk ke dua shalat', 'Zharf Makan', '-', '-'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الذُّنُوبِ؛', 'Dosa-dosa;', 'ذ ن ب', '-', '-', '-', 'Majrur', '-', '-'),
    ('فَعِنْدَ', 'Maka dalam (riwayat)', 'ع ن د', '-', 'Fa + Inda', '-', 'Zharf Makan', '-', '-'),
    ('الْبُخَارِيِّ', 'Al-Bukhari', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('(٥٠٥)،', '(505),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَبِي', 'Abu', 'أ ب و', '-', '-', '-', 'Majrur', '-', '-'),
    ('هُرَيْرَةَ', 'Hurairah', 'ه ر ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Abu Hurairah', 'Jar Majrur', '-', '-'),
    ('قَالَ:', 'Berkata:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Abu Hurairah'),
    ('قَالَ', 'Telah bersabda', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('رَسُولُ', 'Utusan', 'ر س ل', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«الصَّلَوَاتُ', '«Shalat-shalat', 'ص ل ي', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الْخَمْسُ', 'Lima waktu', 'خ م س', '-', '-', '-', 'Na\'at', '-', '-'),
    ('يَمْحُو', 'Menghapus', 'م ح و', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Allah'),
    ('اللَّهُ', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('بِهَا', 'Dengannya', '-', '-', 'Baa + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('الْخَطَايَا».', 'Kesalahan-kesalahan/dosa-dosa».', 'خ ط أ', '-', '-', '-', 'Maf\'ul Bih', '-', '-')
]
# Breaks: 'سَلِيماً' (9), 'عَنْ' (19), 'الْخَمْسُ' (32)
blocks_103.append({
    'type': 'paragraph',
    'ar': 'وَقَدْ ثَبَتَ فِي الصَّحِيحَيْنِ أَنَّ الصَّلَاتَيْنِ يُؤَدِّيهِمَا الْمُسْلِمُ أَدَاءً سَلِيماً تَكُونَانِ كَفَّارَةً لِمَا بَيْنَهُمَا مِنَ الذُّنُوبِ؛ فَعِنْدَ الْبُخَارِيِّ (٥٠٥)، عَنْ أَبِي هُرَيْرَةَ رضي الله عنه قَالَ: قَالَ رَسُولُ اللهِ ﷺ : «الصَّلَوَاتُ الْخَمْسُ يَمْحُو اللَّهُ بِهَا الْخَطَايَا».',
    'id': 'Dan sungguh telah tsabit (shahih) di dalam kitab Shahihain (Bukhari-Muslim) bahwa dua shalat yang ditunaikan oleh seorang muslim dengan penunaian yang baik/sempurna, niscaya keduanya akan menjadi penggugur dosa-dosa yang terjadi di antara keduanya; Dan dalam riwayat Al-Bukhari (505), dari Abu Hurairah RA ia berkata: Rasulullah SAW bersabda: "Shalat lima waktu itu Allah jadikan untuk menghapus dosa-dosa (kesalahan).',
    'words': make_words(p4_words, [9, 19, 32])
})

# Para 5
# Text:
# وَعِنْدَ مُسْلِمٍ (٢٣١)، عَنْ عُثْمَانَ رضي الله عنه قَالَ: قَالَ رَسُولُ
# اللهِ ﷺ : «مَنْ أَتَمَّ الْوُضُوءَ كَمَا أَمَرَهُ اللَّهُ تَعَالَى فَالصَّلَوَاتُ الْمَكْتُوبَاتُ
# كَفَّارَاتٌ لِمَا بَيْنَهُنَّ».
p5_words = [
    ('وَعِنْدَ', 'Dan di dalam riwayat', 'ع ن د', '-', 'Wawu + Inda', '-', 'Zharf Makan', '-', '-'),
    ('مُسْلِمٍ', 'Muslim', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('(٢٣١)،', '(231),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('عُثْمَانَ', 'Utsman', 'ع ث م', '-', '-', '-', 'Majrur', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Utsman', 'Jar Majrur', '-', '-'),
    ('قَالَ:', 'Berkata:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Utsman'),
    ('قَالَ', 'Telah bersabda', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('رَسُولُ', 'Utusan', 'ر س ل', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«مَنْ', '«Barangsiapa yang', '-', '-', '-', '-', 'Isim Syarat', '-', '-'),
    ('أَتَمَّ', 'Menyempurnakan', 'ت م م', '-', '-', '-', 'Fi\'il Madhi (Fi\'il Syarat)', 'Tsulasi Mazid', 'Man (Siapa saja)'),
    ('الْوُضُوءَ', 'Wudhu', 'و ض أ', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('كَمَا', 'Sebagaimana yang', '-', '-', 'Kaf jar + Ma maushul', '-', 'Jar Majrur', '-', '-'),
    ('أَمَرَهُ', 'Diperintahkan padanya oleh', 'أ م ر', '-', 'Amara + hu', 'hu merujuk ke Man (si pembuat wudhu)', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('اللَّهُ', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('تَعَالَى', 'Yang Maha Tinggi', 'ع ل و', '-', '-', '-', 'Fi\'il Madhi (Hal)', 'Tsulasi Mazid', 'Allah'),
    ('فَالصَّلَوَاتُ', 'Maka shalat-shalat', 'ص ل ي', '-', 'Fa + As-Shalawat', '-', 'Mubtada\' (Jawab Syarat)', '-', '-'),
    ('الْمَكْتُوبَاتُ', 'Yang fardhu (diwajibkan)', 'ك ت ب', '-', '-', '-', 'Na\'at', '-', '-'),
    ('كَفَّارَاتٌ', 'Menjadi pelebur/penghapus dosa', 'ك ف ر', '-', '-', '-', 'Khabar', '-', '-'),
    ('لِمَا', 'Bagi apa yang', '-', '-', 'Lam jar + Ma maushul', '-', 'Jar Majrur', '-', '-'),
    ('بَيْنَهُنَّ».', 'Di antara mereka (waktu shalat)».', 'ب ي ن', '-', 'Baina + hunna', 'hunna merujuk ke shalat-shalat', 'Zharf Makan', '-', '-')
]
# Breaks: 'رَسُولُ' (10), 'الْمَكْتُوبَاتُ' (22)
blocks_103.append({
    'type': 'paragraph',
    'ar': 'وَعِنْدَ مُسْلِمٍ (٢٣١)، عَنْ عُثْمَانَ رضي الله عنه قَالَ: قَالَ رَسُولُ اللهِ ﷺ : «مَنْ أَتَمَّ الْوُضُوءَ كَمَا أَمَرَهُ اللَّهُ تَعَالَى فَالصَّلَوَاتُ الْمَكْتُوبَاتُ كَفَّارَاتٌ لِمَا بَيْنَهُنَّ».',
    'id': 'Dan dalam riwayat Muslim (231), dari Utsman RA ia berkata: Rasulullah SAW bersabda: "Barangsiapa yang menyempurnakan wudhu sebagaimana yang diperintahkan oleh Allah Ta\'ala kepadanya, maka shalat-shalat fardhu itu akan menjadi pelebur dosa bagi (kesalahan-kesalahan) yang terjadi di antara waktu-waktunya".',
    'words': make_words(p5_words, [10, 22])
})

# Para 6
# Text:
# كَمَا أَنَّ التَّهَاوُنَ فِي الصَّلَاةِ تَأْخِيراً أَوْ تَرْكاً، مِنْ شَأْنِهِ أَنْ يُؤَدِّيَ
# بِصَاحِبِهِ - إِنْ هُوَ اسْتَمَرَّ عَلَى ذَلِكَ - إِلَى الْكُفْرِ. إِذَا الصَّلَاةُ هِيَ الْغِذَاءُ
# الْأَوَّلُ لِلْإِيمَانِ كَمَا قَدْ عَلِمْتَ.
p6_words = [
    ('كَمَا', 'Sebagaimana pula', '-', '-', 'Kaf jar + Ma', '-', 'Jar Majrur', '-', '-'),
    ('أَنَّ', 'Sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('التَّهَاوُنَ', 'Meremehkan/Mengabaikan', 'ه و ن', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('فِي', 'Dalam hal', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('تَأْخِيراً', 'Dengan mengakhir-akhirkannya', 'أ خ ر', '-', '-', '-', 'Tamyiz / Maf\'ul liajlih', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('تَرْكاً،', 'Meninggalkannya sama sekali,', 'ت ر ك', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('مِنْ', 'Termasuk dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('شَأْنِهِ', 'Dampaknya/Akibatnya', 'ش أ ن', '-', 'Bersambung dhamir hi', 'hi merujuk ke perbuatan meremehkan', 'Jar Majrur / Khabar Anna', '-', '-'),
    ('أَنْ', 'Bahwa hal itu akan', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('يُؤَدِّيَ', 'Membawa/Menjerumuskan', 'أ د ي', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'At-Tahawun (Meremehkan)'),
    ('بِصَاحِبِهِ', 'Pelakunya', 'ص ح ب', '-', 'Baa jar + Shahib + hi', 'hi merujuk ke At-Tahawun', 'Jar Majrur', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('إِنْ', 'Jika', '-', '-', '-', '-', 'Huruf Syarat', '-', '-'),
    ('هُوَ', 'Dia', '-', '-', '-', 'Merujuk ke Pelaku', 'Mubtada\'', '-', '-'),
    ('اسْتَمَرَّ', 'Terus-menerus', 'م ر ر', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Hua'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ذَلِكَ', 'Hal tersebut', 'ذ ل ك', '-', '-', '-', 'Majrur', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('إِلَى', 'Ke dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْكُفْرِ.', 'Kekufuran.', 'ك ف ر', '-', '-', '-', 'Majrur', '-', '-'),
    ('إِذَا', 'Karena', '-', '-', '-', '-', 'Huruf Ta\'lil', '-', '-'),
    ('الصَّلَاةُ', 'Shalat itu', 'ص ل ي', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('هِيَ', 'Adalah', '-', '-', 'Dhamir Fashl', '-', '-', '-', '-'),
    ('الْغِذَاءُ', 'Nutrisi/Asupan gizi', 'غ ذ و', '-', '-', '-', 'Khabar', '-', '-'),
    ('الْأَوَّلُ', 'Yang pertama', 'أ و ل', '-', '-', '-', 'Na\'at', '-', '-'),
    ('لِلْإِيمَانِ', 'Bagi keimanan', 'أ م ن', '-', 'Lam jar + Iman', '-', 'Jar Majrur', '-', '-'),
    ('كَمَا', 'Sebagaimana yang', '-', '-', 'Kaf jar + Ma', '-', 'Jar Majrur', '-', '-'),
    ('قَدْ', 'Sungguh telah', '-', '-', '-', '-', 'Huruf Tahqiq', '-', '-'),
    ('عَلِمْتَ.', 'Engkau ketahui.', 'ع ل م', '-', 'Alima + ta', 'ta merujuk ke pembaca', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Engkau (Ta)')
]
# Breaks: 'يُؤَدِّيَ' (11), 'الْغِذَاءُ' (25)
blocks_103.append({
    'type': 'paragraph',
    'ar': 'كَمَا أَنَّ التَّهَاوُنَ فِي الصَّلَاةِ تَأْخِيراً أَوْ تَرْكاً، مِنْ شَأْنِهِ أَنْ يُؤَدِّيَ بِصَاحِبِهِ - إِنْ هُوَ اسْتَمَرَّ عَلَى ذَلِكَ - إِلَى الْكُفْرِ. إِذَا الصَّلَاةُ هِيَ الْغِذَاءُ الْأَوَّلُ لِلْإِيمَانِ كَمَا قَدْ عَلِمْتَ.',
    'id': 'Sebagaimana pula sikap meremehkan shalat (entah dengan cara menunda-nunda apalagi meninggalkannya), berpotensi kuat menjerumuskan pelakunya - jika ia terus-menerus di atas perbuatannya itu - ke dalam kekufuran. Karena shalat adalah nutrisi asupan gizi utama bagi sebuah keimanan sebagaimana yang telah engkau ketahui.',
    'words': make_words(p6_words, [11, 25])
})

# Para 7
# Text:
# رَوَى الْإِمَامُ أَحْمَدُ (٦/ ٤٢١)، عَنْ أُمِّ أَيْمَنَ رضي الله عنها أَنَّ
p7_words = [
    ('رَوَى', 'Telah meriwayatkan', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Imam Ahmad'),
    ('الْإِمَامُ', 'Imam', 'أ م م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('أَحْمَدُ', 'Ahmad', 'ح م د', '-', '-', '-', 'Badal', '-', '-'),
    ('(٦/ ٤٢١)،', '(Jilid 6 / Hal 421),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أُمِّ', 'Ummu', 'أ م م', '-', '-', '-', 'Majrur', '-', '-'),
    ('أَيْمَنَ', 'Aiman', 'ي م ن', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنها', 'Atasnya', '-', '-', 'An + ha', 'ha merujuk ke Ummu Aiman', 'Jar Majrur', '-', '-'),
    ('أَنَّ', 'Bahwa', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-')
]
# Breaks: 'أَنَّ' (10)
blocks_103.append({
    'type': 'paragraph',
    'ar': 'رَوَى الْإِمَامُ أَحْمَدُ (٦/ ٤٢١)، عَنْ أُمِّ أَيْمَنَ رضي الله عنها أَنَّ',
    'id': 'Telah meriwayatkan Imam Ahmad (6/421), dari Ummu Aiman RA, bahwasanya',
    'words': make_words(p7_words, [10])
})


data.append({
    'pageNumber': 103,
    'blocks': blocks_103
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 103 appended to data.js successfully.')
