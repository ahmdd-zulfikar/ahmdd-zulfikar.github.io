import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_108 = []

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

# Para 1 (Continuation of Waqtu Maghrib)
# Text:
# وَالشَّفَقُ الْأَحْمَرُ: هُوَ بَقَايَا مِنْ آثَارِ ضَوْءِ الشَّمْسِ، يَظْهَرُ فِي الْأُفُقِ
# الشَّرْقِيِّ عِنْدَ وَقْتِ الْغُرُوبِ، ثُمَّ إِنَّ الظَّلَامَ يُطَارِدُهُ نَحْوَ الْغُرُوبِ شَيْئاً
# فَشَيْئاً.
p1_words = [
    ('وَالشَّفَقُ', 'Dan adapun syafaq', 'ش ف ق', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الْأَحْمَرُ:', 'Merah itu:', 'ح م ر', '-', '-', '-', 'Na\'at', '-', '-'),
    ('هُوَ', 'Ia adalah', '-', '-', '-', '-', 'Mubtada\' Tsani', '-', '-'),
    ('بَقَايَا', 'Sisa-sisa', 'ب ق ي', 'Jamak', '-', '-', 'Khabar', '-', '-'),
    ('مِنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('آثَارِ', 'Jejak', 'أ ث ر', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('ضَوْءِ', 'Cahaya', 'ض و أ', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّمْسِ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('يَظْهَرُ', 'Yang nampak', 'ظ ه ر', '-', '-', '-', 'Fi\'il Mudhari\' (Sifat)', 'Tsulasi Mujarrad', 'Syafaq'),
    ('فِي', 'Di', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْأُفُقِ', 'Ufuk (cakrawala)', 'أ ف ق', '-', '-', '-', 'Majrur', '-', '-'),
    ('الشَّرْقِيِّ', 'Timur', 'ش ر ق', '-', '-', '-', 'Na\'at', '-', '-'),
    ('عِنْدَ', 'Pada saat', 'ع ن د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْغُرُوبِ،', 'Terbenamnya (matahari),', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('إِنَّ', 'Sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('الظَّلَامَ', 'Kegelapan malam', 'ظ ل م', '-', '-', '-', 'Isim Inna', '-', '-'),
    ('يُطَارِدُهُ', 'Berangsur mengusirnya/mengejarnya', 'ط ر د', '-', 'Yutharidu + hu', 'hu merujuk ke syafaq', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Zhalam'),
    ('نَحْوَ', 'Ke arah', 'ن ح و', '-', '-', '-', 'Zharf Makan', '-', '-'),
    ('الْغُرُوبِ', 'Barat (tempat tenggelam)', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('شَيْئاً', 'Sedikit', 'ش ي أ', '-', '-', '-', 'Hal / Maf\'ul Muthlaq', '-', '-'),
    ('فَشَيْئاً.', 'Demi sedikit.', 'ش ي أ', '-', 'Fa + Syai\'an', '-', 'Ma\'thuf', '-', '-')
]
# Breaks: 'الْأُفُقِ' (10), 'شَيْئاً' (21), 'فَشَيْئاً.' (22)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'وَالشَّفَقُ الْأَحْمَرُ: هُوَ بَقَايَا مِنْ آثَارِ ضَوْءِ الشَّمْسِ، يَظْهَرُ فِي الْأُفُقِ الشَّرْقِيِّ عِنْدَ وَقْتِ الْغُرُوبِ، ثُمَّ إِنَّ الظَّلَامَ يُطَارِدُهُ نَحْوَ الْغُرُوبِ شَيْئاً فَشَيْئاً.',
    'id': 'Syafaq merah (mega merah) itu sendiri adalah: sisa-sisa jejak cahaya matahari yang nampak di ufuk timur pada saat waktu tenggelamnya matahari, kemudian kegelapan malam berangsur-angsur mengusirnya (menggantikannya) ke arah barat (tempat tenggelam) sedikit demi sedikit.',
    'words': make_words(p1_words, [10, 21, 22])
})


# Para 2 (When Syafaq disappears)
# فَإِذَا أَطْبَقَ الظَّلَامُ وَامْتَدَّ إِلَى الْأُفُقِ الْغَرْبِيِّ، وَزَالَ أَثَرُ الشَّفَقِ
# الْأَحْمَرِ، فَذَلِكَ يَعْنِي انْتِهَاءَ وَقْتِ الْمَغْرِبِ وَدُخُولَ وَقْتِ الْعِشَاءِ.
p2_words = [
    ('فَإِذَا', 'Maka apabila', '-', '-', 'Fa + Idza', '-', 'Zharf Zaman / Syarat', '-', '-'),
    ('أَطْبَقَ', 'Telah menutupi secara merata', 'ط ب ق', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mazid', 'Zhalam'),
    ('الظَّلَامُ', 'Kegelapan malam', 'ظ ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('وَامْتَدَّ', 'Dan membentang luas', 'م د د', '-', 'Wawu + Imtadda', '-', 'Fi\'il Madhi (Ma\'thuf)', 'Tsulasi Mazid', 'Zhalam'),
    ('إِلَى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْأُفُقِ', 'Ke ufuk', 'أ ف ق', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْغَرْبِيِّ،', 'Barat,', 'غ ر ب', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَزَالَ', 'Dan telah hilang', 'ز و ل', '-', 'Wawu + Zala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Atsar'),
    ('أَثَرُ', 'Jejak', 'أ ث ر', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('الشَّفَقِ', 'Mega', 'ش ف ق', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْأَحْمَرِ،', 'Merah,', 'ح م ر', '-', '-', '-', 'Na\'at', '-', '-'),
    ('فَذَلِكَ', 'Maka hal itu', 'ذ ل ك', '-', 'Fa (Jawab) + Dzalika', '-', 'Mubtada\'', '-', '-'),
    ('يَعْنِي', 'Berarti', 'ع ن ي', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Dzalika (hal itu)'),
    ('انْتِهَاءَ', 'Berakhirnya', 'ن ه ي', '-', '-', '-', 'Maf\'ul Bih / Mashdar', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْمَغْرِبِ', 'Maghrib', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَدُخُولَ', 'Dan masuknya', 'د خ ل', '-', 'Wawu + Dukhul', '-', 'Ma\'thuf', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْعِشَاءِ.', 'Isya.', 'ع ش و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-')
]
# Breaks: 'الشَّفَقِ' (9), 'الْعِشَاءِ.' (18)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'فَإِذَا أَطْبَقَ الظَّلَامُ وَامْتَدَّ إِلَى الْأُفُقِ الْغَرْبِيِّ، وَزَالَ أَثَرُ الشَّفَقِ الْأَحْمَرِ، فَذَلِكَ يَعْنِي انْتِهَاءَ وَقْتِ الْمَغْرِبِ وَدُخُولَ وَقْتِ الْعِشَاءِ.',
    'id': 'Maka apabila kegelapan malam telah menutupi secara merata dan membentang hingga ke ufuk barat, serta lenyapnya jejak mega merah tersebut, maka hal itu berarti berakhirlah rentang waktu shalat Maghrib dan masuklah waktu shalat Isya.',
    'words': make_words(p2_words, [9, 18])
})


# Para 3 (Dalil Maghrib)
# دَلَّ عَلَى ذَلِكَ حَدِيثُ الْمَوَاقِيتِ، مَعَ قَوْلِ رَسُولِ اللهِ ﷺ : «وَقْتُ
# الْمَغْرِبِ مَا لَمْ يَغِبِ الشَّفَقُ» (رواه مسلم: ٦١٢).
p3_words = [
    ('دَلَّ', 'Telah menunjukkan', 'د ل ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Hadits'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ذَلِكَ', 'Hal tersebut', 'ذ ل ك', '-', '-', '-', 'Majrur', '-', '-'),
    ('حَدِيثُ', 'Hadits', 'ح د ث', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('الْمَوَاقِيتِ،', 'Al-Mawaqit (Abu Musa tadi),', 'و ق ت', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَعَ', 'Serta', 'م ع ي', '-', '-', '-', 'Zharf', '-', '-'),
    ('قَوْلِ', 'Sabda', 'ق و ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رَسُولِ', 'Rasul', 'ر س ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«وَقْتُ', '«Waktu', 'و ق ت', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الْمَغْرِبِ', 'Shalat Maghrib', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَا', 'Selama', '-', '-', '-', '-', 'Huruf Mashdariyah Zharfiyah', '-', '-'),
    ('لَمْ', 'Belum (tidak)', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَغِبِ', 'Hilang/lenyap', 'غ ي ب', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mujarrad', 'Asy-Syafaq'),
    ('الشَّفَقُ»', 'Mega merah»', 'ش ف ق', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('مسلم:', 'Muslim:', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٦١٢).', '612).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: '«وَقْتُ' (11), '٦١٢).' (19)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'دَلَّ عَلَى ذَلِكَ حَدِيثُ الْمَوَاقِيتِ، مَعَ قَوْلِ رَسُولِ اللهِ ﷺ : «وَقْتُ الْمَغْرِبِ مَا لَمْ يَغِبِ الشَّفَقُ» (رواه مسلم: ٦١٢).',
    'id': 'Hal tersebut ditunjukkan oleh Hadits Al-Mawaqit (waktu-waktu shalat) yang lalu, ditambah juga dengan sabda Rasulullah SAW: "Waktu pelaksanaan shalat Maghrib berlangsung selama cahaya mega merah belum hilang di ufuk" (HR. Muslim: 612).',
    'words': make_words(p3_words, [11, 19])
})


# Heading: «الْعِشَاءُ»:
h1_words = [
    ('«الْعِشَاءُ»:', '«Waktu Isya»:', 'ع ش و', '-', '-', '-', 'Mubtada\'', '-', '-')
]
blocks_108.append({'type': 'heading', 'ar': '«الْعِشَاءُ»:', 'id': 'Waktu Shalat Isya:', 'words': make_words(h1_words, [])})

# Para 4 (Waqtu Isya)
# يَدْخُلُ وَقْتُهُ بِانْتِهَاءِ وَقْتِ الْمَغْرِبِ، وَيَسْتَمِرُّ إِلَى ظُهُورِ الْفَجْرِ
# الصَّادِقِ. وَالِاخْتِيَارُ أَنْ لَا تُؤَخَّرَ عَنِ الثُّلُثِ الْأَوَّلِ مِنَ اللَّيْلِ.
p4_words = [
    ('يَدْخُلُ', 'Masuklah', 'د خ ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Waqtuhu'),
    ('وَقْتُهُ', 'Waktunya (Isya)', 'و ق ت', '-', 'Waqtu + hu', 'hu merujuk ke shalat isya', 'Fa\'il', '-', '-'),
    ('بِانْتِهَاءِ', 'Seketika berakhirnya', 'ن ه ي', '-', 'Baa jar + Intiha\'', '-', 'Jar Majrur', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْمَغْرِبِ،', 'Maghrib,', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَيَسْتَمِرُّ', 'Dan ia berlanjut terus', 'م ر ر', '-', 'Wawu + Yastamirru', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Waqtuhu'),
    ('إِلَى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ظُهُورِ', 'Kemunculan/terbitnya', 'ظ ه ر', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْفَجْرِ', 'Fajar', 'ف ج ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الصَّادِقِ.', 'Sadiq (cahaya fajar sesungguhnya).', 'ص د ق', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَالِاخْتِيَارُ', 'Dan hal yang ikhtiyar (ideal) adalah', 'خ ي ر', '-', 'Wawu + Ikhtiyar', '-', 'Mubtada\'', '-', '-'),
    ('أَنْ', 'Hendaknya ia', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('لَا', 'Janganlah', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('تُؤَخَّرَ', 'Diakhirkan (ditunda)', 'أ خ ر', '-', '-', '-', 'Fi\'il Mudhari\' Majhul (Manshub)', 'Tsulasi Mazid', 'Isya'),
    ('عَنِ', 'Hingga melebihi dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الثُّلُثِ', 'Sepertiga', 'ث ل ث', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْأَوَّلِ', 'Pertama', 'أ و ل', '-', '-', '-', 'Na\'at', '-', '-'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('اللَّيْلِ.', 'Malam hari.', 'ل ي ل', '-', '-', '-', 'Majrur', '-', '-')
]
# Breaks: 'الْفَجْرِ' (8), 'اللَّيْلِ.' (18)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'يَدْخُلُ وَقْتُهُ بِانْتِهَاءِ وَقْتِ الْمَغْرِبِ، وَيَسْتَمِرُّ إِلَى ظُهُورِ الْفَجْرِ الصَّادِقِ. وَالِاخْتِيَارُ أَنْ لَا تُؤَخَّرَ عَنِ الثُّلُثِ الْأَوَّلِ مِنَ اللَّيْلِ.',
    'id': 'Waktunya (Isya) mulai masuk seketika usainya batas waktu shalat Maghrib, dan akan berlanjut terus hingga kemunculan Fajar Shadiq (batas Shubuh). Dan waktu yang menjadi ikhtiyar (pilihan utama/ideal) adalah hendaknya pelaksanaannya tidak ditunda hingga melewati sepertiga malam yang pertama.',
    'words': make_words(p4_words, [8, 18])
})

# Para 5 (Fajar Shadiq Explanation)
# وَالْمَقْصُودُ بِالْفَجْرِ الصَّادِقِ ضِيَاءٌ يَنْتَشِرُ مُمْتَدّاً مَعَ الْأُفُقِ الشَّرْقِيِّ،
# وَهُوَ انْعِكَاسٌ لِضَوْءِ الشَّمْسِ تُقْبِلُ مِنْ بَعِيدٍ. ثُمَّ إِنَّ هَذَا الضِّيَاءَ يَعْلُو نَحْوَ
# السَّمَاءِ شَيْئاً فَشَيْئاً إِلَى أَنْ يَتَكَامَلَ بِطُلُوعِ الشَّمْسِ.
p5_words = [
    ('وَالْمَقْصُودُ', 'Dan yang dimaksud', 'ق ص د', '-', 'Wawu + Maqsud', '-', 'Mubtada\'', '-', '-'),
    ('بِالْفَجْرِ', 'Dengan Fajar', 'ف ج ر', '-', 'Baa jar + Fajr', '-', 'Jar Majrur', '-', '-'),
    ('الصَّادِقِ', 'Shadiq', 'ص د ق', '-', '-', '-', 'Na\'at', '-', '-'),
    ('ضِيَاءٌ', 'Adalah suatu cahaya', 'ض و أ', '-', '-', '-', 'Khabar', '-', '-'),
    ('يَنْتَشِرُ', 'Yang tersebar/memancar', 'ن ش ر', '-', '-', '-', 'Fi\'il Mudhari\' (Sifat)', 'Tsulasi Mazid', 'Dhiya\''),
    ('مُمْتَدّاً', 'Membentang', 'م د د', '-', '-', '-', 'Hal', '-', '-'),
    ('مَعَ', 'Sepanjang', 'م ع ي', '-', '-', '-', 'Zharf', '-', '-'),
    ('الْأُفُقِ', 'Cakrawala', 'أ ف ق', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الشَّرْقِيِّ،', 'Timur,', 'ش ر ق', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَهُوَ', 'Di mana ia (cahaya itu)', '-', '-', 'Wawu hal + Hua', 'Hua merujuk ke Dhiya\'', 'Mubtada\'', '-', '-'),
    ('انْعِكَاسٌ', 'Adalah pantulan', 'ع ك س', '-', '-', '-', 'Khabar', '-', '-'),
    ('لِضَوْءِ', 'Dari pendaran cahaya', 'ض و أ', '-', 'Lam jar + Dhau\'', '-', 'Jar Majrur', '-', '-'),
    ('الشَّمْسِ', 'Matahari', 'ش م س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('تُقْبِلُ', 'Yang datang (menghadap)', 'ق ب ل', '-', '-', '-', 'Fi\'il Mudhari\' (Sifat)', 'Tsulasi Mazid', 'Syams (Matahari)'),
    ('مِنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('بَعِيدٍ.', 'Kejauhan.', 'ب ع د', '-', '-', '-', 'Majrur', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('إِنَّ', 'Sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('هَذَا', 'Ini', '-', '-', '-', '-', 'Isim Isyarah / Isim Inna', '-', '-'),
    ('الضِّيَاءَ', 'Cahaya', 'ض و أ', '-', '-', '-', 'Badal', '-', '-'),
    ('يَعْلُو', 'Akan terus meninggi/naik', 'ع ل و', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Dhiya\''),
    ('نَحْوَ', 'Ke arah', 'ن ح و', '-', '-', '-', 'Zharf Makan', '-', '-'),
    ('السَّمَاءِ', 'Langit (atas)', 'س م و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('شَيْئاً', 'Sedikit', 'ش ي أ', '-', '-', '-', 'Maf\'ul Muthlaq', '-', '-'),
    ('فَشَيْئاً', 'Demi sedikit', 'ش ي أ', '-', 'Fa + Syai\'an', '-', 'Ma\'thuf', '-', '-'),
    ('إِلَى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنْ', 'Tiba saatnya ia', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('يَتَكَامَلَ', 'Menjadi sempurna (puncak terangnya)', 'ك م ل', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mazid', 'Dhiya\''),
    ('بِطُلُوعِ', 'Bersamaan dengan terbitnya', 'ط ل ع', '-', 'Baa jar + Thulu\'', '-', 'Jar Majrur', '-', '-'),
    ('الشَّمْسِ.', 'Matahari.', 'ش م س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-')
]
# Breaks: 'الشَّرْقِيِّ،' (8), 'نَحْوَ' (21), 'الشَّمْسِ.' (29)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'وَالْمَقْصُودُ بِالْفَجْرِ الصَّادِقِ ضِيَاءٌ يَنْتَشِرُ مُمْتَدّاً مَعَ الْأُفُقِ الشَّرْقِيِّ، وَهُوَ انْعِكَاسٌ لِضَوْءِ الشَّمْسِ تُقْبِلُ مِنْ بَعِيدٍ. ثُمَّ إِنَّ هَذَا الضِّيَاءَ يَعْلُو نَحْوَ السَّمَاءِ شَيْئاً فَشَيْئاً إِلَى أَنْ يَتَكَامَلَ بِطُلُوعِ الشَّمْسِ.',
    'id': 'Dan adapun yang dimaksud dengan "Fajar Shadiq" adalah seberkas cahaya putih yang memancar membentang luas di sepanjang garis cakrawala bagian timur; yakni suatu pantulan pendaran dari cahaya matahari yang datang dari kejauhan. Kemudian cahaya tersebut akan terus bergerak meninggi ke atas langit sedikit demi sedikit hingga mencapai puncaknya (kesempurnaannya) bersamaan dengan terbitnya bulatan matahari.',
    'words': make_words(p5_words, [8, 21, 29])
})


# Para 6 (Dalil Isya)
# وَدَلَّ عَلَى وَقْتِ الْعِشَاءِ ابْتِدَاءً وَانْتِهَاءً وَاخْتِيَاراً: مَا جَاءَ فِي حَدِيثِ
# الْمَوَاقِيتِ مَعَ مَا رَوَاهُ مُسْلِمٌ (٦٨١) وَغَيْرُهُ، عَنْ أَبِي قَتَادَةَ رضي الله عنه،
# أَنَّهُ ﷺ قَالَ: «أَمَا إِنَّهُ لَيْسَ فِي النَّوْمِ تَفْرِيطٌ، إِنَّمَا التَّفْرِيطُ عَلَى مَنْ
# لَمْ يُصَلِّ الصَّلَاةَ حَتَّى يَجِيءَ وَقْتُ الصَّلَاةِ الْأُخْرَى».
p6_words = [
    ('وَدَلَّ', 'Dan dalil yang menunjukkan', 'د ل ل', '-', 'Wawu + Dalla', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Ma'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('وَقْتِ', 'Waktu', 'و ق ت', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْعِشَاءِ', 'Shalat Isya', 'ع ش و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ابْتِدَاءً', 'Sebagai awal waktu', 'ب د أ', '-', '-', '-', 'Hal / Tamyiz', '-', '-'),
    ('وَانْتِهَاءً', 'Dan batas akhir', 'ن ه ي', '-', 'Wawu + Intiha\'', '-', 'Ma\'thuf', '-', '-'),
    ('وَاخْتِيَاراً:', 'Serta waktu idealnya adalah:', 'خ ي ر', '-', 'Wawu + Ikhtiyar', '-', 'Ma\'thuf', '-', '-'),
    ('مَا', 'Apa-apa yang', '-', '-', '-', '-', 'Fa\'il (dari dalla)', '-', '-'),
    ('جَاءَ', 'Telah datang/disebutkan', 'ج ي أ', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Ma'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('حَدِيثِ', 'Hadits', 'ح د ث', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْمَوَاقِيتِ', 'Al-Mawaqit (Abu Musa tadi)', 'و ق ت', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَعَ', 'Serta', 'م ع ي', '-', '-', '-', 'Zharf', '-', '-'),
    ('مَا', 'Hadits yang', '-', '-', '-', '-', 'Mudhaf Ilaih / Isim Maushul', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan', 'ر و ي', '-', 'Rawa + hu', 'hu merujuk ke hadits (ma)', 'Fi\'il Madhi (Shilah)', 'Tsulasi Mujarrad', 'Muslim'),
    ('مُسْلِمٌ', 'Muslim', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٦٨١)', '(681)', '-', '-', '-', '-', '-', '-', '-'),
    ('وَغَيْرُهُ،', 'Dan selainnya,', 'غ ي ر', '-', 'Wawu + Ghairu + hu', 'hu merujuk ke Muslim', 'Ma\'thuf', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَبِي', 'Abu', 'أ ب و', '-', '-', '-', 'Majrur', '-', '-'),
    ('قَتَادَةَ', 'Qatadah', 'ق ت د', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه،', 'Atasnya,', '-', '-', 'An + hu', 'hu merujuk ke Abu Qatadah', 'Jar Majrur', '-', '-'),
    ('أَنَّهُ', 'Bahwa beliau', '-', '-', 'Anna + hu', 'hu merujuk ke Nabi', 'Amil Nawasikh', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('قَالَ:', 'Telah bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«أَمَا', '«Ketahuilah/Ingatlah', '-', '-', '-', '-', 'Huruf Tanbih', '-', '-'),
    ('إِنَّهُ', 'Sesungguhnya hal itu', '-', '-', 'Inna + hu', 'hu dhamir sya\'n', 'Amil Nawasikh', '-', '-'),
    ('لَيْسَ', 'Tidaklah', 'ل ي س', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Tafrith'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('النَّوْمِ', 'Kondisi tertidur', 'ن و م', '-', '-', '-', 'Majrur / Khabar Laisa', '-', '-'),
    ('تَفْرِيطٌ،', 'Dianggap kelalaian,', 'ف ر ط', '-', '-', '-', 'Isim Laisa', '-', '-'),
    ('إِنَّمَا', 'Hanyasanya', '-', '-', 'Inna + ma kaffah', '-', 'Adat Hashr (pembatasan)', '-', '-'),
    ('التَّفْرِيطُ', 'Sebuah kelalaian (dosa) itu', 'ف ر ط', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('عَلَى', 'Diatribusikan kepada', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مَنْ', 'Orang yang', '-', '-', '-', '-', 'Majrur / Khabar', '-', '-'),
    ('لَمْ', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يُصَلِّ', 'Mengerjakan shalat', 'ص ل ي', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mazid', 'Man'),
    ('الصَّلَاةَ', 'Suatu shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar / Ghayah', '-', '-'),
    ('يَجِيءَ', 'Tiba/masuknya', 'ج ي أ', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Waqtu'),
    ('وَقْتُ', 'Waktu', 'و ق ت', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْأُخْرَى».', 'Berikutnya».', 'أ خ ر', '-', '-', '-', 'Na\'at', '-', '-')
]
# Breaks: 'حَدِيثِ' (10), 'عَنْهُ،' (23), 'مَنْ' (36), 'الْأُخْرَى».' (44)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'وَدَلَّ عَلَى وَقْتِ الْعِشَاءِ ابْتِدَاءً وَانْتِهَاءً وَاخْتِيَاراً: مَا جَاءَ فِي حَدِيثِ الْمَوَاقِيتِ مَعَ مَا رَوَاهُ مُسْلِمٌ (٦٨١) وَغَيْرُهُ، عَنْ أَبِي قَتَادَةَ رضي الله عنه، أَنَّهُ ﷺ قَالَ: «أَمَا إِنَّهُ لَيْسَ فِي النَّوْمِ تَفْرِيطٌ، إِنَّمَا التَّفْرِيطُ عَلَى مَنْ لَمْ يُصَلِّ الصَّلَاةَ حَتَّى يَجِيءَ وَقْتُ الصَّلَاةِ الْأُخْرَى».',
    'id': 'Adapun yang menjadi dalil bagi batasan awal masuk, batas akhir, serta waktu ikhtiyar dari shalat Isya adalah: penjelasan yang termaktub dalam Hadits Al-Mawaqit tadi, digabungkan dengan hadits riwayat Muslim (681) dan selainnya, dari Abu Qatadah RA, bahwasanya Nabi SAW bersabda: "Ketahuilah, sesungguhnya dalam kondisi tertidur (sampai terlewat waktu shalat) tidaklah dianggap sebagai suatu kelalaian (dosa). Kelalaian (dosa) itu hanyalah ditimpakan kepada orang (yang dalam keadaan sadar) tidak mengerjakan suatu shalat hingga tiba batas masuknya waktu shalat berikutnya (yang lain)".',
    'words': make_words(p6_words, [10, 23, 36, 44])
})


# Para 7 (Deduction from Hadith)
# فَدَلَّ عَلَى أَنَّ وَقْتَ الصَّلَاةِ لَا يَخْرُجُ إِلَّا بِدُخُولِ غَيْرِهَا، وَخَرَجَ
# الصُّبْحُ مِنْ هَذَا الْعُمُومِ.
p7_words = [
    ('فَدَلَّ', 'Maka hadits ini menunjukkan', 'د ل ل', '-', 'Fa + Dalla', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Hadits'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنَّ', 'Bahwasanya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('وَقْتَ', 'Waktu suatu', 'و ق ت', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لَا', 'Tidaklah', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَخْرُجُ', 'Habis (keluar)', 'خ ر ج', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar Anna)', 'Tsulasi Mujarrad', 'Waqtu'),
    ('إِلَّا', 'Melainkan', '-', '-', '-', '-', 'Adat Istitsna\' (Pengecualian)', '-', '-'),
    ('بِدُخُولِ', 'Dengan masuknya waktu shalat', 'د خ ل', '-', 'Baa jar + Dukhul', '-', 'Jar Majrur', '-', '-'),
    ('غَيْرِهَا،', 'Yang lainnya (setelahnya),', 'غ ي ر', '-', 'Ghairi + ha', 'ha merujuk ke shalat', 'Mudhaf Ilaih', '-', '-'),
    ('وَخَرَجَ', 'Dan dikecualikan (dikeluarkan)', 'خ ر ج', '-', 'Wawu + Kharaja', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Asy-Shubhu'),
    ('الصُّبْحُ', 'Waktu Shubuh (fajar)', 'ص ب ح', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('مِنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('هَذَا', 'Kaidah (ini)', '-', '-', '-', '-', 'Isim Isyarah / Majrur', '-', '-'),
    ('الْعُمُومِ.', 'Keumuman tersebut.', 'ع م م', '-', '-', '-', 'Badal', '-', '-')
]
# Breaks: 'وَخَرَجَ' (10)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'فَدَلَّ عَلَى أَنَّ وَقْتَ الصَّلَاةِ لَا يَخْرُجُ إِلَّا بِدُخُولِ غَيْرِهَا، وَخَرَجَ الصُّبْحُ مِنْ هَذَا الْعُمُومِ.',
    'id': 'Maka hadits ini menjadi landasan bahwa waktu suatu shalat tidaklah terhitung habis (keluar) melainkan saat tibanya waktu shalat yang lain (berikutnya). Namun, batas akhir waktu Shubuh dikecualikan dari keumuman kaidah ini (karena berakhir di terbitnya matahari, bukan di awal waktu Zhuhur).',
    'words': make_words(p7_words, [10])
})


# Para 8 (Conclusion on times)
# هَذِهِ هِيَ أَوْقَاتُ الصَّلَاةِ الْخَمْسِ، وَلَكِنْ يَنْبَغِي أَنْ لَا يَتَعَمَّدَ الْمُسْلِمُ
# تَأْخِيرَهَا إِلَى أَوَاخِرِ أَوْقَاتِهَا، مُحْتَجّاً بِاتِّسَاعِهَا؛ إِذْ رُبَّمَا تَسَبَّبَ عَنْ ذَلِكَ
p8_words = [
    ('هَذِهِ', 'Inilah', '-', '-', '-', '-', 'Isim Isyarah / Mubtada\'', '-', '-'),
    ('هِيَ', 'Dia', '-', '-', '-', '-', 'Dhamir Fashl', '-', '-'),
    ('أَوْقَاتُ', 'Waktu-waktu', 'و ق ت', 'Jamak', '-', '-', 'Khabar', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْخَمْسِ،', 'Lima waktu,', 'خ م س', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَلَكِنْ', 'Akan tetapi', 'ل ك ن', '-', 'Wawu + Lakin', '-', 'Huruf Istidrak (Susulan)', '-', '-'),
    ('يَنْبَغِي', 'Sepatutnya (seharusnya)', 'ب غ ي', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'An laa yata\'ammada (Mashdar muawwal)'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('لَا', 'Janganlah', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَتَعَمَّدَ', 'Berani menyengaja', 'ع م د', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mazid', 'Al-Muslimu'),
    ('الْمُسْلِمُ', 'Seorang muslim', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('تَأْخِيرَهَا', 'Untuk mengakhirkannya (menundanya)', 'أ خ ر', '-', 'Ta\'khira + ha', 'ha merujuk ke shalat', 'Maf\'ul Bih / Mashdar', '-', '-'),
    ('إِلَى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَوَاخِرِ', 'Ke ujung akhir', 'أ خ ر', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('أَوْقَاتِهَا،', 'Batas waktu-waktunya,', 'و ق ت', 'Jamak', 'Awqati + ha', 'ha merujuk ke shalat', 'Mudhaf Ilaih', '-', '-'),
    ('مُحْتَجّاً', 'Dengan berhujjah (beralasan)', 'ح ج ج', '-', '-', '-', 'Hal', '-', '-'),
    ('بِاتِّسَاعِهَا؛', 'Kelonggaran/keluasannya;', 'و س ع', '-', 'Baa jar + Ittisa\' + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('إِذْ', 'Karena', '-', '-', '-', '-', 'Huruf Ta\'lil (Zharf)', '-', '-'),
    ('رُبَّمَا', 'Terkadang (bisa jadi)', '-', '-', '-', '-', 'Huruf Jarr Syabih biz Zaid', '-', '-'),
    ('تَسَبَّبَ', 'Hal itu bisa menyebabkan', 'س ب ب', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Ma'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ذَلِكَ', 'Tindakan (penundaan) tersebut', 'ذ ل ك', '-', '-', '-', 'Majrur', '-', '-')
]
# Breaks: 'الْمُسْلِمُ' (10), 'ذَلِكَ' (21)
blocks_108.append({
    'type': 'paragraph',
    'ar': 'هَذِهِ هِيَ أَوْقَاتُ الصَّلَاةِ الْخَمْسِ، وَلَكِنْ يَنْبَغِي أَنْ لَا يَتَعَمَّدَ الْمُسْلِمُ تَأْخِيرَهَا إِلَى أَوَاخِرِ أَوْقَاتِهَا، مُحْتَجّاً بِاتِّسَاعِهَا؛ إِذْ رُبَّمَا تَسَبَّبَ عَنْ ذَلِكَ',
    'id': 'Demikianlah rincian waktu shalat lima waktu. Akan tetapi sepatutnya bagi seorang muslim untuk tidak berani dengan sengaja terus-menerus menunda shalat hingga mepet ke ujung batas akhirnya, sembari berhujjah dengan alasan "waktunya masih longgar/luas". Karena bisa jadi kelalaian tersebut menjadi sebab...',
    'words': make_words(p8_words, [10, 21])
})

data.append({
    'pageNumber': 108,
    'blocks': blocks_108
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 108 appended to data.js successfully.')
