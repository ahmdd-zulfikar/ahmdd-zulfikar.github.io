import json

# Read current data
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_102 = []

def make_words(word_tuples):
    words = []
    for t in word_tuples:
        words.append({
            'text': t[0],
            'translation': t[1],
            'root': t[2],
            'explanation': t[3],
            'joined_explanation': t[4],
            'pronoun_ref': t[5],
            'irab': t[6],
            'verb_type': t[7],
            'fail_ref': t[8]
        })
    return words

# Para 1 (Continuation of Hadith)
p1_words = [
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أُمَّتِي', 'Umatku', 'أ م م', '-', 'Bersambung dhamir ya', 'ya merujuk ke Rasulullah', 'Majrur', '-', '-'),
    ('خَمْسِينَ', 'Lima puluh', 'خ م س', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('صَلَاةً...', 'Shalat...', 'ص ل ي', '-', '-', '-', 'Tamyiz', '-', '-'),
    ('فَرَاجَعْتُهُ', 'Maka aku meminta (keringanan) pada-Nya', 'ر ج ع', '-', 'Fa + Raja\'a + tu + hu', 'tu merujuk ke Rasul, hu ke Allah', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Rasulullah (Tu)'),
    ('فَقَالَ:', 'Maka Dia berfirman:', 'ق و ل', '-', 'Fa + Qala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('هِيَ', 'Ia (shalat itu)', '-', '-', '-', 'Merujuk ke Shalawat Khams', 'Mubtada\'', '-', '-'),
    ('خَمْسٌ', 'Lima (waktu)', 'خ م س', '-', '-', '-', 'Khabar', '-', '-'),
    ('وَهِيَ', 'Dan ia (bernilai)', '-', '-', 'Wawu + Hiya', 'Merujuk ke Shalawat Khams', 'Mubtada\'', '-', '-'),
    ('خَمْسُونَ،', 'Lima puluh,', 'خ م س', '-', '-', '-', 'Khabar', '-', '-'),
    ('لَا', 'Tidak', '-', '-', '-', '-', 'Huruf Nafi', '-', '-'),
    ('يُبَدَّلُ', 'Bisa diubah', 'ب د ل', '-', '-', '-', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mazid', 'Al-Qawl'),
    ('الْقَوْلُ', 'Ketetapan/Firman', 'ق و ل', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('لَدَيَّ».', 'Di sisi-Ku».', 'ل د ي', '-', 'Lada + ya (mutakallim)', 'ya merujuk ke Allah', 'Zharf Makan', '-', '-')
]
blocks_102.append({'type': 'paragraph', 'ar': 'عَلَى أُمَّتِي خَمْسِينَ صَلَاةً... فَرَاجَعْتُهُ فَقَالَ: هِيَ خَمْسٌ وَهِيَ خَمْسُونَ، لَا يُبَدَّلُ الْقَوْلُ لَدَيَّ».', 'id': 'Atas umatku sebanyak lima puluh shalat... Maka aku pun memohon keringanan kepada-Nya. Lalu Allah berfirman: "Ia (pelaksanaannya) lima waktu, dan ia (pahalanya bernilai) lima puluh. Ketetapan-Ku tidak dapat diubah".', 'words': make_words(p1_words)})

# Para 2
p2_words = [
    ('وَالصَّحِيحُ', 'Dan pendapat yang shahih', 'ص ح ح', '-', 'Wawu + As-Shahih', '-', 'Mubtada\'', '-', '-'),
    ('أَنَّ', 'Bahwa sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('حَادِثَةَ', 'Peristiwa', 'ح د ث', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('الْإِسْرَاءِ', 'Isra\'', 'س ر ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('كَانَتْ', 'Itu terjadi', 'ك و ن', '-', 'Bersambung ta\' ta\'nits', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Haditsatul Isra\''),
    ('قَبْلَ', 'Sebelum', 'ق ب ل', '-', '-', '-', 'Zharf Zaman / Khabar Kanat', '-', '-'),
    ('هِجْرَةِ', 'Hijrahnya', 'ه ج ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('النَّبِيِّ', 'Nabi', 'ن ب أ', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('عَلَيْهِ', 'Atasnya', '-', '-', 'Ala + hi', 'hi merujuk ke Nabi', 'Jar Majrur', '-', '-'),
    ('الصَّلَاةُ', 'Shalawat', 'ص ل ي', '-', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('وَالسَّلَامُ', 'Dan keselamatan', 'س ل م', '-', 'Wawu + Salam', '-', 'Ma\'thuf', '-', '-'),
    ('إِلَى', 'Ke', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْمَدِينَةِ', 'Madinah', 'م د ن', '-', '-', '-', 'Majrur', '-', '-'),
    ('بِثَمَانِيَةِ', 'Terpaut delapan', 'ث م ن', '-', 'Baa jar + Tsamaniyah', '-', 'Jar Majrur', '-', '-'),
    ('عَشَرَ', 'Belas', 'ع ش ر', '-', '-', '-', 'Juz Mabni (Bilangan)', '-', '-'),
    ('شَهْراً؛', 'Bulan;', 'ش ه ر', '-', '-', '-', 'Tamyiz', '-', '-'),
    ('وَإِذًا', 'Oleh karena itu', '-', '-', 'Wawu + Idzan', '-', 'Huruf Jawab', '-', '-'),
    ('فَإِنَّ', 'Maka sesungguhnya', '-', '-', 'Fa + Inna', '-', 'Amil Nawasikh', '-', '-'),
    ('الصَّلَوَاتِ', 'Shalat-shalat', 'ص ل ي', '-', '-', '-', 'Isim Inna', '-', '-'),
    ('الْخَمْسَ', 'Lima (waktu)', 'خ م س', '-', '-', '-', 'Na\'at', '-', '-'),
    ('الْمَكْتُوبَةَ', 'Yang diwajibkan', 'ك ت ب', '-', '-', '-', 'Na\'at 2', '-', '-'),
    ('نَسَخَتِ', 'Telah menghapus (hukum)', 'ن س خ', '-', 'Bersambung ta\' ta\'nits', '-', 'Fi\'il Madhi / Khabar Inna', 'Tsulasi Mujarrad', 'As-Shalawat'),
    ('الرَّكْعَتَيْنِ', 'Dua rakaat', 'ر ك ع', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('اللَّتَيْنِ', 'Yang', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('كَانَتَا', 'Dahulu keduanya ada', 'ك و ن', '-', 'Kana + Alif Itsnain', 'Alif merujuk ke dua rakaat', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Rak\'ataini (Alif)'),
    ('فِي', 'Pada', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الصَّبَاحِ', 'Pagi', 'ص ب ح', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَالْمَسَاءِ.', 'Dan sore.', 'م س و', '-', 'Wawu + Masa\'', '-', 'Ma\'thuf', '-', '-')
]
blocks_102.append({'type': 'paragraph', 'ar': 'وَالصَّحِيحُ أَنَّ حَادِثَةَ الْإِسْرَاءِ كَانَتْ قَبْلَ هِجْرَةِ النَّبِيِّ عليه الصلاة والسلام إِلَى الْمَدِينَةِ بِثَمَانِيَةِ عَشَرَ شَهْراً؛ وَإِذًا فَإِنَّ الصَّلَوَاتِ الْخَمْسَ الْمَكْتُوبَةَ نَسَخَتِ الرَّكْعَتَيْنِ اللَّتَيْنِ كَانَتَا فِي الصَّبَاحِ وَالْمَسَاءِ.', 'id': 'Pendapat yang paling kuat menyatakan bahwa peristiwa Isra\' Mi\'raj terjadi sebelum hijrahnya Nabi SAW ke Madinah dengan selisih waktu delapan belas bulan. Oleh karena itu, kewajiban shalat lima waktu ini telah menghapus (nasakh) hukum shalat dua rakaat yang sebelumnya didirikan di waktu pagi dan sore.', 'words': make_words(p2_words)})

# Heading 1
h1_words = [
    ('دَلِيلُ', 'Dalil (Dasar Hukum)', 'د ل ل', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('مَشْرُوعِيَّتِهَا', 'Disyariatkannya', 'ش ر ع', '-', 'Bersambung dhamir ha', 'ha merujuk ke Shalat', 'Mudhaf Ilaih', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_102.append({'type': 'heading', 'ar': 'دَلِيلُ مَشْرُوعِيَّتِهَا :', 'id': 'Dalil Disyariatkannya (Shalat):', 'words': make_words(h1_words)})

# Para 3
p3_words = [
    ('ثَبَتَتْ', 'Telah tetap/disyariatkan', 'ث ب ت', '-', 'Bersambung ta\' ta\'nits', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Masyru\'iyyah'),
    ('مَشْرُوعِيَّةُ', 'Pensyariatan', 'ش ر ع', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('الصَّلَاةِ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('بِآيَاتٍ', 'Dengan ayat-ayat', 'أ ي ي', '-', 'Baa jar + Ayat', '-', 'Jar Majrur', '-', '-'),
    ('كَثِيرَةٍ', 'Yang banyak', 'ك ث ر', '-', '-', '-', 'Na\'at', '-', '-'),
    ('مِنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('كِتَابِ', 'Kitab', 'ك ت ب', '-', '-', '-', 'Majrur', '-', '-'),
    ('اللهِ،', 'Allah,', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَبِأَحَادِيثَ', 'Dan dengan hadits-hadits', 'ح د ث', '-', 'Wawu + Baa + Ahadits', '-', 'Ma\'thuf / Jar Majrur', '-', '-'),
    ('كَثِيرَةٍ', 'Yang banyak', 'ك ث ر', '-', '-', '-', 'Na\'at', '-', '-'),
    ('مِنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('سُنَّةِ', 'Sunnah', 'س ن ن', '-', '-', '-', 'Majrur', '-', '-'),
    ('رَسُولِ', 'Rasul', 'ر س ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('.', '.', '-', '-', '-', '-', '-', '-', '-')
]
blocks_102.append({'type': 'paragraph', 'ar': 'ثَبَتَتْ مَشْرُوعِيَّةُ الصَّلَاةِ بِآيَاتٍ كَثِيرَةٍ مِنْ كِتَابِ اللهِ، وَبِأَحَادِيثَ كَثِيرَةٍ مِنْ سُنَّةِ رَسُولِ اللهِ ﷺ .', 'id': 'Pensyariatan shalat telah ditetapkan oleh banyak ayat dari Kitabullah (Al-Qur\'an), serta banyak hadits dari Sunnah Rasulullah SAW.', 'words': make_words(p3_words)})

# Para 4
p4_words = [
    ('فَمِنَ', 'Maka di antara', '-', '-', 'Fa + Min', '-', 'Huruf Jar', '-', '-'),
    ('الْقُرْآنِ:', 'Al-Qur\'an:', 'ق ر أ', '-', '-', '-', 'Majrur / Khabar Muqaddam', '-', '-'),
    ('قَوْلُهُ', 'Firman-Nya', 'ق و ل', '-', 'Bersambung dhamir hu', 'hu merujuk ke Allah', 'Mubtada\' Muakhkhar', '-', '-'),
    ('تَعَالَى:', 'Yang Maha Tinggi:', 'ع ل و', '-', '-', '-', 'Fi\'il Madhi (Hal)', 'Tsulasi Mazid', 'Allah'),
    ('﴿فَسُبْحَانَ', '﴿Maka bertasbihlah (Maha Suci)', 'س ب ح', '-', 'Fa + Subhana', '-', 'Maf\'ul Muthlaq', '-', '-'),
    ('اللَّهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('حِينَ', 'Ketika', 'ح ي ن', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('تُمْسُونَ', 'Kalian berada di waktu sore', 'م س و', '-', 'Amsa + Wawu Jama\'ah', 'Wawu merujuk ke kaum muslimin', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Kalian (Wawu)'),
    ('وَحِينَ', 'Dan ketika', 'ح ي ن', '-', 'Wawu + Hina', '-', 'Ma\'thuf / Zharf Zaman', '-', '-'),
    ('تُصْبِحُونَ', 'Kalian berada di waktu pagi', 'ص ب ح', '-', 'Asbaha + Wawu Jama\'ah', 'Wawu merujuk ke kaum muslimin', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Kalian (Wawu)'),
    ('*', '*', '-', '-', '-', '-', '-', '-', '-'),
    ('وَلَهُ', 'Dan bagi-Nyalah', '-', '-', 'Wawu + Lam + hu', 'hu merujuk ke Allah', 'Jar Majrur / Khabar', '-', '-'),
    ('الْحَمْدُ', 'Segala puji', 'ح م د', '-', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('فِي', 'Di', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('السَّمَوَاتِ', 'Langit', 'س م و', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَالْأَرْضِ', 'Dan bumi', 'أ ر ض', '-', 'Wawu + Al-Ardh', '-', 'Ma\'thuf', '-', '-'),
    ('وَعَشِيًّا', 'Dan di waktu petang', 'ع ش ي', '-', 'Wawu + Asyiyyan', '-', 'Ma\'thuf / Zharf Zaman', '-', '-'),
    ('وَحِينَ', 'Dan ketika', 'ح ي ن', '-', 'Wawu + Hina', '-', 'Ma\'thuf / Zharf Zaman', '-', '-'),
    ('تُظْهِرُونَ﴾', 'Kalian berada di waktu zhuhur﴾', 'ظ ه ر', '-', 'Azhhara + Wawu Jama\'ah', 'Wawu merujuk ke kaum muslimin', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Kalian (Wawu)'),
    ('(سُورَةُ', '(Surat', 'س و ر', '-', '-', '-', 'Khabar mahdzuf', '-', '-'),
    ('الرُّومِ:', 'Ar-Rum:', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْآيَات', 'Ayat', 'أ ي ي', '-', '-', '-', 'Badal', '-', '-'),
    ('١٧', '17', '-', '-', '-', '-', '-', '-', '-'),
    ('و١٨).', 'dan 18).', '-', '-', '-', '-', '-', '-', '-'),
    ('قَالَ', 'Telah berkata', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Ibnu Abbas'),
    ('ابْنُ', 'Ibnu', 'ب ن ي', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَبَّاسٍ', 'Abbas', 'ع ب س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنهما:', 'Atas keduanya:', '-', '-', 'An + huma', 'huma merujuk ke Ibnu Abbas dan ayahnya', 'Jar Majrur', '-', '-'),
    ('أَرَادَ', 'Ia (Allah) bermaksud', 'ر و د', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Allah'),
    ('بِقَوْلِهِ:', 'Dengan firman-Nya:', 'ق و ل', '-', 'Baa + Qaul + hi', 'hi merujuk ke Allah', 'Jar Majrur', '-', '-'),
    ('﴿حِينَ', '﴿Ketika', 'ح ي ن', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('تُمْسُونَ﴾:', 'Kalian berada di waktu sore﴾:', 'م س و', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Kalian (Wawu)'),
    ('صَلَاةَ', 'Yaitu Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih (Penjelasan dari Aroda)', '-', '-'),
    ('الْمَغْرِبِ', 'Maghrib', 'غ ر ب', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَالْعِشَاءِ،', 'Dan Isya\',', 'ع ش و', '-', 'Wawu + Al-Isha\'', '-', 'Ma\'thuf', '-', '-'),
    ('﴿وَحِينَ', '﴿Dan ketika', 'ح ي ن', '-', 'Wawu + Hina', '-', 'Zharf Zaman', '-', '-'),
    ('تُصْبِحُونَ﴾:', 'Kalian berada di waktu pagi﴾:', 'ص ب ح', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Kalian (Wawu)'),
    ('صَلَاةَ', 'Yaitu Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('الصُّبْحِ،', 'Subuh,', 'ص ب ح', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('﴿وَعَشِيًّا﴾:', '﴿Dan waktu petang﴾:', 'ع ش ي', '-', 'Wawu + Asyiyyan', '-', 'Zharf Zaman', '-', '-'),
    ('صَلَاةَ', 'Yaitu Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('الْعَصْرِ،', 'Ashar,', 'ع ص ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('﴿وَحِينَ', '﴿Dan ketika', 'ح ي ن', '-', 'Wawu + Hina', '-', 'Zharf Zaman', '-', '-'),
    ('تُظْهِرُونَ﴾:', 'Kalian berada di waktu zhuhur﴾:', 'ظ ه ر', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Kalian (Wawu)'),
    ('صَلَاةَ', 'Yaitu Shalat', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('الظُّهْرِ.', 'Zhuhur.', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-')
]
blocks_102.append({'type': 'paragraph', 'ar': 'فَمِنَ الْقُرْآنِ: قَوْلُهُ تَعَالَى: ﴿فَسُبْحَانَ اللَّهِ حِينَ تُمْسُونَ وَحِينَ تُصْبِحُونَ * وَلَهُ الْحَمْدُ فِي السَّمَوَاتِ وَالْأَرْضِ وَعَشِيًّا وَحِينَ تُظْهِرُونَ﴾ (سورة الروم: الآيات ١٧ و١٨). قَالَ ابْنُ عَبَّاسٍ رضي الله عنهما: أَرَادَ بِقَوْلِهِ: ﴿حِينَ تُمْسُونَ﴾: صَلَاةَ الْمَغْرِبِ وَالْعِشَاءِ، ﴿وَحِينَ تُصْبِحُونَ﴾: صَلَاةَ الصُّبْحِ، ﴿وَعَشِيًّا﴾: صَلَاةَ الْعَصْرِ، ﴿وَحِينَ تُظْهِرُونَ﴾: صَلَاةَ الظُّهْرِ.', 'id': 'Dalil dari Al-Qur\'an adalah firman Allah Ta\'ala: "Maka bertasbihlah kepada Allah di waktu kamu berada di petang hari dan waktu kamu berada di waktu subuh, dan bagi-Nya-lah segala puji di langit dan di bumi dan di waktu kamu berada pada petang hari dan di waktu kamu berada di waktu zhuhur." (QS. Ar-Rum: Ayat 17 & 18). Ibnu Abbas RA berkata: Yang dimaksud oleh Allah dengan firman-Nya "Ketika kamu berada di petang hari" adalah shalat Maghrib dan Isya, "Ketika kamu berada di waktu pagi" adalah shalat Subuh, "Dan di waktu petang" adalah shalat Ashar, dan "Ketika kamu berada di waktu zhuhur" adalah shalat Zhuhur.', 'words': make_words(p4_words)})

# Para 5
p5_words = [
    ('وَقَوْلُهُ', 'Dan firman-Nya', 'ق و ل', '-', 'Wawu + Qaul + hu', 'hu merujuk ke Allah', 'Ma\'thuf', '-', '-'),
    ('تَعَالَى:', 'Yang Maha Tinggi:', 'ع ل و', '-', '-', '-', 'Fi\'il Madhi (Hal)', 'Tsulasi Mazid', 'Allah'),
    ('﴿إِنَّ', '﴿Sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('الصَّلَاةَ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Isim Inna', '-', '-'),
    ('كَانَتْ', 'Adalah ia', 'ك و ن', '-', 'Bersambung ta\' ta\'nits', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'As-Shalah'),
    ('عَلَى', 'Atas/Bagi', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْمُؤْمِنِينَ', 'Orang-orang beriman', 'أ م ن', '-', '-', '-', 'Majrur', '-', '-'),
    ('كِتَابًا', 'Kewajiban', 'ك ت ب', '-', '-', '-', 'Khabar Kanat', '-', '-'),
    ('مَّوْقُوتًا﴾', 'Yang telah ditentukan waktunya﴾', 'و ق ت', '-', '-', '-', 'Na\'at', '-', '-'),
    ('(سُورَةُ', '(Surat', 'س و ر', '-', '-', '-', 'Khabar mahdzuf', '-', '-'),
    ('النِّسَاءِ:', 'An-Nisa:', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْآيَة', 'Ayat', 'أ ي ي', '-', '-', '-', 'Badal', '-', '-'),
    ('١٠٣).', '103).', '-', '-', '-', '-', '-', '-', '-'),
    ('أَيْ', 'Yaitu/Artinya', '-', '-', '-', '-', 'Huruf Tafsir', '-', '-'),
    ('مَحْتُومَةً', 'Telah ditetapkan/diwajibkan', 'ح ت م', '-', '-', '-', 'Khabar mahdzuf', '-', '-'),
    ('وَمُوَقَّتَةً', 'Dan diberi batas waktu', 'و ق ت', '-', 'Wawu + Muwaqqatah', '-', 'Ma\'thuf', '-', '-'),
    ('بِأَوْقَاتٍ', 'Dengan waktu-waktu', 'و ق ت', '-', 'Baa jar + Awqat', '-', 'Jar Majrur', '-', '-'),
    ('مَخْصُوصَةٍ.', 'Yang khusus/tertentu.', 'خ ص ص', '-', '-', '-', 'Na\'at', '-', '-')
]
blocks_102.append({'type': 'paragraph', 'ar': 'وَقَوْلُهُ تَعَالَى: ﴿إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَّوْقُوتًا﴾ (سورة النساء: الآية ١٠٣). أَيْ مَحْتُومَةً وَمُوَقَّتَةً بِأَوْقَاتٍ مَخْصُوصَةٍ.', 'id': 'Dan firman Allah Ta\'ala: "Sesungguhnya shalat itu adalah fardhu/kewajiban yang ditentukan waktunya atas orang-orang yang beriman." (QS. An-Nisa: Ayat 103). Artinya, diwajibkan dan dibatasi dengan waktu-waktu tertentu.', 'words': make_words(p5_words)})

# Para 6
p6_words = [
    ('وَمِنَ', 'Dan di antara', '-', '-', 'Wawu + Min', '-', 'Huruf Jar', '-', '-'),
    ('السُّنَّةِ:', 'Sunnah:', 'س ن ن', '-', '-', '-', 'Majrur / Khabar Muqaddam', '-', '-'),
    ('حَدِيثُ', 'Hadits', 'ح د ث', '-', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('الْإِسْرَاءِ', 'Isra\'', 'س ر ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('السَّابِقُ.', 'Yang telah lalu/disebut sebelumnya.', 'س ب ق', '-', '-', '-', 'Na\'at', '-', '-')
]
blocks_102.append({'type': 'paragraph', 'ar': 'وَمِنَ السُّنَّةِ: حَدِيثُ الْإِسْرَاءِ السَّابِقُ.', 'id': 'Adapun dalil dari As-Sunnah (Hadits): Yaitu Hadits tentang peristiwa Isra\' yang telah disebutkan sebelumnya.', 'words': make_words(p6_words)})

# Para 7
p7_words = [
    ('وَمَا', 'Dan apa yang', '-', '-', 'Wawu + Ma Maushul', '-', 'Ma\'thuf / Mubtada\'', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan oleh', 'ر و ي', '-', 'Bersambung dhamir hu', 'hu merujuk ke Ma', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Bukhari'),
    ('الْبُخَارِيُّ', 'Al-Bukhari', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(١٣٣١)؛', '(1331);', '-', '-', '-', '-', '-', '-', '-'),
    ('وَمُسْلِمٌ', 'Dan Muslim', 'س ل م', '-', 'Wawu + Muslim', '-', 'Ma\'thuf', '-', '-'),
    ('(١٩)،', '(19),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنِ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('ابْنِ', 'Ibnu', 'ب ن ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('عَبَّاسٍ', 'Abbas', 'ع ب س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنهما:', 'Keduanya:', '-', '-', 'An + huma', 'huma merujuk ke Ibnu Abbas dan ayahnya', 'Jar Majrur', '-', '-'),
    ('أَنَّ', 'Bahwa sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('النَّبِيَّ', 'Nabi', 'ن ب أ', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('بَعَثَ', 'Telah mengutus', 'ب ع ث', '-', '-', '-', 'Fi\'il Madhi / Khabar Anna', 'Tsulasi Mujarrad', 'Nabi Muhammad'),
    ('مُعَاذًا', 'Mu\'adz', 'ع و ذ', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Muadz', 'Jar Majrur', '-', '-'),
    ('إِلَى', 'Ke', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْيَمَنِ', 'Yaman', 'ي م ن', '-', '-', '-', 'Majrur', '-', '-'),
    ('فَقَالَ:', 'Lalu beliau bersabda:', 'ق و ل', '-', 'Fa + Qala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi Muhammad'),
    ('«ادْعُهُمْ', '«Serulah/Ajaklah mereka', 'د ع و', '-', 'Id\'u + hum', 'hum merujuk ke penduduk Yaman', 'Fi\'il Amr', 'Tsulasi Mujarrad', 'Muadz (Anta)'),
    ('إِلَى', 'Kepada', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('شَهَادَةِ', 'Persaksian', 'ش ه د', '-', '-', '-', 'Majrur', '-', '-'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('لَا', 'Tidak ada', '-', '-', '-', '-', 'Laa Nafi Lil Jinsi', '-', '-'),
    ('إِلَهَ', 'Tuhan', 'أ ل ه', '-', '-', '-', 'Isim Laa', '-', '-'),
    ('إِلَّا', 'Selain', '-', '-', '-', '-', 'Huruf Istitsna\'', '-', '-'),
    ('اللَّهُ', 'Allah', '-', '-', '-', '-', 'Khabar Laa / Badal', '-', '-'),
    ('وَأَنِّي', 'Dan bahwa aku (bersaksi)', '-', '-', 'Wawu + Anna + Ya', 'ya merujuk ke Rasulullah', 'Amil Nawasikh', '-', '-'),
    ('مُحَمَّدًا', 'Muhammad', 'ح م د', '-', '-', '-', 'Isim Anna / Khabar Anna', '-', '-'),
    ('رَّسُولُ', 'Utusan', 'ر س ل', '-', '-', '-', 'Khabar Anna', '-', '-'),
    ('اللَّهِ،', 'Allah,', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَإِنْ', 'Maka jika', '-', '-', 'Fa + In', '-', 'Huruf Syarat', '-', '-'),
    ('هُمْ', 'Mereka', '-', '-', '-', '-', 'Mubtada\'', '-', '-')
]
blocks_102.append({'type': 'paragraph', 'ar': 'وَمَا رَوَاهُ الْبُخَارِيُّ (١٣٣١)؛ وَمُسْلِمٌ (١٩)، عَنِ ابْنِ عَبَّاسٍ رضي الله عنهما: أَنَّ النَّبِيَّ ﷺ بَعَثَ مُعَاذًا رضي الله عنه إِلَى الْيَمَنِ فَقَالَ: «ادْعُهُمْ إِلَى شَهَادَةِ أَنْ لَا إِلَهَ إِلَّا اللَّهُ وَأَنِّي مُحَمَّدًا رَّسُولُ اللَّهِ، فَإِنْ هُمْ', 'id': 'Dan (dalil berikutnya) adalah Hadits yang diriwayatkan oleh Al-Bukhari (1331) dan Muslim (19), dari Ibnu Abbas RA: Bahwasanya Nabi SAW mengutus Mu\'adz RA ke Yaman, lalu beliau bersabda: "Ajaklah mereka kepada persaksian bahwa tiada Tuhan (yang berhak disembah) melainkan Allah dan bahwa aku adalah Muhammad utusan Allah, maka jika mereka...', 'words': make_words(p7_words)})

data.append({
    'pageNumber': 102,
    'blocks': blocks_102
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 102 appended to data.js successfully.')
