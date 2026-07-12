import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_106 = []

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

# Para 1 (Continuation from page 105)
# كَمَا بَيَّنَ رَسُولُ اللهِ ﷺ ذَلِكَ لِلْمُسْلِمِينَ بِالْقَوْلِ وَالْفِعْلِ.
p1_words = [
    ('كَمَا', 'Sebagaimana pula', '-', '-', 'Kaf jar + Ma', '-', 'Jar Majrur', '-', '-'),
    ('بَيَّنَ', 'Telah menjelaskan', 'ب ي ن', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Rasulullah'),
    ('رَسُولُ', 'Rasul', 'ر س ل', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('ذَلِكَ', 'Hal tersebut', 'ذ ل ك', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('لِلْمُسْلِمِينَ', 'Bagi kaum muslimin', 'س ل م', 'Jamak', 'Lam jar + Muslimin', '-', 'Jar Majrur', '-', '-'),
    ('بِالْقَوْلِ', 'Melalui ucapan', 'ق و ل', '-', 'Baa jar + Qaul', '-', 'Jar Majrur / Hal', '-', '-'),
    ('وَالْفِعْلِ.', 'Dan perbuatan.', 'ف ع ل', '-', 'Wawu + Fi\'il', '-', 'Ma\'thuf', '-', '-')
]
# Breaks: 'وَالْفِعْلِ.' (8)
blocks_106.append({
    'type': 'paragraph',
    'ar': 'كَمَا بَيَّنَ رَسُولُ اللهِ ﷺ ذَلِكَ لِلْمُسْلِمِينَ بِالْقَوْلِ وَالْفِعْلِ.',
    'id': 'Sebagaimana pula Rasulullah SAW telah menjelaskan batasan-batasan waktu tersebut kepada kaum muslimin, baik melalui ucapan (sabda) maupun perbuatan (praktik langsung).',
    'words': make_words(p1_words, [8])
})

# Para 2 (Hadith Abu Musa part 1)
# وَالْحَدِيثُ الَّذِي يَجْمَعُ مَوَاقِيتَ الصَّلَوَاتِ الْخَمْسِ مَا رَوَاهُ
# (مُسْلِمٌ: ٦١٤) وَغَيْرُهُ، عَنْ أَبِي مُوسَى الْأَشْعَرِيِّ رضي الله عنه، عَنِ
# النَّبِيِّ ﷺ : أَنَّهُ أَتَاهُ سَائِلٌ يَسْأَلُهُ عَنْ مَوَاقِيتِ الصَّلَاةِ فَلَمْ يَرُدَّ عَلَيْهِ شَيْئاً.
# وَفِي رِوَايَةٍ أُخْرَى قَالَ: «اشْهَدْ مَعَنَا الصَّلَاةَ». قَالَ: فَأَقَامَ الْفَجْرَ حِينَ
# انْشَقَّ الْفَجْرُ، وَالنَّاسُ لَا يَكَادُ يَعْرِفُ بَعْضُهُمْ بَعْضاً، ثُمَّ أَمَرَهُ فَأَقَامَ بِالظُّهْرِ
# حِينَ زَالَتِ الشَّمْسُ، وَالْقَائِلُ يَقُولُ: قَدِ انْتَصَفَ النَّهَارُ وَهُوَ كَانَ أَعْلَمَ
# مِنْهُمْ، ثُمَّ أَمَرَهُمْ فَأَقَامَ بِالْعَصْرِ وَالشَّمْسُ مُرْتَفِعَةٌ، ثُمَّ أَمَرَهُ فَأَقَامَ بِالْمَغْرِبِ
# حِينَ وَقَعَتِ الشَّمْسُ، ثُمَّ أَمَرَهُ فَأَقَامَ الْعِشَاءَ حِينَ غَابَ الشَّفَقُ.
p2_words = [
    ('وَالْحَدِيثُ', 'Dan hadits', 'ح د ث', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الَّذِي', 'Yang', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('يَجْمَعُ', 'Mengumpulkan/Mencakup', 'ج م ع', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Hadits'),
    ('مَوَاقِيتَ', 'Waktu-waktu', 'و ق ت', 'Jamak', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('الصَّلَوَاتِ', 'Shalat', 'ص ل ي', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْخَمْسِ', 'Lima', 'خ م س', '-', '-', '-', 'Na\'at', '-', '-'),
    ('مَا', 'Adalah apa yang', '-', '-', '-', '-', 'Khabar (Isim Maushul)', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan', 'ر و ي', '-', 'Rawa + hu', 'hu merujuk ke hadits (ma)', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Muslim'),
    ('(مُسْلِمٌ:', '(Muslim:', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٦١٤)', '614)', '-', '-', '-', '-', '-', '-', '-'),
    ('وَغَيْرُهُ،', 'Dan selainnya,', 'غ ي ر', '-', 'Wawu + Ghairu + hu', 'hu merujuk ke Muslim', 'Ma\'thuf', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَبِي', 'Abu', 'أ ب و', '-', '-', '-', 'Majrur', '-', '-'),
    ('مُوسَى', 'Musa', 'م و س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْأَشْعَرِيِّ', 'Al-Asy\'ari', '-', '-', '-', '-', 'Na\'at / Badal', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه،', 'Atasnya,', '-', '-', 'An + hu', 'hu merujuk ke Abu Musa', 'Jar Majrur', '-', '-'),
    ('عَنِ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('النَّبِيِّ', 'Nabi', 'ن ب أ', '-', '-', '-', 'Majrur', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('أَنَّهُ', 'Bahwasanya beliau', '-', '-', 'Anna + hu', 'hu merujuk ke Nabi', 'Amil Nawasikh', '-', '-'),
    ('أَتَاهُ', 'Telah didatangi oleh', 'أ ت ي', '-', 'Ata + hu', 'hu merujuk ke Nabi', 'Fi\'il Madhi (Khabar Anna)', 'Tsulasi Mujarrad', 'Sa\'il'),
    ('سَائِلٌ', 'Seorang penanya', 'س أ ل', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('يَسْأَلُهُ', 'Bertanya kepada beliau', 'س أ ل', '-', 'Yas\'alu + hu', 'hu merujuk ke Nabi', 'Fi\'il Mudhari\' (Sifat)', 'Tsulasi Mujarrad', 'Sa\'il'),
    ('عَنْ', 'Tentang', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مَوَاقِيتِ', 'Waktu-waktu', 'و ق ت', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَلَمْ', 'Maka beliau tidak', '-', '-', 'Fa + Lam', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَرُدَّ', 'Menjawab', 'ر د د', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mujarrad', 'Nabi'),
    ('عَلَيْهِ', 'Kepadanya', '-', '-', 'Ala + hi', 'hi merujuk ke penanya', 'Jar Majrur', '-', '-'),
    ('شَيْئاً.', 'Sedikitpun (dengan lisan).', 'ش ي أ', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('وَفِي', 'Dan dalam', '-', '-', 'Wawu + Fii', '-', 'Huruf Jar', '-', '-'),
    ('رِوَايَةٍ', 'Riwayat', 'ر و ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('أُخْرَى', 'Yang lain', 'أ خ ر', '-', '-', '-', 'Na\'at', '-', '-'),
    ('قَالَ:', 'Beliau bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('«اشْهَدْ', '«Saksikanlah/Hadirilah', 'ش ه د', '-', '-', '-', 'Fi\'il Amr', 'Tsulasi Mujarrad', 'Penanya (Anta)'),
    ('مَعَنَا', 'Bersama kami', 'م ع ي', '-', 'Ma\'a + Naa', 'naa merujuk ke Nabi & Sahabat', 'Zharf Makan', '-', '-'),
    ('الصَّلَاةَ».', 'Pelaksanaan shalat».', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('قَالَ:', 'Abu Musa berkata:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Abu Musa'),
    ('فَأَقَامَ', 'Maka beliau mendirikan', 'ق و م', '-', 'Fa + Aqama', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('الْفَجْرَ', 'Shalat fajar (shubuh)', 'ف ج ر', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حِينَ', 'Ketika', 'ح ي ن', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('انْشَقَّ', 'Merekah/terbit', 'ش ق ق', '-', '-', '-', 'Fi\'il Madhi (Mudhaf Ilaih)', 'Tsulasi Mazid', 'Al-Fajru'),
    ('الْفَجْرُ،', 'Fajar (cahaya shubuh),', 'ف ج ر', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('وَالنَّاسُ', 'Sementara orang-orang', 'ن و س', '-', 'Wawu hal + Nas', '-', 'Mubtada\'', '-', '-'),
    ('لَا', 'Tidak/Hampir tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَكَادُ', 'Hampir', 'ك و د', '-', '-', '-', 'Fi\'il Mudhari\' Naqish (Khabar)', 'Tsulasi Mujarrad', 'An-Nas'),
    ('يَعْرِفُ', 'Mengenali', 'ع ر ف', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar Yakadu)', 'Tsulasi Mujarrad', 'Ba\'dhuhum'),
    ('بَعْضُهُمْ', 'Sebagian mereka', 'ب ع ض', '-', 'Ba\'dhu + hum', 'hum merujuk ke orang-orang', 'Fa\'il', '-', '-'),
    ('بَعْضاً،', 'Sebagian yang lain,', 'ب ع ض', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَمَرَهُ', 'Beliau memerintahkannya (muadzin)', 'أ م ر', '-', 'Amara + hu', 'hu merujuk ke bilal/muadzin', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('فَأَقَامَ', 'Maka ia iqamah', 'ق و م', '-', 'Fa + Aqama', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Muadzin'),
    ('بِالظُّهْرِ', 'Untuk shalat zhuhur', 'ظ ه ر', '-', 'Baa jar + Zhuhur', '-', 'Jar Majrur', '-', '-'),
    ('حِينَ', 'Ketika', 'ح ي ن', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('زَالَتِ', 'Telah tergelincir', 'ز و ل', '-', 'Zalat + Ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('الشَّمْسُ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('وَالْقَائِلُ', 'Padahal ada yang berkata', 'ق و ل', '-', 'Wawu hal + Qail', '-', 'Mubtada\'', '-', '-'),
    ('يَقُولُ:', 'Berucap:', 'ق و ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Al-Qail'),
    ('قَدِ', 'Sungguh', '-', '-', '-', '-', 'Huruf Tahqiq', '-', '-'),
    ('انْتَصَفَ', 'Telah separuh', 'ن ص ف', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'An-Nahar'),
    ('النَّهَارُ', 'Siang hari', 'ن ه ر', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('وَهُوَ', 'Padahal beliau (Nabi)', '-', '-', 'Wawu hal + Hua', 'Hua merujuk ke Nabi', 'Mubtada\'', '-', '-'),
    ('كَانَ', 'Adalah', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish (Khabar)', 'Tsulasi Mujarrad', 'Hua (Nabi)'),
    ('أَعْلَمَ', 'Lebih mengetahui (waktu)', 'ع ل م', '-', '-', '-', 'Khabar Kana', '-', '-'),
    ('مِنْهُمْ،', 'Daripada mereka,', '-', '-', 'Min + hum', 'hum merujuk ke orang-orang', 'Jar Majrur', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَمَرَهُمْ', 'Beliau memerintahkan mereka', 'أ م ر', '-', 'Amara + hum', 'hum merujuk ke muadzin/sahabat', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('فَأَقَامَ', 'Lalu didirikanlah', 'ق و م', '-', 'Fa + Aqama', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Muadzin'),
    ('بِالْعَصْرِ', 'Shalat ashar', 'ع ص ر', '-', 'Baa jar + Ashr', '-', 'Jar Majrur', '-', '-'),
    ('وَالشَّمْسُ', 'Sementara matahari', 'ش م س', '-', 'Wawu hal + Syams', '-', 'Mubtada\'', '-', '-'),
    ('مُرْتَفِعَةٌ،', 'Masih (terang) meninggi,', 'ر ف ع', '-', '-', '-', 'Khabar', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَمَرَهُ', 'Beliau memerintahkannya', 'أ م ر', '-', 'Amara + hu', 'hu merujuk ke muadzin', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('فَأَقَامَ', 'Lalu iqamahlah', 'ق و م', '-', 'Fa + Aqama', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Muadzin'),
    ('بِالْمَغْرِبِ', 'Shalat maghrib', 'غ ر ب', '-', 'Baa jar + Maghrib', '-', 'Jar Majrur', '-', '-'),
    ('حِينَ', 'Ketika', 'ح ي ن', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('وَقَعَتِ', 'Telah terbenam', 'و ق ع', '-', 'Waqaa\'at + Ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('الشَّمْسُ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَمَرَهُ', 'Beliau memerintahkannya', 'أ م ر', '-', 'Amara + hu', 'hu merujuk ke muadzin', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('فَأَقَامَ', 'Lalu iqamahlah', 'ق و م', '-', 'Fa + Aqama', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Muadzin'),
    ('الْعِشَاءَ', 'Shalat isya', 'ع ش و', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حِينَ', 'Ketika', 'ح ي ن', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('غَابَ', 'Telah hilang', 'غ ي ب', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Asy-Syafaq'),
    ('الشَّفَقُ.', 'Syafaq (mega merah).', 'ش ف ق', '-', '-', '-', 'Fa\'il', '-', '-')
]
# Breaks: 'رَوَاهُ' (7), 'عَنِ' (18), 'شَيْئاً.' (28), 'حِينَ' (38), 'بِالظُّهْرِ' (49), 'أَعْلَمَ' (60), 'بِالْمَغْرِبِ' (71), 'الشَّفَقُ.' (81)
blocks_106.append({
    'type': 'paragraph',
    'ar': 'وَالْحَدِيثُ الَّذِي يَجْمَعُ مَوَاقِيتَ الصَّلَوَاتِ الْخَمْسِ مَا رَوَاهُ (مُسْلِمٌ: ٦١٤) وَغَيْرُهُ، عَنْ أَبِي مُوسَى الْأَشْعَرِيِّ رضي الله عنه، عَنِ النَّبِيِّ ﷺ : أَنَّهُ أَتَاهُ سَائِلٌ يَسْأَلُهُ عَنْ مَوَاقِيتِ الصَّلَاةِ فَلَمْ يَرُدَّ عَلَيْهِ شَيْئاً. وَفِي رِوَايَةٍ أُخْرَى قَالَ: «اشْهَدْ مَعَنَا الصَّلَاةَ». قَالَ: فَأَقَامَ الْفَجْرَ حِينَ انْشَقَّ الْفَجْرُ، وَالنَّاسُ لَا يَكَادُ يَعْرِفُ بَعْضُهُمْ بَعْضاً، ثُمَّ أَمَرَهُ فَأَقَامَ بِالظُّهْرِ حِينَ زَالَتِ الشَّمْسُ، وَالْقَائِلُ يَقُولُ: قَدِ انْتَصَفَ النَّهَارُ وَهُوَ كَانَ أَعْلَمَ مِنْهُمْ، ثُمَّ أَمَرَهُمْ فَأَقَامَ بِالْعَصْرِ وَالشَّمْسُ مُرْتَفِعَةٌ، ثُمَّ أَمَرَهُ فَأَقَامَ بِالْمَغْرِبِ حِينَ وَقَعَتِ الشَّمْسُ، ثُمَّ أَمَرَهُ فَأَقَامَ الْعِشَاءَ حِينَ غَابَ الشَّفَقُ.',
    'id': 'Adapun hadits yang menghimpun penjelasan kelima waktu shalat ini adalah hadits yang diriwayatkan oleh Muslim (614) dan selainnya, dari Abu Musa Al-Asy\'ari RA, dari Nabi SAW: Bahwasanya datang seorang penanya menemui beliau, menanyakan tentang waktu-waktu shalat, namun beliau tidak langsung menjawabnya dengan sepatah kata pun. Dalam riwayat lain, beliau bersabda: "Hadirilah shalat bersama kami (agar kau tahu)". Abu Musa berkata: Maka beliau mendirikan shalat fajar (shubuh) di saat fajar (shubuh) baru merekah (sangat gelap), hingga orang-orang nyaris tidak mengenali satu sama lain. Kemudian beliau menyuruh (Bilal) sehingga ia mengumandangkan iqamah untuk shalat zhuhur tepat ketika matahari tergelincir, padahal ada orang yang mengira: "Hari baru separuh siang (belum tergelincir)", padahal beliau (Nabi) lebih tahu dari mereka. Kemudian beliau menyuruh mereka sehingga didirikan shalat ashar saat matahari masih (terang) meninggi, kemudian beliau menyuruhnya (Bilal) sehingga ia mengumandangkan iqamah shalat maghrib tepat ketika matahari terbenam, kemudian beliau menyuruhnya sehingga didirikan shalat isya tepat ketika mega merah (syafaq) lenyap.',
    'words': make_words(p2_words, [7, 18, 28, 38, 49, 60, 71, 81])
})

# Para 3 (Hadith Abu Musa part 2 - second day)
# ثُمَّ أَخَّرَ الْفَجْرَ مِنَ الْغَدِ، حَتَّى انْصَرَفَ مِنْهَا وَالْقَائِلُ يَقُولُ: قَدْ
# طَلَعَتِ الشَّمْسُ أَوْ كَادَتْ، ثُمَّ أَخَّرَ الظُّهْرَ حَتَّى كَانَ قَرِيباً مِنْ وَقْتِ الْعَصْرِ
# بِالْأَمْسِ، ثُمَّ أَخَّرَ الْعَصْرَ حَتَّى انْصَرَفَ مِنْهَا وَالْقَائِلُ يَقُولُ: قَدِ احْمَرَّتِ
# الشَّمْسُ، ثُمَّ أَخَّرَ الْمَغْرِبَ حَتَّى كَانَ عِنْدَ سُقُوطِ الشَّفَقِ، ثُمَّ أَخَّرَ الْعِشَاءَ
# حَتَّى كَانَ ثُلُثُ اللَّيْلِ الْأَوَّلُ. ثُمَّ أَصْبَحَ، فَدَعَا السَّائِلَ فَقَالَ: «الْوَقْتُ بَيْنَ
# هَذَيْنِ».
p3_words = [
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَخَّرَ', 'Beliau mengakhirkan', 'أ خ ر', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('الْفَجْرَ', 'Shalat fajar', 'ف ج ر', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('مِنَ', 'Pada', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْغَدِ،', 'Hari berikutnya (hari kedua),', 'غ د و', '-', '-', '-', 'Majrur', '-', '-'),
    ('حَتَّى', 'Sehingga', '-', '-', '-', '-', 'Huruf Jar / Ghayah', '-', '-'),
    ('انْصَرَفَ', 'Beliau selesai berpaling', 'ص ر ف', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('مِنْهَا', 'Darinya (shalat fajar)', '-', '-', 'Min + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('وَالْقَائِلُ', 'Sementara ada yang berkata', 'ق و ل', '-', 'Wawu hal + Qail', '-', 'Mubtada\'', '-', '-'),
    ('يَقُولُ:', 'Berucap:', 'ق و ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Al-Qail'),
    ('قَدْ', 'Sungguh', '-', '-', '-', '-', 'Huruf Tahqiq', '-', '-'),
    ('طَلَعَتِ', 'Telah terbit', 'ط ل ع', '-', 'Tala\'at + Ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('الشَّمْسُ', 'Matahari', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('كَادَتْ،', 'Hampir (terbit),', 'ك و د', '-', 'Kadat + Ta\' ta\'nits', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Asy-Syamsu'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَخَّرَ', 'Beliau mengakhirkan', 'أ خ ر', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('الظُّهْرَ', 'Shalat zhuhur', 'ظ ه ر', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حَتَّى', 'Sehingga', '-', '-', '-', '-', 'Huruf Jar / Ghayah', '-', '-'),
    ('كَانَ', 'Waktunya tiba', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Waktu (Hua)'),
    ('قَرِيباً', 'Begitu dekat', 'ق ر ب', '-', '-', '-', 'Khabar Kana', '-', '-'),
    ('مِنْ', 'Dengan', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْعَصْرِ', 'Shalat ashar', 'ع ص ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('بِالْأَمْسِ،', 'Hari kemarin (hari pertama),', 'أ م س', '-', 'Baa jar + Ams', '-', 'Jar Majrur', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَخَّرَ', 'Beliau mengakhirkan', 'أ خ ر', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('الْعَصْرَ', 'Shalat ashar', 'ع ص ر', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حَتَّى', 'Sehingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('انْصَرَفَ', 'Beliau selesai berpaling', 'ص ر ف', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('مِنْهَا', 'Darinya', '-', '-', 'Min + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('وَالْقَائِلُ', 'Padahal ada yang berkata', 'ق و ل', '-', 'Wawu hal + Qail', '-', 'Mubtada\'', '-', '-'),
    ('يَقُولُ:', 'Berucap:', 'ق و ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Al-Qail'),
    ('قَدِ', 'Sungguh', '-', '-', '-', '-', 'Huruf Tahqiq', '-', '-'),
    ('احْمَرَّتِ', 'Telah memerah', 'ح م ر', '-', 'Ahmarat + Ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Asy-Syamsu'),
    ('الشَّمْسُ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَخَّرَ', 'Beliau mengakhirkan', 'أ خ ر', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('الْمَغْرِبَ', 'Shalat maghrib', 'غ ر ب', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حَتَّى', 'Sehingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('كَانَ', 'Waktunya tiba', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Waktu (Hua)'),
    ('عِنْدَ', 'Pada saat', 'ع ن د', '-', '-', '-', 'Zharf Makan / Khabar Kana', '-', '-'),
    ('سُقُوطِ', 'Gugurnya/hilangnya', 'س ق ط', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّفَقِ،', 'Mega merah (syafaq),', 'ش ف ق', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَخَّرَ', 'Beliau mengakhirkan', 'أ خ ر', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('الْعِشَاءَ', 'Shalat isya', 'ع ش و', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حَتَّى', 'Sehingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('كَانَ', 'Waktunya tiba', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Waktu (Hua)'),
    ('ثُلُثُ', 'Sepertiga', 'ث ل ث', '-', '-', '-', 'Isim Kana', '-', '-'),
    ('اللَّيْلِ', 'Malam', 'ل ي ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْأَوَّلُ.', 'Yang pertama.', 'أ و ل', '-', '-', '-', 'Na\'at', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَصْبَحَ،', 'Setelah tiba paginya,', 'ص ب ح', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Nabi'),
    ('فَدَعَا', 'Maka beliau memanggil', 'د ع و', '-', 'Fa + Da\'a', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('السَّائِلَ', 'Penanya (kemarin)', 'س أ ل', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('فَقَالَ:', 'Lalu bersabda:', 'ق و ل', '-', 'Fa + Qala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('«الْوَقْتُ', '«Waktu (shalat itu)', 'و ق ت', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('بَيْنَ', 'Adalah di antara', 'ب ي ن', '-', '-', '-', 'Zharf Makan / Khabar', '-', '-'),
    ('هَذَيْنِ».', 'Kedua (batasan) ini».', '-', '-', '-', '-', 'Isim Isyarah / Mudhaf Ilaih', '-', '-')
]
# Breaks: 'قَدْ' (10), 'الْعَصْرِ' (23), 'احْمَرَّتِ' (34), 'الْعِشَاءَ' (46), 'بَيْنَ' (58), 'هَذَيْنِ».' (59)
blocks_106.append({
    'type': 'paragraph',
    'ar': 'ثُمَّ أَخَّرَ الْفَجْرَ مِنَ الْغَدِ، حَتَّى انْصَرَفَ مِنْهَا وَالْقَائِلُ يَقُولُ: قَدْ طَلَعَتِ الشَّمْسُ أَوْ كَادَتْ، ثُمَّ أَخَّرَ الظُّهْرَ حَتَّى كَانَ قَرِيباً مِنْ وَقْتِ الْعَصْرِ بِالْأَمْسِ، ثُمَّ أَخَّرَ الْعَصْرَ حَتَّى انْصَرَفَ مِنْهَا وَالْقَائِلُ يَقُولُ: قَدِ احْمَرَّتِ الشَّمْسُ، ثُمَّ أَخَّرَ الْمَغْرِبَ حَتَّى كَانَ عِنْدَ سُقُوطِ الشَّفَقِ، ثُمَّ أَخَّرَ الْعِشَاءَ حَتَّى كَانَ ثُلُثُ اللَّيْلِ الْأَوَّلُ. ثُمَّ أَصْبَحَ، فَدَعَا السَّائِلَ فَقَالَ: «الْوَقْتُ بَيْنَ هَذَيْنِ».',
    'id': 'Kemudian pada hari berikutnya (hari kedua), beliau mengakhirkan pelaksanaan shalat fajar, sehingga saat beliau selesai mengerjakannya ada yang berkata: "Matahari sungguh telah terbit atau hampir terbit", kemudian beliau mengakhirkan shalat zhuhur hingga mendekati waktu pelaksaan ashar di hari kemarin, kemudian beliau mengakhirkan shalat ashar sehingga tatkala beliau selesai ada yang berkata: "Matahari sungguh telah memerah", kemudian beliau mengakhirkan shalat maghrib sehingga dilaksanakan tatkala mega merah hendak tenggelam, kemudian beliau mengakhirkan shalat isya hingga mencapai sepertiga malam pertama. Kemudian saat tiba waktu paginya, beliau memanggil sang penanya lalu bersabda: "Waktu shalat itu adalah (durasi) di antara kedua rentang (hari pertama dan hari kedua) ini".',
    'words': make_words(p3_words, [10, 23, 34, 46, 58, 59])
})

# Para 4 (Glossary)
# [انْشَقَّ الْفَجْرُ: طَلَعَ ضَوْءُهُ. زَالَتْ: مَالَتْ عَنْ وَسَطِ السَّمَاءِ.
# الشَّفَقُ: الْحُمْرَةُ الَّتِي تَظْهَرُ بَعْدَ غُرُوبِ الشَّمْسِ. سُقُوطُ الشَّفَقِ: غِيَابُهُ].
p4_words = [
    ('[انْشَقَّ', '[Insyaqqal', 'ش ق ق', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Al-Fajr'),
    ('الْفَجْرُ:', 'Fajru:', 'ف ج ر', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('طَلَعَ', 'Artinya terbit/muncul', 'ط ل ع', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Dhau\'uhu'),
    ('ضَوْءُهُ.', 'Cahayanya.', 'ض و أ', '-', 'Dhau\'u + hu', 'hu merujuk ke fajar', 'Fa\'il', '-', '-'),
    ('زَالَتْ:', 'Zalat (tergelincir):', 'ز و ل', '-', 'Zalat + Ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Syams'),
    ('مَالَتْ', 'Artinya condong/bergeser', 'م ي ل', '-', 'Malat + Ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Syams'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('وَسَطِ', 'Tengah', 'و س ط', '-', '-', '-', 'Majrur', '-', '-'),
    ('السَّمَاءِ.', 'Langit.', 'س م و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّفَقُ:', 'Asy-Syafaq:', 'ش ف ق', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الْحُمْرَةُ', 'Artinya warna kemerahan', 'ح م ر', '-', '-', '-', 'Khabar', '-', '-'),
    ('الَّتِي', 'Yang', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('تَظْهَرُ', 'Mulai nampak', 'ظ ه ر', '-', '-', '-', 'Fi\'il Mudhari\' (Shilah)', 'Tsulasi Mujarrad', 'Humrah'),
    ('بَعْدَ', 'Setelah', 'ب ع د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('غُرُوبِ', 'Terbenamnya', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّمْسِ.', 'Matahari.', 'ش م س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('سُقُوطُ', 'Suquth (jatuhnya)', 'س ق ط', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الشَّفَقِ:', 'Syafaq:', 'ش ف ق', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('غِيَابُهُ].', 'Artinya kehilangannya/lenyapnya].', 'غ ي ب', '-', 'Ghiyabu + hu', 'hu merujuk ke syafaq', 'Khabar', '-', '-')
]
# Breaks: 'السَّمَاءِ.' (8)
blocks_106.append({
    'type': 'paragraph',
    'ar': '[انْشَقَّ الْفَجْرُ: طَلَعَ ضَوْءُهُ. زَالَتْ: مَالَتْ عَنْ وَسَطِ السَّمَاءِ. الشَّفَقُ: الْحُمْرَةُ الَّتِي تَظْهَرُ بَعْدَ غُرُوبِ الشَّمْسِ. سُقُوطُ الشَّفَقِ: غِيَابُهُ].',
    'id': '[Penjelasan Kosakata: "Insyaqqal fajru": Muncul cahayanya (merekah). "Zalat": Condong atau bergesernya matahari dari titik tengah langit (puncak). "Asy-Syafaq": Semburat mega merah yang muncul di ufuk setelah terbenamnya matahari. "Suquth asy-syafaq": Menghilang atau lenyapnya mega merah tersebut].',
    'words': make_words(p4_words, [8])
})

# Para 5
# وَهُنَاكَ أَحَادِيثُ بَيَّنَتْ بَعْضَ مَا أُجْمِلَ فِيهِ، أَوْ زَادَتْ عَلَيْهِ، كَمَا
# سَتَرَى فِي تَفْصِيلِ وَقْتِ كُلِّ صَلَاةٍ، وَإِلَيْكَ بَيَانُهَا:
p5_words = [
    ('وَهُنَاكَ', 'Dan di sana ada', '-', '-', 'Wawu + Hunaka', '-', 'Zharf Makan / Khabar Muqaddam', '-', '-'),
    ('أَحَادِيثُ', 'Beberapa hadits lain', 'ح د ث', 'Jamak', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('بَيَّنَتْ', 'Yang merincikan', 'ب ي ن', '-', 'Bayyanat + Ta\' ta\'nits', '-', 'Fi\'il Madhi (Sifat)', 'Tsulasi Mazid', 'Ahadits'),
    ('بَعْضَ', 'Sebagian', 'ب ع ض', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('مَا', 'Hal yang', '-', '-', '-', '-', 'Isim Maushul / Mudhaf Ilaih', '-', '-'),
    ('أُجْمِلَ', 'Dianggap global/umum', 'ج م ل', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mazid', 'Ma'),
    ('فِيهِ،', 'Di dalamnya,', '-', '-', 'Fii + hi', 'hi merujuk ke hadits sebelumnya', 'Jar Majrur', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('زَادَتْ', 'Menambahkan', 'ز ي د', '-', 'Zadat + Ta\' ta\'nits', '-', 'Fi\'il Madhi (Ma\'thuf)', 'Tsulasi Mujarrad', 'Ahadits'),
    ('عَلَيْهِ،', 'Atasnya,', '-', '-', 'Ala + hi', 'hi merujuk ke hadits sebelumnya', 'Jar Majrur', '-', '-'),
    ('كَمَا', 'Sebagaimana yang', '-', '-', 'Kaf jar + Ma', '-', 'Jar Majrur', '-', '-'),
    ('سَتَرَى', 'Akan engkau lihat', 'ر أ ي', '-', 'Sa + Tara', 'Sa bermakna akan datang', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Engkau (Anta)'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('تَفْصِيلِ', 'Rincian', 'ف ص ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('كُلِّ', 'Masing-masing', 'ك ل ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('صَلَاةٍ،', 'Shalat,', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَإِلَيْكَ', 'Dan berikut ini disajikan untukmu', '-', '-', 'Wawu + Ilaika', '-', 'Isim Fi\'il Amr', '-', '-'),
    ('بَيَانُهَا:', 'Penjelasannya:', 'ب ي ن', '-', 'Bayanu + ha', 'ha merujuk ke waktu-waktu shalat', 'Fa\'il (dari isim fi\'il)', '-', '-')
]
# Breaks: 'كَمَا' (10)
blocks_106.append({
    'type': 'paragraph',
    'ar': 'وَهُنَاكَ أَحَادِيثُ بَيَّنَتْ بَعْضَ مَا أُجْمِلَ فِيهِ، أَوْ زَادَتْ عَلَيْهِ، كَمَا سَتَرَى فِي تَفْصِيلِ وَقْتِ كُلِّ صَلَاةٍ، وَإِلَيْكَ بَيَانُهَا:',
    'id': 'Selain itu, terdapat hadits-hadits lain yang memperjelas sebagian makna global yang ada di dalam hadits tadi, atau memberikan tambahan keterangan atasnya, sebagaimana yang akan engkau lihat pada rincian waktu masing-masing shalat berikut. Dan inilah perinciannya:',
    'words': make_words(p5_words, [10])
})

# Heading 1
# «الْفَجْرُ»:
h1_words = [
    ('«الْفَجْرُ»:', '«Shalat Fajar (Shubuh)»:', 'ف ج ر', '-', '-', '-', 'Mubtada\'', '-', '-')
]
blocks_106.append({'type': 'heading', 'ar': '«الْفَجْرُ»:', 'id': 'Waktu Shalat Fajar (Shubuh):', 'words': make_words(h1_words, [])})

# Para 6
# يَدْخُلُ وَقْتُهُ بِظُهُورِ الْفَجْرِ الصَّادِقِ وَيَمْتَدُّ إِلَى طُلُوعِ الشَّمْسِ؛ قَالَ
p6_words = [
    ('يَدْخُلُ', 'Masuk', 'د خ ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Waqtuhu'),
    ('وَقْتُهُ', 'Waktunya', 'و ق ت', '-', 'Waqtu + hu', 'hu merujuk ke shalat fajar', 'Fa\'il', '-', '-'),
    ('بِظُهُورِ', 'Dengan kemunculan', 'ظ ه ر', '-', 'Baa jar + Zhuhur', '-', 'Jar Majrur', '-', '-'),
    ('الْفَجْرِ', 'Fajar', 'ف ج ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الصَّادِقِ', 'Sadiq (Fajar yang benar/terang membentang)', 'ص د ق', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَيَمْتَدُّ', 'Dan membentang (berlanjut)', 'م د د', '-', 'Wawu + Yamtaddu', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Waqtuhu'),
    ('إِلَى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('طُلُوعِ', 'Terbitnya', 'ط ل ع', '-', '-', '-', 'Majrur', '-', '-'),
    ('الشَّمْسِ؛', 'Matahari;', 'ش م س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('قَالَ', 'Telah bersabda', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah')
]
# Breaks: none (last line)
blocks_106.append({
    'type': 'paragraph',
    'ar': 'يَدْخُلُ وَقْتُهُ بِظُهُورِ الْفَجْرِ الصَّادِقِ وَيَمْتَدُّ إِلَى طُلُوعِ الشَّمْسِ؛ قَالَ',
    'id': 'Waktunya mulai masuk dengan kemunculan Fajar Shadiq (cahaya putih membentang di ufuk timur) dan berlanjut terus hingga terbitnya matahari. Rasulullah SAW bersabda',
    'words': make_words(p6_words, [])
})


data.append({
    'pageNumber': 106,
    'blocks': blocks_106
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 106 appended to data.js successfully.')
