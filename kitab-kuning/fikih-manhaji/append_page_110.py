import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_110 = []

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

# Para 1 (Continuation of Glossary)
# Text:
# يَكُونُ بَارِكاً فَيَقُومُ مِنْ شِدَّةِ حَرِّ الْأَرْضِ، فَصَارَ يُكْنَى بِهِ عَنْ شِدَّةِ الْحَرِّ.
# تَمِيلُ: عَنْ وَسَطِ السَّمَاءِ. تَضَيَّفُ: تَمِيلُ مُصْفَرَّةً وَتَقْرُبُ مِنَ الْغُرُوبِ].
p1_words = [
    ('يَكُونُ', 'Tadinya (unta itu)', 'ك و ن', '-', '-', '-', 'Fi\'il Mudhari\' Naqish', 'Tsulasi Mujarrad', 'Al-Ba\'ir'),
    ('بَارِكاً', 'Mendekam/menderum', 'ب ر ك', '-', '-', '-', 'Khabar Yakunu', '-', '-'),
    ('فَيَقُومُ', 'Lalu ia (terpaksa) berdiri', 'ق و م', '-', 'Fa + Yaqumu', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Ba\'ir'),
    ('مِنْ', 'Akibat (dari)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('شِدَّةِ', 'Sangatnya', 'ش د د', '-', '-', '-', 'Majrur', '-', '-'),
    ('حَرِّ', 'Panas', 'ح ر ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْأَرْضِ،', 'Bumi (pasir),', 'أ ر ض', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَصَارَ', 'Maka jadilah kata ini', 'ص ي ر', '-', 'Fa + Shara', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Kata Qaimud Dhahirah'),
    ('يُكْنَى', 'Dikiaskan', 'ك ن ي', '-', '-', '-', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mujarrad', 'Shara (Kata ini)'),
    ('بِهِ', 'Dengannya', '-', '-', 'Baa jar + hi', 'hi merujuk ke kata tsb', 'Jar Majrur', '-', '-'),
    ('عَنْ', 'Untuk menggambarkan', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('شِدَّةِ', 'Puncak sangatnya', 'ش د د', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْحَرِّ.', 'Rasa panas.', 'ح ر ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('تَمِيلُ:', 'Tamilu (Tergelincir):', 'م ي ل', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('عَنْ', 'Artinya bergeser dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('وَسَطِ', 'Tengah-tengah', 'و س ط', '-', '-', '-', 'Majrur / Khabar', '-', '-'),
    ('السَّمَاءِ.', 'Langit.', 'س م و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('تَضَيَّفُ:', 'Tadhayyafu (Telah condong):', 'ض ي ف', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('تَمِيلُ', 'Artinya ia bergeser', 'م ي ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Syams'),
    ('مُصْفَرَّةً', 'Dalam keadaan menguning', 'ص ف ر', '-', '-', '-', 'Hal', '-', '-'),
    ('وَتَقْرُبُ', 'Dan hampir (mendekati)', 'ق ر ب', '-', 'Wawu + Taqrubu', '-', 'Fi\'il Mudhari\' (Ma\'thuf)', 'Tsulasi Mujarrad', 'Syams'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْغُرُوبِ].', 'Waktu terbenam].', 'غ ر ب', '-', '-', '-', 'Majrur', '-', '-')
]
# Breaks: 'الْحَرِّ.' (12)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'يَكُونُ بَارِكاً فَيَقُومُ مِنْ شِدَّةِ حَرِّ الْأَرْضِ، فَصَارَ يُكْنَى بِهِ عَنْ شِدَّةِ الْحَرِّ. تَمِيلُ: عَنْ وَسَطِ السَّمَاءِ. تَضَيَّفُ: تَمِيلُ مُصْفَرَّةً وَتَقْرُبُ مِنَ الْغُرُوبِ].',
    'id': '...menderum (berhenti jalan), lalu terpaksa berdiri akibat sangat memuncaknya hawa panas di bumi. Maka kata ini pun dijadikan sebagai kiasan untuk menggambarkan kondisi cuaca yang sangat panas menyengat. "Tamilu": maksudnya tergelincir bergeser dari titik puncak langit. "Tadhayyafu": Maksudnya matahari tergelincir menguning dan hampir tenggelam].',
    'words': make_words(p1_words, [12])
})


# Para 2 (Condition of Karahah)
# وَهَذِهِ الْكَرَاهَةُ إِنْ لَمْ يَكُنْ لِلصَّلَاةِ سَبَبٌ مُتَقَدِّمٌ، أَوْ تَعَمُّدِ الدَّفْنِ
# فِيهَا.
p2_words = [
    ('وَهَذِهِ', 'Dan (hukum) ini', '-', '-', 'Wawu + Hadzihi', '-', 'Isim Isyarah / Mubtada\'', '-', '-'),
    ('الْكَرَاهَةُ', 'Kemakruhan/Larangan (berlaku)', 'ك ر ه', '-', '-', '-', 'Badal / Khabar', '-', '-'),
    ('إِنْ', 'Jika', '-', '-', '-', '-', 'Huruf Syarat', '-', '-'),
    ('لَمْ', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَكُنْ', 'Ada', 'ك و ن', '-', '-', '-', 'Fi\'il Mudhari\' Naqish Majzum', 'Tsulasi Mujarrad', 'Sababun (Sebab)'),
    ('لِلصَّلَاةِ', 'Bagi shalat tersebut', 'ص ل ي', '-', 'Lam jar + Shalah', '-', 'Jar Majrur / Khabar Yakun', '-', '-'),
    ('سَبَبٌ', 'Suatu sebab', 'س ب ب', '-', '-', '-', 'Isim Yakun Muakhkhar', '-', '-'),
    ('مُتَقَدِّمٌ،', 'Yang mendahuluinya,', 'ق د م', '-', '-', '-', 'Na\'at', '-', '-'),
    ('أَوْ', 'Atau jika (ada)', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('تَعَمُّدِ', 'Kesengajaan', 'ع م د', '-', '-', '-', 'Ma\'thuf (Majrur)', '-', '-'),
    ('الدَّفْنِ', 'Dalam menguburkan (jenazah)', 'د ف ن', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فِيهَا.', 'Pada waktu-waktu tersebut.', '-', '-', 'Fii + ha', 'ha merujuk ke waktu-waktu terlarang', 'Jar Majrur', '-', '-')
]
# Breaks: 'الدَّفْنِ' (10)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'وَهَذِهِ الْكَرَاهَةُ إِنْ لَمْ يَكُنْ لِلصَّلَاةِ سَبَبٌ مُتَقَدِّمٌ، أَوْ تَعَمُّدِ الدَّفْنِ فِيهَا.',
    'id': 'Hukum kemakruhan (larangan keras) ini berlaku manakala shalat sunnah yang dikerjakan tersebut tidak memiliki sebab yang mendahuluinya (seperti shalat tahiyatul masjid dll yang ada sebabnya), atau ada unsur kesengajaan dalam menguburkan jenazah tepat pada waktu-waktu terlarang tersebut.',
    'words': make_words(p2_words, [10])
})


# Para 3 (Exceptions to Karahah)
# وَأَمَّا إِذَا لَمْ يَتَعَمَّدْ فِيهَا الدَّفْنَ وَجَاءَ اتِّفَاقاً، أَوْ كَانَ لِلصَّلَاةِ سَبَبٌ
# مُتَقَدِّمٌ كَسُنَّةِ الْوُضُوءِ وَتَحِيَّةِ الْمَسْجِدِ وَقَضَاءِ الْفَائِتَةِ؛ فَإِنَّهُ لَا كَرَاهَةَ فِي
# ذَلِكَ.
p3_words = [
    ('وَأَمَّا', 'Adapun', '-', '-', 'Wawu + Amma', '-', 'Huruf Syarat & Tafshil', '-', '-'),
    ('إِذَا', 'Apabila', '-', '-', '-', '-', 'Zharf Zaman / Syarat', '-', '-'),
    ('لَمْ', 'Tidaklah', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَتَعَمَّدْ', 'Ia menyengaja', 'ع م د', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mazid', 'Al-Mar\'u (Seseorang)'),
    ('فِيهَا', 'Di waktu-waktu tersebut', '-', '-', 'Fii + ha', 'ha merujuk ke awqat', 'Jar Majrur', '-', '-'),
    ('الدَّفْنَ', 'Dalam penguburan jenazah', 'د ف ن', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('وَجَاءَ', 'Namun hal itu terjadi', 'ج ي أ', '-', 'Wawu + Ja\'a', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Dafn (Penguburan)'),
    ('اتِّفَاقاً،', 'Secara kebetulan (tanpa niat),', 'و ف ق', '-', '-', '-', 'Hal', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('كَانَ', 'Adalah', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Sababun'),
    ('لِلصَّلَاةِ', 'Bagi shalat tersebut', 'ص ل ي', '-', 'Lam jar + Shalah', '-', 'Jar Majrur / Khabar Kana', '-', '-'),
    ('سَبَبٌ', 'Suatu sebab', 'س ب ب', '-', '-', '-', 'Isim Kana', '-', '-'),
    ('مُتَقَدِّمٌ', 'Yang mendahuluinya', 'ق د م', '-', '-', '-', 'Na\'at', '-', '-'),
    ('كَسُنَّةِ', 'Seperti shalat sunnah', 'س ن ن', '-', 'Kaf jar + Sunnah', '-', 'Jar Majrur', '-', '-'),
    ('الْوُضُوءِ', 'Wudhu,', 'و ض أ', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَتَحِيَّةِ', 'Dan (shalat) Tahiyatul', 'ح ي ي', '-', 'Wawu + Tahiyyah', '-', 'Ma\'thuf', '-', '-'),
    ('الْمَسْجِدِ', 'Masjid,', 'س ج د', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَقَضَاءِ', 'Dan meng-qadha (mengganti)', 'ق ض ي', '-', 'Wawu + Qadha', '-', 'Ma\'thuf', '-', '-'),
    ('الْفَائِتَةِ؛', 'Shalat wajib yang terlewat;', 'ف و ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَإِنَّهُ', 'Maka sesungguhnya hal itu', '-', '-', 'Fa (Jawab) + Inna + hu', 'hu dhamir sya\'n', 'Amil Nawasikh', '-', '-'),
    ('لَا', 'Tidak ada', '-', '-', '-', '-', 'Laa Nafi lil Jinsi', '-', '-'),
    ('كَرَاهَةَ', 'Kemakruhan (larangan)', 'ك ر ه', '-', '-', '-', 'Isim Laa', '-', '-'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ذَلِكَ.', 'Keadaan tersebut.', 'ذ ل ك', '-', '-', '-', 'Majrur / Khabar Laa', '-', '-')
]
# Breaks: 'سَبَبٌ' (11), 'فِي' (22)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'وَأَمَّا إِذَا لَمْ يَتَعَمَّدْ فِيهَا الدَّفْنَ وَجَاءَ اتِّفَاقاً، أَوْ كَانَ لِلصَّلَاةِ سَبَبٌ مُتَقَدِّمٌ كَسُنَّةِ الْوُضُوءِ وَتَحِيَّةِ الْمَسْجِدِ وَقَضَاءِ الْفَائِتَةِ؛ فَإِنَّهُ لَا كَرَاهَةَ فِي ذَلِكَ.',
    'id': 'Sebaliknya, apabila seseorang tidak ada niat sengaja menguburkan jenazah tepat di jam larangan itu lalu terjadinya secara kebetulan (misal: proses yang molor), atau sebuah shalat yang dikerjakan memiliki "sebab yang mendahului", seperti shalat sunnah wudhu, tahiyatul masjid, atau niat meng-qadha shalat fardhu yang terlewat; maka sesungguhnya tidak ada larangan/kemakruhan sama sekali dalam kondisi-kondisi pengecualian tersebut.',
    'words': make_words(p3_words, [11, 22])
})


# Para 4 (Dalil for exceptions)
# وَيَدُلُّ عَلَى عَدَمِ الْكَرَاهَةِ: مَا رَوَاهُ الْبُخَارِيُّ (٥٧٢)؛ وَمُسْلِمٌ
# (٦٨٤)، عَنْ أَنَسٍ رضي الله عنه عَنِ النَّبِيِّ ﷺ : مَنْ نَسِيَ صَلَاةً فَلْيُصَلِّ
# إِذَا ذَكَرَهَا لَا كَفَّارَةَ لَهَا إِلَّا ذَلِكَ: ﴿وَأَقِمِ الصَّلَاةَ لِذِكْرِي﴾ (سورة طه:
# الآية ١٤).
p4_words = [
    ('وَيَدُلُّ', 'Dan dalil yang menunjukkan', 'د ل ل', '-', 'Wawu + Yadullu', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Ma'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('عَدَمِ', 'Ketiadaan (gugurnya)', 'ع د م', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْكَرَاهَةِ:', 'Kemakruhan tersebut adalah:', 'ك ر ه', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَا', 'Hadits yang', '-', '-', '-', '-', 'Fa\'il (dari yadullu) / Isim Maushul', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan', 'ر و ي', '-', 'Rawa + hu', 'hu merujuk ke hadits (ma)', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Bukhari'),
    ('الْبُخَارِيُّ', 'Oleh Al-Bukhari', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٥٧٢)؛', '(572);', '-', '-', '-', '-', '-', '-', '-'),
    ('وَمُسْلِمٌ', 'Dan Muslim', 'س ل م', '-', 'Wawu + Muslim', '-', 'Ma\'thuf', '-', '-'),
    ('(٦٨٤)،', '(684),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنَسٍ', 'Anas', 'أ ن س', '-', '-', '-', 'Majrur', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Anas', 'Jar Majrur', '-', '-'),
    ('عَنِ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('النَّبِيِّ', 'Nabi', 'ن ب أ', '-', '-', '-', 'Majrur', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('مَنْ', 'Barangsiapa yang', '-', '-', '-', '-', 'Isim Syarat', '-', '-'),
    ('نَسِيَ', 'Lupa (terlewat)', 'ن س ي', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Man'),
    ('صَلَاةً', 'Mengerjakan suatu shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('فَلْيُصَلِّ', 'Maka hendaklah ia mengerjakannya', 'ص ل ي', '-', 'Fa + Lam amr + Yushalli', '-', 'Fi\'il Mudhari\' Majzum (Jawab)', 'Tsulasi Mazid', 'Man'),
    ('إِذَا', 'Kapanpun ketika', '-', '-', '-', '-', 'Zharf Zaman / Syarat', '-', '-'),
    ('ذَكَرَهَا', 'Ia mengingatnya', 'ذ ك ر', '-', 'Dzakara + ha', 'ha merujuk ke shalat', 'Fi\'il Madhi (Mudhaf Ilaih)', 'Tsulasi Mujarrad', 'Man'),
    ('لَا', 'Tidak ada', '-', '-', '-', '-', 'Laa Nafi lil Jinsi', '-', '-'),
    ('كَفَّارَةَ', 'Tebusan', 'ك ف ر', '-', '-', '-', 'Isim Laa', '-', '-'),
    ('لَهَا', 'Bagi shalat tersebut', '-', '-', 'Lam jar + ha', 'ha merujuk ke shalat', 'Jar Majrur / Khabar Laa', '-', '-'),
    ('إِلَّا', 'Melainkan', '-', '-', '-', '-', 'Adat Istitsna\'', '-', '-'),
    ('ذَلِكَ:', 'Hal tersebut (yakni mengerjakannya):', 'ذ ل ك', '-', '-', '-', 'Mustatsna / Badal', '-', '-'),
    ('﴿وَأَقِمِ', '﴿Dan dirikanlah', 'ق و م', '-', 'Wawu + Aqim', '-', 'Fi\'il Amr', 'Tsulasi Mazid', 'Engkau (Anta)'),
    ('الصَّلَاةَ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('لِذِكْرِي﴾', 'Untuk mengingat-Ku﴾', 'ذ ك ر', '-', 'Lam jar + Dzikri + Yaa', 'Yaa merujuk ke Allah', 'Jar Majrur', '-', '-'),
    ('(سورة', '(Surah', '-', '-', '-', '-', 'Khabar (dari mubtada mahdzuf)', '-', '-'),
    ('طه:', 'Thaha:', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الآية', 'Ayat', 'أ ي ي', '-', '-', '-', 'Badal', '-', '-'),
    ('١٤).', '14).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'وَمُسْلِمٌ' (8), 'فَلْيُصَلِّ' (22), 'طه:' (34)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'وَيَدُلُّ عَلَى عَدَمِ الْكَرَاهَةِ: مَا رَوَاهُ الْبُخَارِيُّ (٥٧٢)؛ وَمُسْلِمٌ (٦٨٤)، عَنْ أَنَسٍ رضي الله عنه عَنِ النَّبِيِّ ﷺ : مَنْ نَسِيَ صَلَاةً فَلْيُصَلِّ إِذَا ذَكَرَهَا لَا كَفَّارَةَ لَهَا إِلَّا ذَلِكَ: ﴿وَأَقِمِ الصَّلَاةَ لِذِكْرِي﴾ (سورة طه: الآية ١٤).',
    'id': 'Dan dalil yang menunjukkan atas kebolehan (gugurnya larangan makruh untuk mengerjakan shalat qadha) adalah hadits riwayat Al-Bukhari (572) dan Muslim (684), dari Anas RA dari Nabi SAW: "Barangsiapa yang lupa mengerjakan suatu shalat (hingga terlewat waktunya), maka hendaklah ia segera mengerjakannya kapanpun ia teringat! Tidak ada tebusan (kafarah) bagi shalat tersebut melainkan (hanya dengan) hal itu (mengerjakannya langsung): "Dan dirikanlah shalat untuk mengingat-Ku" (QS. Thaha: 14).',
    'words': make_words(p4_words, [8, 22, 34])
})


# Para 5 (Explanation of the verse and hadith)
# فَقَوْلُهُ: «إِذَا ذَكَرَهَا»: يَدُلُّ عَلَى أَنَّ وَقْتَهَا الْمَشْرُوعَ، وَالْمُطَالَبَ
# بِصَلَاتِهَا فِيهِ، هُوَ وَقْتُ الذِّكْرِ، وَقَدْ يَذْكُرُهَا فِي أَحَدِ الْأَوْقَاتِ الْمَنْهِيِّ
# عَنْهَا، فَدَلَّ عَلَى اسْتِثْنَاءِ ذَلِكَ مِنَ النَّهْيِ.
p5_words = [
    ('فَقَوْلُهُ:', 'Maka sabda beliau:', 'ق و ل', '-', 'Fa + Qaulu + hu', 'hu merujuk ke Nabi', 'Mubtada\'', '-', '-'),
    ('«إِذَا', '«Kapanpun ketika', '-', '-', '-', '-', 'Zharf', '-', '-'),
    ('ذَكَرَهَا»:', 'Ia mengingatnya»:', 'ذ ك ر', '-', 'Dzakara + ha', 'ha merujuk ke shalat', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Man'),
    ('يَدُلُّ', 'Menunjukkan', 'د ل ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar Mubtada\')', 'Tsulasi Mujarrad', 'Qauluhu'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنَّ', 'Bahwa sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('وَقْتَهَا', 'Waktunya', 'و ق ت', '-', 'Waqta + ha', 'ha merujuk ke shalat', 'Isim Anna', '-', '-'),
    ('الْمَشْرُوعَ،', 'Yang disyariatkan,', 'ش ر ع', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَالْمُطَالَبَ', 'Dan yang dituntut', 'ط ل ب', '-', 'Wawu + Muthalab', '-', 'Ma\'thuf', '-', '-'),
    ('بِصَلَاتِهَا', 'Untuk pelaksanaannya', 'ص ل ي', '-', 'Baa jar + Shalati + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('فِيهِ،', 'Pada waktu tersebut,', '-', '-', 'Fii + hi', 'hi merujuk ke waktu', 'Jar Majrur', '-', '-'),
    ('هُوَ', 'Ialah', '-', '-', '-', '-', 'Dhamir Fashl', '-', '-'),
    ('وَقْتُ', 'Waktu saat', 'و ق ت', '-', '-', '-', 'Khabar Anna', '-', '-'),
    ('الذِّكْرِ،', 'Mengingat (teringat shalat),', 'ذ ك ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَقَدْ', 'Dan terkadang (bisa jadi)', '-', '-', 'Wawu + Qad', '-', 'Huruf Taqil', '-', '-'),
    ('يَذْكُرُهَا', 'Seseorang baru teringat shalatnya', 'ذ ك ر', '-', 'Yadzkuru + ha', 'ha merujuk ke shalat', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Man (seseorang)'),
    ('فِي', 'Di', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَحَدِ', 'Salah satu dari', 'أ ح د', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْأَوْقَاتِ', 'Waktu-waktu', 'و ق ت', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْمَنْهِيِّ', 'Yang dilarang', 'ن ه ي', '-', '-', '-', 'Na\'at', '-', '-'),
    ('عَنْهَا،', 'Atasnya,', '-', '-', 'An + ha', 'ha merujuk ke awqat', 'Jar Majrur', '-', '-'),
    ('فَدَلَّ', 'Maka hal ini menunjukkan', 'د ل ل', '-', 'Fa + Dalla', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Konteks'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('اسْتِثْنَاءِ', 'Pengecualian', 'ث ن ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('ذَلِكَ', 'Tindakan (qadha) tersebut', 'ذ ل ك', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('النَّهْيِ.', 'Larangan mutlak ini.', 'ن ه ي', '-', '-', '-', 'Majrur', '-', '-')
]
# Breaks: 'وَالْمُطَالَبَ' (8), 'الْمَنْهِيِّ' (19)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'فَقَوْلُهُ: «إِذَا ذَكَرَهَا»: يَدُلُّ عَلَى أَنَّ وَقْتَهَا الْمَشْرُوعَ، وَالْمُطَالَبَ بِصَلَاتِهَا فِيهِ، هُوَ وَقْتُ الذِّكْرِ، وَقَدْ يَذْكُرُهَا فِي أَحَدِ الْأَوْقَاتِ الْمَنْهِيِّ عَنْهَا، فَدَلَّ عَلَى اسْتِثْنَاءِ ذَلِكَ مِنَ النَّهْيِ.',
    'id': 'Maka sabda beliau yang berbunyi: "Kapanpun ia teringat akan shalatnya", menjadi dalil bahwasanya waktu pelaksanaannya yang disyariatkan, serta yang dituntut untuk langsung ditunaikan saat itu juga, adalah tepat pada saat seseorang teringat shalatnya. Dan bisa saja seseorang baru teringat shalatnya secara tak sengaja pas jatuh pada salah satu waktu-waktu yang dilarang/dimakruhkan tadi, maka hadits ini jelas menunjukkan pengecualian shalat qadha dari larangan tersebut.',
    'words': make_words(p5_words, [8, 19])
})


# Para 6 (Dalil for shalat after Ashar / Sunnah mutaqaddimah)
# وَمَا رَوَاهُ الْبُخَارِيُّ (١١٧٦)؛ وَمُسْلِمٌ (٨٣٤)، عَنْ أُمِّ سَلَمَةَ رضي
# الله عنها: أَنَّهُ ﷺ صَلَّى رَكْعَتَيْنِ بَعْدَ الْعَصْرِ، فَسَأَلَتْهُ عَنْ ذَلِكَ فَقَالَ:
# «يَا بِنْتَ أَبِي أُمَيَّةَ، سَأَلْتِ عَنِ الرَّكْعَتَيْنِ بَعْدَ الْعَصْرِ، وَإِنَّهُ أَتَانِي نَاسٌ مِنْ
# عَبْدِ الْقَيْسِ، فَشَغَلُونِي عَنِ الرَّكْعَتَيْنِ اللَّتَيْنِ بَعْدَ الظُّهْرِ، فَهُمَا هَاتَانِ».
p6_words = [
    ('وَمَا', 'Dan dalil lain (yang diriwayatkan)', '-', '-', 'Wawu + Ma', '-', 'Ma\'thuf', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan', 'ر و ي', '-', 'Rawa + hu', 'hu merujuk ke hadits', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Bukhari'),
    ('الْبُخَارِيُّ', 'Oleh Al-Bukhari', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(١١٧٦)؛', '(1176);', '-', '-', '-', '-', '-', '-', '-'),
    ('وَمُسْلِمٌ', 'Dan Muslim', 'س ل م', '-', 'Wawu + Muslim', '-', 'Ma\'thuf', '-', '-'),
    ('(٨٣٤)،', '(834),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أُمِّ', 'Ummu', 'أ م م', '-', '-', '-', 'Majrur', '-', '-'),
    ('سَلَمَةَ', 'Salamah', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنها:', 'Atasnya:', '-', '-', 'An + ha', 'ha merujuk ke Ummu Salamah', 'Jar Majrur', '-', '-'),
    ('أَنَّهُ', 'Bahwa beliau', '-', '-', 'Anna + hu', 'hu merujuk ke Nabi', 'Amil Nawasikh', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('صَلَّى', 'Telah mengerjakan shalat', 'ص ل ي', '-', '-', '-', 'Fi\'il Madhi (Khabar Anna)', 'Tsulasi Mazid', 'Nabi'),
    ('رَكْعَتَيْنِ', 'Dua rakaat (sunnah)', 'ر ك ع', 'Mutsanna', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('بَعْدَ', 'Sesudah', 'ب ع د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('الْعَصْرِ،', 'Shalat Ashar,', 'ع ص ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَسَأَلَتْهُ', 'Maka Ummu Salamah bertanya kepadanya', 'س أ ل', '-', 'Fa + Sa\'alat + hu', 'hu merujuk ke Nabi', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Hiya (Ummu Salamah)'),
    ('عَنْ', 'Tentang', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ذَلِكَ', 'Tindakan (shalat) tersebut', 'ذ ل ك', '-', '-', '-', 'Majrur', '-', '-'),
    ('فَقَالَ:', 'Maka beliau menjawab:', 'ق و ل', '-', 'Fa + Qala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('«يَا', '«Wahai', '-', '-', '-', '-', 'Huruf Nida\'', '-', '-'),
    ('بِنْتَ', 'Putri', 'ب ن ي', '-', '-', '-', 'Munada', '-', '-'),
    ('أَبِي', 'Abu', 'أ ب و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('أُمَيَّةَ،', 'Umayyah,', 'أ م م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('سَأَلْتِ', 'Engkau bertanya', 'س أ ل', '-', 'Sa\'al + ti', 'ti merujuk ke Anti', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Engkau (Anti)'),
    ('عَنِ', 'Tentang', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الرَّكْعَتَيْنِ', 'Dua rakaat (yang kukerjakan)', 'ر ك ع', 'Mutsanna', '-', '-', 'Majrur', '-', '-'),
    ('بَعْدَ', 'Setelah', 'ب ع د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('الْعَصْرِ،', 'Shalat ashar,', 'ع ص ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَإِنَّهُ', 'Maka sesungguhnya perihal itu adalah', '-', '-', 'Wawu + Inna + hu', 'hu dhamir sya\'n', 'Amil Nawasikh', '-', '-'),
    ('أَتَانِي', 'Telah datang kepadaku', 'أ ت ي', '-', 'Ata + nii', 'nii merujuk ke Aku', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nasun'),
    ('نَاسٌ', 'Orang-orang', 'ن و س', 'Jamak', '-', '-', 'Fa\'il', '-', '-'),
    ('مِنْ', 'Dari kabilah', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('عَبْدِ', 'Abdul', 'ع ب د', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْقَيْسِ،', 'Qais,', 'ق ي س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَشَغَلُونِي', 'Lalu mereka menyibukkanku', 'ش غ ل', '-', 'Fa + Syaghalu + nii', 'nii merujuk ke Nabi', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nasun (Mereka)'),
    ('عَنِ', 'Sehingga terlewatkan dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الرَّكْعَتَيْنِ', 'Dua rakaat (sunnah badiyah)', 'ر ك ع', 'Mutsanna', '-', '-', 'Majrur', '-', '-'),
    ('اللَّتَيْنِ', 'Yakni yang semestinya dikerjakan', '-', 'Mutsanna', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('بَعْدَ', 'Setelah', 'ب ع د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('الظُّهْرِ،', 'Shalat zhuhur,', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَهُمَا', 'Maka dua rakaat (tadi) adalah', '-', 'Mutsanna', 'Fa + Huma', 'huma merujuk ke 2 rakaat', 'Mubtada\'', '-', '-'),
    ('هَاتَانِ».', 'Untuk (mengganti) kedua rakaat tersebut».', '-', 'Mutsanna', '-', '-', 'Khabar', '-', '-')
]
# Breaks: 'رضي' (9), 'فَقَالَ:' (21), 'مِنْ' (34), 'هَاتَانِ».' (44)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'وَمَا رَوَاهُ الْبُخَارِيُّ (١١٧٦)؛ وَمُسْلِمٌ (٨٣٤)، عَنْ أُمِّ سَلَمَةَ رضي الله عنها: أَنَّهُ ﷺ صَلَّى رَكْعَتَيْنِ بَعْدَ الْعَصْرِ، فَسَأَلَتْهُ عَنْ ذَلِكَ فَقَالَ: «يَا بِنْتَ أَبِي أُمَيَّةَ، سَأَلْتِ عَنِ الرَّكْعَتَيْنِ بَعْدَ الْعَصْرِ، وَإِنَّهُ أَتَانِي نَاسٌ مِنْ عَبْدِ الْقَيْسِ، فَشَغَلُونِي عَنِ الرَّكْعَتَيْنِ اللَّتَيْنِ بَعْدَ الظُّهْرِ، فَهُمَا هَاتَانِ».',
    'id': 'Dalil pengecualian (bolehnya melakukan shalat yang ada "sebab yang mendahului") adalah riwayat Bukhari (1176) dan Muslim (834), dari Ummu Salamah RA: bahwasanya Nabi SAW pernah terlihat mengerjakan shalat dua rakaat setelah shalat Ashar (padahal ini waktu larangan mutlak). Maka Ummu Salamah pun bertanya padanya mengenai hal tersebut, lalu beliau menjawab: "Wahai putri Abu Umayyah, engkau bertanya tentang dua rakaat yang kukerjakan setelah ashar, sesungguhnya tadi datang kepadaku sekelompok orang dari kabilah Abdul Qais, lalu mereka mengalihkan kesibukanku sehingga aku melewatkan dua rakaat (sunnah badiyah) setelah shalat zhuhur. Maka yang kukerjakan barusan adalah sebagai ganti untuk kedua rakaat tersebut".',
    'words': make_words(p6_words, [9, 21, 34, 44])
})


# Para 7 (Qiyas for reason)
# وَقِيسَ عَلَى الْقَضَاءِ غَيْرُهُ مِمَّا لَهُ سَبَبٌ مُتَقَدِّمٌ مِنَ الصَّلَوَاتِ.
p7_words = [
    ('وَقِيسَ', 'Dan dikiaskanlah', 'ق ي س', '-', 'Wawu + Qisa', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Ghairuhu'),
    ('عَلَى', 'Diatas (hukum)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْقَضَاءِ', 'Bolehnya meng-qadha (mengganti shalat)', 'ق ض ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('غَيْرُهُ', 'Shalat-shalat selainnya', 'غ ي ر', '-', 'Ghairu + hu', 'hu merujuk ke qadha', 'Na\'ib Fa\'il', '-', '-'),
    ('مِمَّا', 'Yakni terhadap apa-apa yang', '-', '-', 'Min + Ma maushul', '-', 'Jar Majrur', '-', '-'),
    ('لَهُ', 'Memiliki (baginya)', '-', '-', 'Lam jar + hu', 'hu merujuk ke shalat', 'Jar Majrur / Khabar Muqaddam', '-', '-'),
    ('سَبَبٌ', 'Suatu sebab', 'س ب ب', '-', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('مُتَقَدِّمٌ', 'Yang mendahuluinya', 'ق د م', '-', '-', '-', 'Na\'at', '-', '-'),
    ('مِنَ', 'Dari jenis', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الصَّلَوَاتِ.', 'Shalat-shalat (sunnah).', 'ص ل ي', 'Jamak', '-', '-', 'Majrur', '-', '-')
]
# Breaks: 'الصَّلَوَاتِ.' (9)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'وَقِيسَ عَلَى الْقَضَاءِ غَيْرُهُ مِمَّا لَهُ سَبَبٌ مُتَقَدِّمٌ مِنَ الصَّلَوَاتِ.',
    'id': 'Maka di-qiyas-kanlah (disamakan) hukum kebolehan ini pada seluruh jenis shalat-shalat (meski sunnah) selain qadha, yang pelaksanaannya memiliki "sebab yang mendahului" (seperti tahiyatul masjid karena sebab masuk masjid).',
    'words': make_words(p7_words, [9])
})


# Para 8 (Exception for Makkah)
# وَيُسْتَثْنَى مِنْ هَذَا النَّهْيِ مُطْلَقاً حَرَمُ مَكَّةَ، لِقَوْلِهِ ﷺ : «يَا بَنِي
p8_words = [
    ('وَيُسْتَثْنَى', 'Dan dikecualikan', 'ث ن ي', '-', 'Wawu + Yustatsna', '-', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mazid', 'Haram Makkatun'),
    ('مِنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('هَذَا', 'Kaidah ini', '-', '-', '-', '-', 'Isim Isyarah / Majrur', '-', '-'),
    ('النَّهْيِ', 'Larangan ini', 'ن ه ي', '-', '-', '-', 'Badal', '-', '-'),
    ('مُطْلَقاً', 'Secara mutlak', 'ط ل ق', '-', '-', '-', 'Hal', '-', '-'),
    ('حَرَمُ', 'Tanah Haram', 'ح ر م', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('مَكَّةَ،', 'Makkah,', 'م ك ك', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لِقَوْلِهِ', 'Berdasarkan sabda beliau', 'ق و ل', '-', 'Lam jar + Qauli + hi', 'hi merujuk ke Nabi', 'Jar Majrur', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«يَا', '«Wahai', '-', '-', '-', '-', 'Huruf Nida\'', '-', '-'),
    ('بَنِي', 'Bani (Anak-anak keturunan)', 'ب ن ي', 'Jamak', '-', '-', 'Munada Mudhaf', '-', '-')
]
# Breaks: 'بَنِي' (11)
blocks_110.append({
    'type': 'paragraph',
    'ar': 'وَيُسْتَثْنَى مِنْ هَذَا النَّهْيِ مُطْلَقاً حَرَمُ مَكَّةَ، لِقَوْلِهِ ﷺ : «يَا بَنِي',
    'id': 'Dan ada satu pengecualian mutlak (tidak berlaku larangan sama sekali meskipun tanpa sebab yang mendahului) khusus bagi area Tanah Haram Makkah, hal ini berdasarkan sabda beliau SAW: "Wahai keturunan Bani...',
    'words': make_words(p8_words, [11])
})


data.append({
    'pageNumber': 110,
    'blocks': blocks_110
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 110 appended to data.js successfully.')
