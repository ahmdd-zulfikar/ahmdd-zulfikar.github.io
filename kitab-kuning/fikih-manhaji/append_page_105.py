import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_105 = []

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

# Para 1
# Text:
# وَلَكِنَّهُ لَا يَكْفُرُ، بِدَلِيلِ مَا رَوَاهُ أَبُو دَاوُدَ (١٤٢٠) وَغَيْرُهُ، عَنْ عُبَادَةَ بْنِ
# الصَّامِتِ رضي الله عنه قَالَ: سَمِعْتُ رَسُولَ اللهِ ﷺ يَقُولُ: «خَمْسُ
# صَلَوَاتٍ كَتَبَهُنَّ اللَّهُ عَلَى الْعِبَادِ، فَمَنْ جَاءَ بِهِنَّ، لَمْ يُضَيِّعْ مِنْهُنَّ شَيْئاً
# اسْتِخْفَافاً بِحَقِّهِنَّ، كَانَ لَهُ عِنْدَ اللَّهِ عَهْدٌ أَنْ يُدْخِلَهُ الْجَنَّةَ، وَمَنْ لَمْ يَأْتِ
# بِهِنَّ فَلَيْسَ لَهُ عِنْدَ اللَّهِ عَهْدٌ، إِنْ شَاءَ عَذَّبَهُ وَإِنْ شَاءَ أَدْخَلَهُ الْجَنَّةَ».
p1_words = [
    ('وَلَكِنَّهُ', 'Namun sesungguhnya ia', 'ل ك ن', '-', 'Wawu + Lakinna + hu', 'hu merujuk ke orang malas', 'Amil Nawasikh', '-', '-'),
    ('لَا', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَكْفُرُ،', 'Menjadi kafir,', 'ك ف ر', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar Inna)', 'Tsulasi Mujarrad', 'Hua'),
    ('بِدَلِيلِ', 'Berdasarkan dalil', 'د ل ل', '-', 'Baa jar + Dalil', '-', 'Jar Majrur', '-', '-'),
    ('مَا', 'Apa yang', '-', '-', '-', '-', 'Isim Maushul', '-', '-'),
    ('رَوَاهُ', 'Telah diriwayatkan', 'ر و ي', '-', 'Rawa + hu', 'hu merujuk ke hadits', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Abu Dawud'),
    ('أَبُو', 'Abu', 'أ ب و', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('دَاوُدَ', 'Dawud', 'د و د', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('(١٤٢٠)', '(1420)', '-', '-', '-', '-', '-', '-', '-'),
    ('وَغَيْرُهُ،', 'Dan selainnya,', 'غ ي ر', '-', 'Wawu + Ghairu + hu', 'hu merujuk ke Abu Dawud', 'Ma\'thuf', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('عُبَادَةَ', 'Ubadah', 'ع ب د', '-', '-', '-', 'Majrur', '-', '-'),
    ('بْنِ', 'Bin (Putra)', 'ب ن ي', '-', '-', '-', 'Na\'at / Badal', '-', '-'),
    ('الصَّامِتِ', 'Ash-Shamit', 'ص م ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Ubadah', 'Jar Majrur', '-', '-'),
    ('قَالَ:', 'Telah berkata:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Ubadah'),
    ('سَمِعْتُ', 'Aku telah mendengar', 'س م ع', '-', 'Sami\' + tu', 'tu merujuk ke Ubadah', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Aku (Tu)'),
    ('رَسُولَ', 'Rasul', 'ر س ل', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('يَقُولُ:', 'Bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Mudhari\' (Hal)', 'Tsulasi Mujarrad', 'Hua (Rasulullah)'),
    ('«خَمْسُ', '«Lima waktu', 'خ م س', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('صَلَوَاتٍ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('كَتَبَهُنَّ', 'Yang telah diwajibkannya', 'ك ت ب', '-', 'Kataba + hunna', 'hunna merujuk ke 5 waktu shalat', 'Fi\'il Madhi (Na\'at)', 'Tsulasi Mujarrad', 'Allah'),
    ('اللَّهُ', 'Oleh Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْعِبَادِ،', 'Para hamba,', 'ع ب د', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('فَمَنْ', 'Maka barangsiapa yang', '-', '-', 'Fa + Man', '-', 'Isim Syarat', '-', '-'),
    ('جَاءَ', 'Datang/membawa', 'ج ي أ', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Man (Siapa saja)'),
    ('بِهِنَّ،', 'Dengannya,', '-', '-', 'Baa jar + hinna', 'hinna merujuk ke shalat 5 waktu', 'Jar Majrur', '-', '-'),
    ('لَمْ', 'Dia tidak', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يُضَيِّعْ', 'Menyia-nyiakan', 'ض ي ع', '-', '-', '-', 'Fi\'il Mudhari\' Majzum', 'Tsulasi Mazid', 'Hua'),
    ('مِنْهُنَّ', 'Darinya', '-', '-', 'Min + hunna', 'hunna merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('شَيْئاً', 'Sesuatu (apapun)', 'ش ي أ', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('اسْتِخْفَافاً', 'Karena meremehkan', 'خ ف ف', '-', '-', '-', 'Maf\'ul liajlih / Hal', '-', '-'),
    ('بِحَقِّهِنَّ،', 'Akan hak/keagungannya,', 'ح ق ق', '-', 'Baa jar + Haqq + hinna', 'hinna merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('كَانَ', 'Maka adalah', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish (Jawab Syarat)', 'Tsulasi Mujarrad', 'Ahdun (Perjanjian)'),
    ('لَهُ', 'Baginya', '-', '-', 'Lam jar + hu', 'hu merujuk ke hamba tersebut', 'Jar Majrur / Khabar Kana muqaddam', '-', '-'),
    ('عِنْدَ', 'Di sisi', 'ع ن د', '-', '-', '-', 'Zharf Makan', '-', '-'),
    ('اللَّهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('عَهْدٌ', 'Sebuah perjanjian (jaminan)', 'ع ه د', '-', '-', '-', 'Isim Kana Muakhkhar', '-', '-'),
    ('أَنْ', 'Bahwa Dia akan', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('يُدْخِلَهُ', 'Memasukkannya', 'د خ ل', '-', 'Yudkhila + hu', 'hu merujuk ke hamba', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Allah'),
    ('الْجَنَّةَ،', 'Ke surga,', 'ج ن ن', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('وَمَنْ', 'Dan barangsiapa yang', '-', '-', 'Wawu + Man', '-', 'Isim Syarat', '-', '-'),
    ('لَمْ', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَأْتِ', 'Membawa/datang', 'أ ت ي', '-', '-', '-', 'Fi\'il Mudhari\' Majzum (Syarat)', 'Tsulasi Mujarrad', 'Hua'),
    ('بِهِنَّ', 'Dengannya', '-', '-', 'Baa jar + hinna', 'hinna merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('فَلَيْسَ', 'Maka tidak ada', 'ل ي س', '-', 'Fa (jawab) + Laisa', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Ahdun'),
    ('لَهُ', 'Baginya', '-', '-', 'Lam jar + hu', 'hu merujuk ke hamba yang lalai', 'Jar Majrur / Khabar Laisa', '-', '-'),
    ('عِنْدَ', 'Di sisi', 'ع ن د', '-', '-', '-', 'Zharf Makan', '-', '-'),
    ('اللَّهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('عَهْدٌ،', 'Sebuah perjanjian (jaminan),', 'ع ه د', '-', '-', '-', 'Isim Laisa', '-', '-'),
    ('إِنْ', 'Jika', '-', '-', '-', '-', 'Huruf Syarat', '-', '-'),
    ('شَاءَ', 'Dia (Allah) berkehendak', 'ش ي أ', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Allah'),
    ('عَذَّبَهُ', 'Dia akan mengazabnya', 'ع ذ ب', '-', 'Azzaba + hu', 'hu merujuk ke hamba tersebut', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mazid', 'Allah'),
    ('وَإِنْ', 'Dan jika', '-', '-', 'Wawu + In', '-', 'Huruf Syarat', '-', '-'),
    ('شَاءَ', 'Dia berkehendak', 'ش ي أ', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Allah'),
    ('أَدْخَلَهُ', 'Dia akan memasukkannya', 'د خ ل', '-', 'Adkhala + hu', 'hu merujuk ke hamba', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mazid', 'Allah'),
    ('الْجَنَّةَ».', 'Ke surga».', 'ج ن ن', '-', '-', '-', 'Maf\'ul Bih', '-', '-')
]
# Breaks: 'بْنِ' (12), '«خَمْسُ' (23), 'شَيْئاً' (35), 'يَأْتِ' (48), 'الْجَنَّةَ».' (61)
blocks_105.append({
    'type': 'paragraph',
    'ar': 'وَلَكِنَّهُ لَا يَكْفُرُ، بِدَلِيلِ مَا رَوَاهُ أَبُو دَاوُدَ (١٤٢٠) وَغَيْرُهُ، عَنْ عُبَادَةَ بْنِ الصَّامِتِ رضي الله عنه قَالَ: سَمِعْتُ رَسُولَ اللهِ ﷺ يَقُولُ: «خَمْسُ صَلَوَاتٍ كَتَبَهُنَّ اللَّهُ عَلَى الْعِبَادِ، فَمَنْ جَاءَ بِهِنَّ، لَمْ يُضَيِّعْ مِنْهُنَّ شَيْئاً اسْتِخْفَافاً بِحَقِّهِنَّ، كَانَ لَهُ عِنْدَ اللَّهِ عَهْدٌ أَنْ يُدْخِلَهُ الْجَنَّةَ، وَمَنْ لَمْ يَأْتِ بِهِنَّ فَلَيْسَ لَهُ عِنْدَ اللَّهِ عَهْدٌ، إِنْ شَاءَ عَذَّبَهُ وَإِنْ شَاءَ أَدْخَلَهُ الْجَنَّةَ».',
    'id': 'Namun sesungguhnya ia (yang sekadar malas) tidaklah kafir, berdasarkan dalil hadits riwayat Abu Dawud (1420) dan selainnya, dari Ubadah bin Ash-Shamit RA, ia berkata: Aku telah mendengar Rasulullah SAW bersabda: "Lima waktu shalat yang telah Allah wajibkan atas hamba-hamba-Nya, maka barangsiapa yang menunaikannya, ia tidak menyia-nyiakan hak shalat itu sedikitpun karena meremehkannya, maka ia memiliki jaminan di sisi Allah bahwa Dia akan memasukkannya ke dalam surga. Dan barangsiapa yang tidak menunaikannya, maka tidak ada jaminan baginya di sisi Allah; Jika Allah berkehendak, Dia akan menyiksanya, dan jika Dia berkehendak, Dia akan memasukkannya ke dalam surga".',
    'words': make_words(p1_words, [12, 23, 35, 48, 61])
})

# Para 2
# Text:
# فَقَدْ دَلَّ عَلَى أَنَّ تَارِكَ الصَّلَاةِ لَا يَكْفُرُ، لِأَنَّهُ لَوْ كَفَرَ لَمْ يَدْخُلْ فِي
# قَوْلِهِ: «وَإِنْ شَاءَ أَدْخَلَهُ الْجَنَّةَ»؛ إِذِ الْكَافِرُ لَا يَدْخُلُ الْجَنَّةَ قَطْعاً، فَحُمِلَ
# عَلَى مَنْ تَرَكَهَا كَسَلًا، جَمْعاً بَيْنَ الْأَدِلَّةِ.
p2_words = [
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('دَلَّ', 'Ia (hadits) telah menunjukkan', 'د ل ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Hadits'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَنَّ', 'Bahwa sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('تَارِكَ', 'Orang yang meninggalkan', 'ت ر ك', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لَا', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَكْفُرُ،', 'Menjadi kafir,', 'ك ف ر', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar Anna)', 'Tsulasi Mujarrad', 'Tarik'),
    ('لِأَنَّهُ', 'Karena sesungguhnya dia', '-', '-', 'Lam ta\'lil + Anna + hu', 'hu merujuk ke tarik', 'Amil Nawasikh', '-', '-'),
    ('لَوْ', 'Seandainya', '-', '-', '-', '-', 'Huruf Syarat/Tamanni', '-', '-'),
    ('كَفَرَ', 'Ia telah kafir', 'ك ف ر', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Tarik'),
    ('لَمْ', 'Niscaya ia tidak akan', '-', '-', '-', '-', 'Huruf Nafi & Jazm', '-', '-'),
    ('يَدْخُلْ', 'Masuk (tercakup)', 'د خ ل', '-', '-', '-', 'Fi\'il Mudhari\' Majzum (Jawab)', 'Tsulasi Mujarrad', 'Tarik'),
    ('فِي', 'Ke dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('قَوْلِهِ:', 'Sabda beliau:', 'ق و ل', '-', 'Qauli + hi', 'hi merujuk ke Rasulullah', 'Majrur', '-', '-'),
    ('«وَإِنْ', '«Dan jika', '-', '-', 'Wawu + In', '-', 'Huruf Syarat', '-', '-'),
    ('شَاءَ', 'Dia berkehendak', 'ش ي أ', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Allah'),
    ('أَدْخَلَهُ', 'Dia memasukkannya', 'د خ ل', '-', 'Adkhala + hu', 'hu merujuk ke hamba', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mazid', 'Allah'),
    ('الْجَنَّةَ»؛', 'Ke surga»;', 'ج ن ن', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('إِذِ', 'Karena', '-', '-', '-', '-', 'Huruf Ta\'lil', '-', '-'),
    ('الْكَافِرُ', 'Orang kafir', 'ك ف ر', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('لَا', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَدْخُلُ', 'Akan masuk', 'د خ ل', '-', '-', '-', 'Fi\'il Mudhari\' (Khabar)', 'Tsulasi Mujarrad', 'Kafir'),
    ('الْجَنَّةَ', 'Ke surga', 'ج ن ن', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('قَطْعاً،', 'Secara pasti (mutlak),', 'ق ط ع', '-', '-', '-', 'Maf\'ul Muthlaq / Hal', '-', '-'),
    ('فَحُمِلَ', 'Maka diarahkanlah makna ini', 'ح م ل', '-', 'Fa + Humila', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Hadits (Konteks)'),
    ('عَلَى', 'Kepada', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مَنْ', 'Orang yang', '-', '-', '-', '-', 'Majrur', '-', '-'),
    ('تَرَكَهَا', 'Meninggalkannya', 'ت ر ك', '-', 'Taraka + ha', 'ha merujuk ke shalat', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Man'),
    ('كَسَلًا،', 'Karena malas,', 'ك س ل', '-', '-', '-', 'Maf\'ul liajlih / Hal', '-', '-'),
    ('جَمْعاً', 'Sebagai bentuk penggabungan (kompromi)', 'ج م ع', '-', '-', '-', 'Maf\'ul liajlih', '-', '-'),
    ('بَيْنَ', 'Di antara', 'ب ي ن', '-', '-', '-', 'Zharf Makan/Zaman', '-', '-'),
    ('الْأَدِلَّةِ.', 'Dalil-dalil.', 'د ل ل', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
]
# Breaks: 'فِي' (13), 'فَحُمِلَ' (25), 'الْأَدِلَّةِ.' (32)
blocks_105.append({
    'type': 'paragraph',
    'ar': 'فَقَدْ دَلَّ عَلَى أَنَّ تَارِكَ الصَّلَاةِ لَا يَكْفُرُ، لِأَنَّهُ لَوْ كَفَرَ لَمْ يَدْخُلْ فِي قَوْلِهِ: «وَإِنْ شَاءَ أَدْخَلَهُ الْجَنَّةَ»؛ إِذِ الْكَافِرُ لَا يَدْخُلُ الْجَنَّةَ قَطْعاً، فَحُمِلَ عَلَى مَنْ تَرَكَهَا كَسَلًا، جَمْعاً بَيْنَ الْأَدِلَّةِ.',
    'id': 'Maka sungguh hadits ini menunjukkan bahwa orang yang meninggalkan shalat tidaklah dikafirkan, karena seandainya ia murtad, niscaya ia tidak akan tercakup dalam sabda beliau: "Dan jika Dia berkehendak, Dia akan memasukkannya ke surga"; padahal orang kafir secara mutlak mustahil masuk surga. Oleh karena itu, makna (hukuman mati) diarahkan (dikhususkan) pada orang yang meninggalkannya karena malas, sebagai bentuk kompromi (jam\'u) dalam memahami dalil-dalil yang ada.',
    'words': make_words(p2_words, [13, 25, 32])
})

# Para 3
# Text:
# رَوَى مُسْلِمٌ (٨٢) وَغَيْرُهُ، عَنْ جَابِرٍ رضي الله عنه قَالَ: سَمِعْتُ
# النَّبِيَّ ﷺ يَقُولُ: «إِنَّ بَيْنَ الرَّجُلِ وَبَيْنَ الشِّرْكِ وَالْكُفْرِ تَرْكَ الصَّلَاةِ».
# وَهُوَ مَحْمُولٌ عَلَى التَّرْكِ جُحُوداً وَإِنْكَاراً لِفَرْضِيَّتِهَا، أَوْ اسْتِهْزَاءً بِهَا
# وَاسْتِخْفَافاً بِشَأْنِهَا.
p3_words = [
    ('رَوَى', 'Telah meriwayatkan', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Muslim'),
    ('مُسْلِمٌ', 'Muslim', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٨٢)', '(82)', '-', '-', '-', '-', '-', '-', '-'),
    ('وَغَيْرُهُ،', 'Dan selainnya,', 'غ ي ر', '-', 'Wawu + Ghairu + hu', 'hu merujuk ke Muslim', 'Ma\'thuf', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('جَابِرٍ', 'Jabir', 'ج ب ر', '-', '-', '-', 'Majrur', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Jabir', 'Jar Majrur', '-', '-'),
    ('قَالَ:', 'Telah berkata:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Jabir'),
    ('سَمِعْتُ', 'Aku telah mendengar', 'س م ع', '-', 'Sami\' + tu', 'tu merujuk ke Jabir', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Aku (Tu)'),
    ('النَّبِيَّ', 'Nabi', 'ن ب أ', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('يَقُولُ:', 'Bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Mudhari\' (Hal)', 'Tsulasi Mujarrad', 'Nabi'),
    ('«إِنَّ', '«Sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('بَيْنَ', 'Antara (batas pemisah)', 'ب ي ن', '-', '-', '-', 'Zharf Makan / Khabar Inna', '-', '-'),
    ('الرَّجُلِ', 'Seseorang', 'ر ج ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَبَيْنَ', 'Dan antara', 'ب ي ن', '-', 'Wawu + Baina', '-', 'Ma\'thuf', '-', '-'),
    ('الشِّرْكِ', 'Kesyirikan', 'ش ر ك', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَالْكُفْرِ', 'Dan kekufuran', 'ك ف ر', '-', 'Wawu + Kufr', '-', 'Ma\'thuf', '-', '-'),
    ('تَرْكَ', 'Adalah meninggalkan', 'ت ر ك', '-', '-', '-', 'Isim Inna Muakhkhar', '-', '-'),
    ('الصَّلَاةِ».', 'Shalat».', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَهُوَ', 'Dan hal ini (hadits ini)', '-', '-', 'Wawu hal + Hua', 'Hua merujuk ke teks hadits di atas', 'Mubtada\'', '-', '-'),
    ('مَحْمُولٌ', 'Diarahkan (maknanya)', 'ح م ل', '-', '-', '-', 'Khabar', '-', '-'),
    ('عَلَى', 'Kepada', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('التَّرْكِ', 'Bentuk tindakan meninggalkan (yang disertai dengan)', 'ت ر ك', '-', '-', '-', 'Majrur', '-', '-'),
    ('جُحُوداً', 'Mengingkari', 'ج ح د', '-', '-', '-', 'Hal', '-', '-'),
    ('وَإِنْكَاراً', 'Dan menentang', 'ن ك ر', '-', 'Wawu + Inkar', '-', 'Ma\'thuf', '-', '-'),
    ('لِفَرْضِيَّتِهَا،', 'Akan kewajibannya,', 'ف ر ض', '-', 'Lam jar + Fardhiyyah + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('أَوْ', 'Atau', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('اسْتِهْزَاءً', 'Memperolok-olok', 'ه ز أ', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('بِهَا', 'Dengannya', '-', '-', 'Baa jar + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('وَاسْتِخْفَافاً', 'Dan meremehkan', 'خ ف ف', '-', 'Wawu + Istikhfaf', '-', 'Ma\'thuf', '-', '-'),
    ('بِشَأْنِهَا.', 'Urusannya.', 'ش أ ن', '-', 'Baa jar + Sya\'ni + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-')
]
# Breaks: 'سَمِعْتُ' (10), 'الصَّلَاةِ».' (21), 'بِهَا' (31), 'بِشَأْنِهَا.' (33)
blocks_105.append({
    'type': 'paragraph',
    'ar': 'رَوَى مُسْلِمٌ (٨٢) وَغَيْرُهُ، عَنْ جَابِرٍ رضي الله عنه قَالَ: سَمِعْتُ النَّبِيَّ ﷺ يَقُولُ: «إِنَّ بَيْنَ الرَّجُلِ وَبَيْنَ الشِّرْكِ وَالْكُفْرِ تَرْكَ الصَّلَاةِ». وَهُوَ مَحْمُولٌ عَلَى التَّرْكِ جُحُوداً وَإِنْكَاراً لِفَرْضِيَّتِهَا، أَوْ اسْتِهْزَاءً بِهَا وَاسْتِخْفَافاً بِشَأْنِهَا.',
    'id': 'Telah meriwayatkan Muslim (82) dan selainnya, dari Jabir RA, ia berkata: Aku telah mendengar Nabi SAW bersabda: "Sesungguhnya (batas pemisah) antara seseorang dengan kesyirikan dan kekufuran adalah perbuatan meninggalkan shalat". Hadits ini pemaknaannya diarahkan (terkhusus) pada tindakan meninggalkan shalat yang diiringi dengan penolakan dan pengingkaran atas kewajibannya, atau sebagai bentuk olok-olok dan pelecehan terhadap urusan shalat tersebut.',
    'words': make_words(p3_words, [10, 21, 31, 33])
})

# Heading 1
# أَوْقَاتُ الصَّلَوَاتِ الْمَفْرُوضَةِ :
h1_words = [
    ('أَوْقَاتُ', 'Waktu-waktu', 'و ق ت', 'Jamak', '-', '-', 'Mubtada\'', '-', '-'),
    ('الصَّلَوَاتِ', 'Shalat', 'ص ل ي', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْمَفْرُوضَةِ', 'Yang Diwajibkan (Fardhu)', 'ف ر ض', '-', '-', '-', 'Na\'at', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_105.append({'type': 'heading', 'ar': 'أَوْقَاتُ الصَّلَوَاتِ الْمَفْرُوضَةِ :', 'id': 'Waktu-Waktu Shalat Yang Diwajibkan:', 'words': make_words(h1_words, [])})

# Para 4
# Text:
# الصَّلَوَاتُ الْخَمْسُ، كُلٌّ مِنْهَا لَهَا وَقْتٌ مُعَيَّنٌ، ذُو بِدَايَةٍ لَا تَصِحُّ إِذَا
# قُدِّمَتْ عَلَيْهَا، وَذُو نِهَايَةٍ لَا يَجُوزُ تَأْخِيرُهَا عَنْهَا.
p4_words = [
    ('الصَّلَوَاتُ', 'Shalat-shalat', 'ص ل ي', 'Jamak', '-', '-', 'Mubtada\'', '-', '-'),
    ('الْخَمْسُ،', 'Lima waktu,', 'خ م س', '-', '-', '-', 'Na\'at', '-', '-'),
    ('كُلٌّ', 'Setiap', 'ك ل ل', '-', '-', '-', 'Mubtada\' Tsani', '-', '-'),
    ('مِنْهَا', 'Darinya', '-', '-', 'Min + ha', 'ha merujuk ke shalat 5 waktu', 'Jar Majrur', '-', '-'),
    ('لَهَا', 'Memiliki (baginya)', '-', '-', 'Lam jar + ha', 'ha merujuk ke shalat 5 waktu', 'Jar Majrur / Khabar Muqaddam', '-', '-'),
    ('وَقْتٌ', 'Waktu', 'و ق ت', '-', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('مُعَيَّنٌ،', 'Yang ditentukan,', 'ع ي ن', '-', '-', '-', 'Na\'at', '-', '-'),
    ('ذُو', 'Yang memiliki', 'ذ و', '-', '-', '-', 'Na\'at', '-', '-'),
    ('بِدَايَةٍ', 'Awal (permulaan)', 'ب د أ', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لَا', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('تَصِحُّ', 'Sah', 'ص ح ح', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Shalat'),
    ('إِذَا', 'Apabila', '-', '-', '-', '-', 'Zharf Zaman / Syarat', '-', '-'),
    ('قُدِّمَتْ', 'Didahulukan', 'ق د م', '-', 'Quddimat + Ta\' ta\'nits', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mazid', 'Shalat'),
    ('عَلَيْهَا،', 'Atasnya,', '-', '-', 'Ala + ha', 'ha merujuk ke permulaan waktu', 'Jar Majrur', '-', '-'),
    ('وَذُو', 'Dan memiliki', 'ذ و', '-', 'Wawu + Dzu', '-', 'Ma\'thuf', '-', '-'),
    ('نِهَايَةٍ', 'Batas akhir', 'ن ه ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لَا', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يَجُوزُ', 'Diperbolehkan', 'ج و ز', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Ta\'khiruha'),
    ('تَأْخِيرُهَا', 'Mengakhirkannya', 'أ خ ر', '-', 'Ta\'khiru + ha', 'ha merujuk ke shalat', 'Fa\'il', '-', '-'),
    ('عَنْهَا.', 'Melewatiny. (melewati batas akhir)', '-', '-', 'An + ha', 'ha merujuk ke batas akhir (nihayah)', 'Jar Majrur', '-', '-')
]
# Breaks: 'إِذَا' (11), 'عَنْهَا.' (19)
blocks_105.append({
    'type': 'paragraph',
    'ar': 'الصَّلَوَاتُ الْخَمْسُ، كُلٌّ مِنْهَا لَهَا وَقْتٌ مُعَيَّنٌ، ذُو بِدَايَةٍ لَا تَصِحُّ إِذَا قُدِّمَتْ عَلَيْهَا، وَذُو نِهَايَةٍ لَا يَجُوزُ تَأْخِيرُهَا عَنْهَا.',
    'id': 'Kelima shalat wajib (fardhu) tersebut, masing-masing darinya telah memiliki waktu pelaksanaannya yang spesifik. Setiap waktu memiliki batas permulaan, yang mana shalat menjadi tidak sah apabila didahulukan sebelum waktu permulaan tersebut. Serta memiliki batas akhir, yang mana tidak diperbolehkan mengakhirkan shalat melampaui batas akhir tersebut.',
    'words': make_words(p4_words, [11, 19])
})


# Para 5
# Text:
# قَالَ اللهُ تَعَالَى: ﴿إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَاباً مَّوْقُوتاً﴾
# (سورة النساء: الآية ١٠٣). أَيْ كَانَتْ فَرِيضَةً مُحَدَّدَةً بِأَوْقَاتٍ مَخْصُوصَةٍ.
# وَقَدْ ثَبَتَ فِي الْأَحَادِيثِ الصَّحِيحَةِ أَنَّ جِبْرِيلَ عليه السلام جَاءَ إِلَى
# النَّبِيِّ ﷺ بَعْدَ أَنْ فُرِضَتِ الصَّلَوَاتُ الْخَمْسُ، يُعَرِّفُهُ أَوْقَاتَهَا، وَيَضْبِطُ لَهُ
# وَقْتَ كُلِّ مِنْهَا ابْتِدَاءً وَانْتِهَاءً. [انظر سنن أبي داود كتاب الصلاة، باب
# ما جاء في المواقيت رقم (٣٩٣)؛ والترمذي أول كتاب الصلاة
# رقم (١٤٩)] .
p5_words = [
    ('قَالَ', 'Telah berfirman', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('اللهُ', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('تَعَالَى:', 'Yang Maha Tinggi:', 'ع ل و', '-', '-', '-', 'Fi\'il Madhi (Hal)', 'Tsulasi Mazid', 'Allah'),
    ('﴿إِنَّ', '﴿Sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('الصَّلَاةَ', 'Shalat itu', 'ص ل ي', '-', '-', '-', 'Isim Inna', '-', '-'),
    ('كَانَتْ', 'Adalah', 'ك و ن', '-', 'Kanat + Ta\' ta\'nits', '-', 'Fi\'il Madhi Naqish (Khabar Inna)', 'Tsulasi Mujarrad', 'Shalat'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْمُؤْمِنِينَ', 'Orang-orang mukmin', 'أ م ن', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('كِتَاباً', 'Sebuah ketetapan', 'ك ت ب', '-', '-', '-', 'Khabar Kanat', '-', '-'),
    ('مَّوْقُوتاً﴾', 'Yang telah ditentukan waktunya﴾', 'و ق ت', '-', '-', '-', 'Na\'at', '-', '-'),
    ('(سورة', '(Surah', '-', '-', '-', '-', 'Khabar (mubtada mahdzuf)', '-', '-'),
    ('النساء:', 'An-Nisa:', 'ن س و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الآية', 'Ayat', 'أ ي ي', '-', '-', '-', 'Badal', '-', '-'),
    ('١٠٣).', '103).', '-', '-', '-', '-', '-', '-', '-'),
    ('أَيْ', 'Yaitu', '-', '-', '-', '-', 'Huruf Tafsir', '-', '-'),
    ('كَانَتْ', 'Adalah ia', 'ك و ن', '-', 'Kanat + Ta\' ta\'nits', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Shalat'),
    ('فَرِيضَةً', 'Sebuah fardhu (kewajiban)', 'ف ر ض', '-', '-', '-', 'Khabar Kanat', '-', '-'),
    ('مُحَدَّدَةً', 'Yang ditentukan batasan-batasannya', 'ح د د', '-', '-', '-', 'Na\'at', '-', '-'),
    ('بِأَوْقَاتٍ', 'Dengan waktu-waktu', 'و ق ت', 'Jamak', 'Baa jar + Awqat', '-', 'Jar Majrur', '-', '-'),
    ('مَخْصُوصَةٍ.', 'Yang dikhususkan.', 'خ ص ص', '-', '-', '-', 'Na\'at', '-', '-'),
    ('وَقَدْ', 'Dan sungguh', '-', '-', 'Wawu + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('ثَبَتَ', 'Telah ditetapkan (shahih)', 'ث ب ت', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Ahadiits'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْأَحَادِيثِ', 'Hadits-hadits', 'ح د ث', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('الصَّحِيحَةِ', 'Yang shahih', 'ص ح ح', '-', '-', '-', 'Na\'at', '-', '-'),
    ('أَنَّ', 'Bahwa', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('جِبْرِيلَ', 'Malaikat Jibril', '-', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('عليه', 'Atasnya', '-', '-', 'Ala + hi', 'hi merujuk ke Jibril', 'Jar Majrur / Khabar Muqaddam', '-', '-'),
    ('السلام', 'Keselamatan', 'س ل م', '-', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('جَاءَ', 'Telah datang', 'ج ي أ', '-', '-', '-', 'Fi\'il Madhi (Khabar Anna)', 'Tsulasi Mujarrad', 'Jibril'),
    ('إِلَى', 'Menemui', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('النَّبِيِّ', 'Nabi', 'ن ب أ', '-', '-', '-', 'Majrur', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('بَعْدَ', 'Setelah', 'ب ع د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('فُرِضَتِ', 'Telah diwajibkan', 'ف ر ض', '-', 'Furidhat + Ta\' ta\'nits', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'As-Shalawat'),
    ('الصَّلَوَاتُ', 'Shalat-shalat', 'ص ل ي', 'Jamak', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('الْخَمْسُ،', 'Lima waktu,', 'خ م س', '-', '-', '-', 'Na\'at', '-', '-'),
    ('يُعَرِّفُهُ', 'Untuk memberitahukan kepadanya', 'ع ر ف', '-', 'Yu\'arrifu + hu', 'hu merujuk ke Nabi', 'Fi\'il Mudhari\' (Hal)', 'Tsulasi Mazid', 'Jibril'),
    ('أَوْقَاتَهَا،', 'Akan waktu-waktunya,', 'و ق ت', 'Jamak', 'Awqata + ha', 'ha merujuk ke shalat', 'Maf\'ul Bih Tsani', '-', '-'),
    ('وَيَضْبِطُ', 'Dan untuk mengatur/memastikan', 'ض ب ط', '-', 'Wawu + Yadhbithu', '-', 'Fi\'il Mudhari\' (Ma\'thuf)', 'Tsulasi Mujarrad', 'Jibril'),
    ('لَهُ', 'Baginya (Nabi)', '-', '-', 'Lam jar + hu', 'hu merujuk ke Nabi', 'Jar Majrur', '-', '-'),
    ('وَقْتَ', 'Waktu', 'و ق ت', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('كُلِّ', 'Bagi masing-masing', 'ك ل ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مِنْهَا', 'Darinya (shalat)', '-', '-', 'Min + ha', 'ha merujuk ke shalat', 'Jar Majrur', '-', '-'),
    ('ابْتِدَاءً', 'Sebagai awal permulaan', 'ب د أ', '-', '-', '-', 'Hal / Tamyiz', '-', '-'),
    ('وَانْتِهَاءً.', 'Maupun batas akhirnya.', 'ن ه ي', '-', 'Wawu + Intiha\'', '-', 'Ma\'thuf', '-', '-'),
    ('[انظر', '[Lihatlah', 'ن ظ ر', '-', '-', '-', 'Fi\'il Amr', 'Tsulasi Mujarrad', 'Pembaca (Anta)'),
    ('سنن', 'Sunan', 'س ن ن', 'Jamak', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('أبي', 'Abu', 'أ ب و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('داود', 'Dawud', 'د و د', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('كتاب', 'Kitab', 'ك ت ب', '-', '-', '-', 'Badal', '-', '-'),
    ('الصلاة،', 'Shalat,', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('باب', 'Bab', 'ب و ب', '-', '-', '-', 'Badal', '-', '-'),
    ('ما', 'Apa-apa yang', '-', '-', '-', '-', 'Isim Maushul', '-', '-'),
    ('جاء', 'Telah datang', 'ج ي أ', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Ma'),
    ('في', 'Dalam hal', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('المواقيت', 'Waktu-waktu pelaksanaan', 'و ق ت', 'Jamak', '-', '-', 'Majrur', '-', '-'),
    ('رقم', 'Nomor', 'ر ق م', '-', '-', '-', 'Hal / Tamyiz', '-', '-'),
    ('٣٩٣)؛', '(393);', '-', '-', '-', '-', '-', '-', '-'),
    ('والترمذي', 'Dan At-Tirmidzi', '-', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('أول', 'Di awal', 'أ و ل', '-', '-', '-', 'Zharf Makan', '-', '-'),
    ('كتاب', 'Kitab', 'ك ت ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الصلاة', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رقم', 'Nomor', 'ر ق م', '-', '-', '-', 'Hal / Tamyiz', '-', '-'),
    ('(١٤٩)]', '(149)]', '-', '-', '-', '-', '-', '-', '-'),
    ('.', '.', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'مَّوْقُوتاً﴾' (9), 'مَخْصُوصَةٍ.' (19), 'إِلَى' (30), 'لَهُ' (41), 'باب' (53), 'الصلاة' (63), '.' (66)
blocks_105.append({
    'type': 'paragraph',
    'ar': 'قَالَ اللهُ تَعَالَى: ﴿إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَاباً مَّوْقُوتاً﴾ (سورة النساء: الآية ١٠٣). أَيْ كَانَتْ فَرِيضَةً مُحَدَّدَةً بِأَوْقَاتٍ مَخْصُوصَةٍ. وَقَدْ ثَبَتَ فِي الْأَحَادِيثِ الصَّحِيحَةِ أَنَّ جِبْرِيلَ عليه السلام جَاءَ إِلَى النَّبِيِّ ﷺ بَعْدَ أَنْ فُرِضَتِ الصَّلَوَاتُ الْخَمْسُ، يُعَرِّفُهُ أَوْقَاتَهَا، وَيَضْبِطُ لَهُ وَقْتَ كُلِّ مِنْهَا ابْتِدَاءً وَانْتِهَاءً. [انظر سنن أبي داود كتاب الصلاة، باب ما جاء في المواقيت رقم (٣٩٣)؛ والترمذي أول كتاب الصلاة رقم (١٤٩)] .',
    'id': 'Allah SWT berfirman: "Sesungguhnya shalat itu adalah sebuah fardhu (kewajiban) yang ditentukan waktunya atas orang-orang yang beriman" (QS. An-Nisa: 103). Artinya, shalat adalah sebuah kewajiban yang telah dibatasi pelaksanaannya dengan waktu-waktu yang dikhususkan. Dan sungguh telah tetap dalam hadits-hadits shahih bahwa Malaikat Jibril AS datang menemui Nabi SAW setelah diwajibkannya shalat lima waktu (Isra Mi\'raj), guna memberitahukan kepada beliau perihal waktu-waktu tersebut. Serta mencontohkan batas patokan waktu pelaksanaannya secara detail bagi setiap shalat, baik dari awal permulaan maupun batas akhirnya. [Lihat Sunan Abu Dawud dalam Kitab As-Shalah, Bab "Ma Jaa\'a fil Mawaqit" hadits no. 393; dan Jami\' At-Tirmidzi pada awal Kitab As-Shalah hadits no. 149].',
    'words': make_words(p5_words, [9, 19, 30, 41, 53, 63, 66])
})


data.append({
    'pageNumber': 105,
    'blocks': blocks_105
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 105 appended to data.js successfully.')
