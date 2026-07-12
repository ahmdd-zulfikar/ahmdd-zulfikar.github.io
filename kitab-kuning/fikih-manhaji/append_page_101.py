import json

# Read current data
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_101 = []

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

# Heading 1
h1_words = [
    ('تَارِيخُ', 'Sejarah', 'ت ر خ', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('مَشْرُوعِيَّتِهَا', 'Disyariatkannya', 'ش ر ع', '-', 'Bersambung dhamir ha', 'ha merujuk ke Shalat', 'Mudhaf Ilaih', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_101.append({'type': 'heading', 'ar': 'تَارِيخُ مَشْرُوعِيَّتِهَا :', 'id': 'Sejarah Disyariatkannya (Shalat):', 'words': make_words(h1_words)})

# Para 1
p1_words = [
    ('الصَّلَاةُ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('مِنَ', 'Termasuk dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْعِبَادَاتِ', 'Ibadah-ibadah', 'ع ب د', 'Jamak', '-', '-', 'Majrur / Khabar', '-', '-'),
    ('الْقَدِيمَةِ', 'Yang terdahulu', 'ق د م', '-', '-', '-', 'Na\'at', '-', '-'),
    ('فِي', 'Dalam hal', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('مَشْرُوعِيَّتِهَا،', 'Disyariatkannya,', 'ش ر ع', '-', 'Bersambung dhamir ha', 'ha merujuk ke Shalat', 'Majrur', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('قَالَ', 'Telah berfirman', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('تَعَالَى', 'Yang Maha Tinggi', 'ع ل و', '-', '-', '-', 'Fi\'il Madhi (Hal)', 'Tsulasi Mazid', 'Allah'),
    ('عَنْ', 'Tentang', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('سَيِّدِنَا', 'Sayyid kita (Nabi)', 'س و د', '-', 'Bersambung dhamir na', 'na merujuk ke umat', 'Majrur', '-', '-'),
    ('إِسْمَاعِيلَ', 'Ismail', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('عَلَيْهِ', 'Atasnya', '-', '-', 'Ala + hu', 'hu merujuk ke Ismail', 'Jar Majrur / Khabar Muqaddam', '-', '-'),
    ('السَّلَامُ:', 'Keselamatan:', 'س ل م', '-', '-', '-', 'Mubtada\' Muakhkhar', '-', '-'),
    ('﴿وَكَانَ', '﴿Dan dia (Ismail) adalah', 'ك و ن', '-', 'Wawu + Kana', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Ismail'),
    ('يَأْمُرُ', 'Dia memerintahkan', 'أ م ر', '-', '-', '-', 'Fi\'il Mudhari\' / Khabar Kana', 'Tsulasi Mujarrad', 'Ismail'),
    ('أَهْلَهُ', 'Keluarganya', 'أ ه ل', '-', 'Bersambung dhamir hu', 'hu merujuk ke Ismail', 'Maf\'ul Bih', '-', '-'),
    ('بِالصَّلَاةِ', 'Dengan (mendirikan) shalat', 'ص ل ي', '-', 'Baa jar + As-Shalah', '-', 'Jar Majrur', '-', '-'),
    ('وَالزَّكَاةِ', 'Dan (menunaikan) zakat', 'ز ك و', '-', 'Wawu athaf + Az-Zakah', '-', 'Ma\'thuf', '-', '-'),
    ('وَكَانَ', 'Dan dia adalah', 'ك و ن', '-', 'Wawu + Kana', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Ismail'),
    ('عِنْدَ', 'Di sisi', 'ع ن د', '-', '-', '-', 'Zharf', '-', '-'),
    ('رَبِّهِ', 'Tuhannya', 'ر ب ب', '-', 'Bersambung dhamir hi', 'hi merujuk ke Ismail', 'Mudhaf Ilaih', '-', '-'),
    ('مَرْضِيًّا﴾', 'Seorang yang diridhai﴾', 'ر ض ي', '-', '-', '-', 'Khabar Kana', '-', '-'),
    ('(سُورَةُ', '(Surat', 'س و ر', '-', '-', '-', 'Khabar mubtada mahdzuf', '-', '-'),
    ('مَرْيَمَ:', 'Maryam:', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْآيَة', 'Ayat', 'أ ي ي', '-', '-', '-', 'Badal', '-', '-'),
    ('٥٥)؛', '55);', '-', '-', '-', '-', '-', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('عَرَفَتْهَا', 'Telah mengenalnya (shalat)', 'ع ر ف', '-', 'Bersambung dhamir ha', 'ha merujuk ke Shalat', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Hanifiyyah'),
    ('الْحَنِيفِيَّةُ', 'Agama Hanif (lurus)', 'ح ن ف', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('الَّتِي', 'Yang', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('بُعِثَ', 'Diutus', 'ب ع ث', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Ibrahim'),
    ('بِهَا', 'Dengannya', '-', '-', 'Baa + ha', 'ha merujuk ke Al-Hanifiyyah', 'Jar Majrur', '-', '-'),
    ('إِبْرَاهِيمُ،', 'Ibrahim,', '-', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('وَعَرَفَهَا', 'Dan telah mengenalnya', 'ع ر ف', '-', 'Wawu + Fiil + ha', 'ha merujuk ke Shalat', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Atba\''),
    ('أَتْبَاعُ', 'Para pengikut', 'ت ب ع', 'Jamak dari tabi\'', '-', '-', 'Fa\'il', '-', '-'),
    ('مُوسَى', 'Musa', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('عَلَيْهِ', 'Atasnya', '-', '-', 'Ala + hi', 'hi merujuk ke Musa', 'Jar Majrur', '-', '-'),
    ('السَّلَامُ،', 'Keselamatan,', 'س ل م', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('وَقَالَ', 'Dan berfirman', 'ق و ل', '-', 'Wawu + Qala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('تَعَالَى', 'Yang Maha Tinggi', 'ع ل و', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Allah'),
    ('عَلَى', 'Lewat/Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('لِسَانِ', 'Lisan/Ucapan', 'ل س ن', '-', '-', '-', 'Majrur', '-', '-'),
    ('عِيسَى', 'Isa', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('عَلَيْهِ', 'Atasnya', '-', '-', '-', '-', 'Jar Majrur', '-', '-'),
    ('السَّلَامُ:', 'Keselamatan:', 'س ل م', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('﴿وَأَوْصَانِي', '﴿Dan Dia (Allah) memerintahkan/mewasiatkan kepadaku', 'و ص ي', '-', 'Wawu + Awsha + ni', 'ni merujuk ke Isa', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Allah'),
    ('بِالصَّلَاةِ', 'Untuk (mendirikan) shalat', 'ص ل ي', '-', 'Baa + As-Shalah', '-', 'Jar Majrur', '-', '-'),
    ('وَالزَّكَاةِ', 'Dan (menunaikan) zakat', 'ز ك و', '-', 'Wawu + Az-Zakah', '-', 'Ma\'thuf', '-', '-'),
    ('مَا', 'Selama', '-', '-', '-', '-', 'Huruf Mashdariyyah Zharfiyyah', '-', '-'),
    ('دُمْتُ', 'Aku masih', 'د و م', '-', 'Dama + tu', 'tu merujuk ke Isa', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Isa (Tu)'),
    ('حَيًّا﴾', 'Hidup﴾', 'ح ي ي', '-', '-', '-', 'Khabar Dama', '-', '-'),
    ('(سُورَةُ', '(Surat', 'س و ر', '-', '-', '-', 'Khabar mahdzuf', '-', '-'),
    ('مَرْيَمَ:', 'Maryam:', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْآيَة', 'Ayat', 'أ ي ي', '-', '-', '-', 'Badal', '-', '-'),
    ('٣١).', '31).', '-', '-', '-', '-', '-', '-', '-')
]
blocks_101.append({'type': 'paragraph', 'ar': 'الصَّلَاةُ مِنَ الْعِبَادَاتِ الْقَدِيمَةِ فِي مَشْرُوعِيَّتِهَا، فَقَدْ قَالَ تَعَالَى عَنْ سَيِّدِنَا إِسْمَاعِيلَ عَلَيْهِ السَّلَامُ: ﴿وَكَانَ يَأْمُرُ أَهْلَهُ بِالصَّلَاةِ وَالزَّكَاةِ وَكَانَ عِنْدَ رَبِّهِ مَرْضِيًّا﴾ (سورة مريم: الآية ٥٥)؛ فَقَدْ عَرَفَتْهَا الْحَنِيفِيَّةُ الَّتِي بُعِثَ بِهَا إِبْرَاهِيمُ، وَعَرَفَهَا أَتْبَاعُ مُوسَى عَلَيْهِ السَّلَامُ، وَقَالَ تَعَالَى عَلَى لِسَانِ عِيسَى عَلَيْهِ السَّلَامُ: ﴿وَأَوْصَانِي بِالصَّلَاةِ وَالزَّكَاةِ مَا دُمْتُ حَيًّا﴾ (سورة مريم: الآية ٣١).', 'id': 'Shalat termasuk dari ibadah-ibadah yang terdahulu pensyariatannya. Sungguh Allah Ta\'ala telah berfirman mengenai Nabi Ismail AS: "Dan ia menyuruh keluarganya untuk bersembahyang dan menunaikan zakat, dan ia adalah seorang yang diridhai di sisi Tuhannya." (QS. Maryam: 55). Agama Hanif yang dibawa oleh Nabi Ibrahim juga telah mengenal shalat, begitu pula para pengikut Nabi Musa AS. Dan Allah Ta\'ala berfirman melalui lisan Nabi Isa AS: "Dan Dia memerintahkan kepadaku (mendirikan) shalat dan (menunaikan) zakat selama aku masih hidup." (QS. Maryam: 31).', 'words': make_words(p1_words)})

# Para 2
p2_words = [
    ('وَعِنْدَمَا', 'Dan ketika', 'ع ن د', '-', 'Wawu + Inda + Ma', '-', 'Zharf Zaman', '-', '-'),
    ('بُعِثَ', 'Diutus', 'ب ع ث', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Nabiyyuna'),
    ('نَبِيُّنَا', 'Nabi kita', 'ن ب أ', '-', 'Bersambung dhamir na', 'na merujuk ke umat Islam', 'Na\'ib Fa\'il', '-', '-'),
    ('مُحَمَّدٌ', 'Muhammad', 'ح م د', '-', '-', '-', 'Badal', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('كَانَ', 'Adalah beliau', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Muhammad'),
    ('يُصَلِّي', 'Shalat', 'ص ل ي', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Muhammad'),
    ('رَكْعَتَيْنِ', 'Dua rakaat', 'ر ك ع', '-', '-', '-', 'Maf\'ul Muthlaq', '-', '-'),
    ('كُلَّ', 'Setiap', 'ك ل ل', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('صَبَاحٍ', 'Pagi', 'ص ب ح', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَيُصَلِّي', 'Dan beliau shalat', 'ص ل ي', '-', 'Wawu + Yushalli', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Muhammad'),
    ('رَكْعَتَيْنِ', 'Dua rakaat', 'ر ك ع', '-', '-', '-', 'Maf\'ul Muthlaq', '-', '-'),
    ('كُلَّ', 'Setiap', 'ك ل ل', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('مَسَاءٍ،', 'Sore,', 'م س و', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('قِيلَ:', 'Dikatakan (ulama berpendapat):', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Maqulatul Qaul (Wahuma...)'),
    ('وَهُمَا', 'Dan keduanya (dua shalat itu)', '-', '-', 'Wawu + Huma', 'Huma merujuk ke Shalat pagi & sore', 'Mubtada\'', '-', '-'),
    ('الْمَقْصُودَتَانِ', 'Yang dimaksudkan', 'ق ص د', '-', '-', '-', 'Khabar', '-', '-'),
    ('بِقَوْلِ', 'Dengan firman', 'ق و ل', '-', 'Baa jar + Qaul', '-', 'Jar Majrur', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('تَعَالَى', 'Yang Maha Tinggi', 'ع ل و', '-', '-', '-', 'Fi\'il Madhi (Hal)', 'Tsulasi Mazid', 'Allah'),
    ('خِطَاباً', 'Sebagai seruan/khitab', 'خ ط ب', '-', '-', '-', 'Hal / Maf\'ul Muthlaq', '-', '-'),
    ('لِنَبِيِّهِ', 'Kepada nabi-Nya', 'ن ب أ', '-', 'Lam jar + Nabi + hi', 'hi merujuk ke Allah', 'Jar Majrur', '-', '-'),
    ('ﷺ:', 'SAW:', '-', '-', '-', '-', '-', '-', '-'),
    ('﴿وَسَبِّحْ', '﴿Dan bertasbihlah (shalatlah)', 'س ب ح', 'Maknanya shalat', 'Wawu + Sabbih', '-', 'Fi\'il Amr', 'Tsulasi Mazid', 'Nabi Muhammad (Anta)'),
    ('بِحَمْدِ', 'Dengan memuji', 'ح م د', '-', 'Baa jar + Hamd', '-', 'Jar Majrur', '-', '-'),
    ('رَبِّكَ', 'Tuhanmu', 'ر ب ب', '-', 'Bersambung dhamir ka', 'ka merujuk ke Nabi Muhammad', 'Mudhaf Ilaih', '-', '-'),
    ('بِالْعَشِيِّ', 'Di waktu sore', 'ع ش ي', '-', 'Baa jar + Al-Asyiyyi', '-', 'Jar Majrur', '-', '-'),
    ('وَالْإِبْكَارِ﴾', 'Dan waktu pagi﴾', 'ب ك ر', '-', 'Wawu athaf + Al-Ibkar', '-', 'Ma\'thuf', '-', '-'),
    ('(سُورَةُ', '(Surat', 'س و ر', '-', '-', '-', 'Khabar', '-', '-'),
    ('الْمُؤْمِنِ:', 'Al-Mu\'min (Ghafir):', 'أ م ن', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْآيَة', 'Ayat', 'أ ي ي', '-', '-', '-', 'Badal', '-', '-'),
    ('٥٥).', '55).', '-', '-', '-', '-', '-', '-', '-')
]
blocks_101.append({'type': 'paragraph', 'ar': 'وَعِنْدَمَا بُعِثَ نَبِيُّنَا مُحَمَّدٌ ﷺ كَانَ يُصَلِّي رَكْعَتَيْنِ كُلَّ صَبَاحٍ وَيُصَلِّي رَكْعَتَيْنِ كُلَّ مَسَاءٍ، قِيلَ: وَهُمَا الْمَقْصُودَتَانِ بِقَوْلِ اللهِ تَعَالَى خِطَاباً لِنَبِيِّهِ ﷺ: ﴿وَسَبِّحْ بِحَمْدِ رَبِّكَ بِالْعَشِيِّ وَالْإِبْكَارِ﴾ (سورة المؤمن: الآية ٥٥).', 'id': 'Dan ketika Nabi kita Muhammad SAW diutus, beliau awalnya melaksanakan shalat dua rakaat setiap pagi dan dua rakaat setiap sore. Dikatakan (oleh ulama) bahwa kedua shalat itulah yang dimaksudkan dalam firman Allah Ta\'ala sebagai seruan kepada nabi-Nya SAW: "Dan bertasbihlah (shalatlah) seraya memuji Tuhanmu pada waktu petang dan pagi." (QS. Al-Mu\'min/Ghafir: 55).', 'words': make_words(p2_words)})

# Heading 2
h2_words = [
    ('الصَّلَوَاتُ', 'Shalat-shalat', 'ص ل ي', 'Jamak', '-', '-', 'Mubtada\'', '-', '-'),
    ('الْمَكْتُوبَةُ', 'Yang diwajibkan', 'ك ت ب', '-', '-', '-', 'Na\'at', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_101.append({'type': 'heading', 'ar': 'الصَّلَوَاتُ الْمَكْتُوبَةُ :', 'id': 'Shalat-shalat yang Diwajibkan (Fardhu):', 'words': make_words(h2_words)})

# Para 3
p3_words = [
    ('وَهِيَ', 'Dan dia adalah', '-', '-', 'Wawu + Hiya', 'Hiya merujuk ke Maktubah', 'Mubtada\'', '-', '-'),
    ('الصَّلَوَاتُ', 'Shalat-shalat', 'ص ل ي', '-', '-', '-', 'Khabar', '-', '-'),
    ('الْمَفْرُوضَةُ', 'Yang diwajibkan/difardhukan', 'ف ر ض', '-', '-', '-', 'Na\'at', '-', '-'),
    ('عَلَى', 'Atas/Bagi', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('كُلِّ', 'Setiap', 'ك ل ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('مُسْلِمٍ', 'Muslim', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مُكَلَّفٍ', 'Yang mukallaf (terbebani hukum)', 'ك ل ف', 'Akil Baligh', '-', '-', 'Na\'at', '-', '-'),
    ('وَهِيَ:', 'Yaitu:', '-', '-', 'Wawu + Hiya', '-', 'Mubtada\'', '-', '-'),
    ('الصُّبْحُ', 'Subuh', 'ص ب ح', '-', '-', '-', 'Khabar', '-', '-'),
    ('وَالظُّهْرُ', 'Dan Zhuhur', 'ظ ه ر', '-', 'Wawu + Zhuhur', '-', 'Ma\'thuf', '-', '-'),
    ('وَالْعَصْرُ', 'Dan Ashar', 'ع ص ر', '-', 'Wawu + Ashar', '-', 'Ma\'thuf', '-', '-'),
    ('وَالْمَغْرِبُ', 'Dan Maghrib', 'غ ر ب', '-', 'Wawu + Maghrib', '-', 'Ma\'thuf', '-', '-'),
    ('وَالْعِشَاءُ.', 'Dan Isya.', 'ع ش و', '-', 'Wawu + Isya\'', '-', 'Ma\'thuf', '-', '-'),
    ('شُرِعَتْ', 'Disyariatkan', 'ش ر ع', '-', 'Bersambung ta\' ta\'nits', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Hadzihi as-Shalawat'),
    ('هَذِهِ', 'Ini', '-', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('الصَّلَوَاتُ', 'Shalat-shalat', 'ص ل ي', '-', '-', '-', 'Badal', '-', '-'),
    ('لَيْلَةَ', 'Pada malam', 'ل ي ل', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('أُسْرِيَ', 'Diperjalankannya', 'س ر ي', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mazid', 'Rasulullah'),
    ('بِرَسُولِ', 'Rasul', 'ر س ل', '-', 'Baa jar + Rasul', '-', 'Jar Majrur / Na\'ib Fail', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('إِلَى', 'Ke', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('بَيْتِ', 'Bait', 'ب ي ت', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْمَقْدِسِ', 'Al-Maqdis (Yerusalem)', 'ق د س', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('عُرِجَ', 'Dinaikkannya', 'ع ر ج', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('بِهِ', 'Beliau', '-', '-', 'Baa + hi', 'hi merujuk ke Rasulullah', 'Jar Majrur', '-', '-'),
    ('إِلَى', 'Ke', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('السَّمَاوَاتِ،', 'Langit-langit,', 'س م و', 'Jamak dari Sama\'', '-', '-', 'Majrur', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('فَرَضَ', 'Telah mewajibkan', 'ف ر ض', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('اللهُ', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَلَى', 'Atas', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('نَبِيِّهِ', 'Nabi-Nya', 'ن ب أ', '-', 'Bersambung dhamir hi', 'hi merujuk ke Allah', 'Majrur', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('وَسَائِرِ', 'Dan seluruh', 'س ي ر', '-', 'Wawu + Sair', '-', 'Ma\'thuf', '-', '-'),
    ('الْمُسْلِمِينَ', 'Orang-orang muslim', 'س ل م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('خَمْسِينَ', 'Lima puluh', 'خ م س', '-', '-', '-', 'Maf\'ul Bih 1', '-', '-'),
    ('صَلَاةً', 'Shalat', 'ص ل ي', '-', '-', '-', 'Tamyiz', '-', '-'),
    ('فِي', 'Dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْيَوْمِ', 'Sehari', 'ي و م', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَاللَّيْلَةِ،', 'Dan semalam,', 'ل ي ل', '-', 'Wawu + Lailah', '-', 'Ma\'thuf', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('خَفَّفَهَا', 'Meringankannya', 'خ ف ف', '-', 'Bersambung dhamir ha', 'ha merujuk ke Shalat', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Allah'),
    ('اللهُ', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عَزَّ', 'Maha Perkasa', 'ع ز ز', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('وَجَلَّ', 'Dan Maha Agung', 'ج ل ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('إِلَى', 'Menjadi', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('خَمْسِ', 'Lima', 'خ م س', '-', '-', '-', 'Majrur', '-', '-'),
    ('صَلَوَاتٍ،', 'Waktu shalat,', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَهِيَ', 'Maka ia (shalat itu)', '-', '-', 'Fa + Hiya', 'Hiya merujuk ke Shalat', 'Mubtada\'', '-', '-'),
    ('خَمْسٌ', 'Lima (waktu)', 'خ م س', '-', '-', '-', 'Khabar', '-', '-'),
    ('فِي', 'Dalam (hal)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْأَدَاءِ', 'Penunaian', 'أ د ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَالْفِعْلِ', 'Dan perbuatan', 'ف ع ل', '-', 'Wawu + Fi\'il', '-', 'Ma\'thuf', '-', '-'),
    ('وَخَمْسُونَ', 'Dan lima puluh', 'خ م س', '-', 'Wawu + Khamsun', '-', 'Ma\'thuf', '-', '-'),
    ('فِي', 'Dalam (hal)', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْأَجْرِ.', 'Pahala.', 'أ ج ر', '-', '-', '-', 'Majrur', '-', '-')
]
blocks_101.append({'type': 'paragraph', 'ar': 'وَهِيَ الصَّلَوَاتُ الْمَفْرُوضَةُ عَلَى كُلِّ مُسْلِمٍ مُكَلَّفٍ وَهِيَ: الصُّبْحُ وَالظُّهْرُ وَالْعَصْرُ وَالْمَغْرِبُ وَالْعِشَاءُ. شُرِعَتْ هَذِهِ الصَّلَوَاتُ لَيْلَةَ أُسْرِيَ بِرَسُولِ اللهِ ﷺ إِلَى بَيْتِ الْمَقْدِسِ ثُمَّ عُرِجَ بِهِ إِلَى السَّمَاوَاتِ، فَقَدْ فَرَضَ اللهُ عَلَى نَبِيِّهِ ﷺ وَسَائِرِ الْمُسْلِمِينَ خَمْسِينَ صَلَاةً فِي الْيَوْمِ وَاللَّيْلَةِ، ثُمَّ خَفَّفَهَا اللهُ عَزَّ وَجَلَّ إِلَى خَمْسِ صَلَوَاتٍ، فَهِيَ خَمْسٌ فِي الْأَدَاءِ وَالْفِعْلِ وَخَمْسُونَ فِي الْأَجْرِ.', 'id': 'Yaitu shalat-shalat yang diwajibkan atas setiap muslim yang mukallaf, yaitu: Subuh, Zhuhur, Ashar, Maghrib, dan Isya. Shalat-shalat ini disyariatkan pada malam saat Rasulullah SAW diperjalankan (Isra\') ke Baitul Maqdis lalu dinaikkan (Mi\'raj) ke langit. Awalnya Allah mewajibkan atas Nabi SAW dan seluruh kaum muslimin sebanyak lima puluh kali shalat dalam sehari semalam, lalu Allah Azza wa Jalla meringankannya menjadi lima waktu shalat. Sehingga ia (dihitung) lima kali dalam pelaksanaan dan perbuatan, namun (dihitung) lima puluh kali dalam hal pahala.', 'words': make_words(p3_words)})

# Para 4
p4_words = [
    ('جَاءَ', 'Telah disebutkan', 'ج ي أ', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Khabar (Isi Hadits)'),
    ('فِي', 'Dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('حَدِيثِ', 'Hadits (Kisah)', 'ح د ث', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْإِسْرَاءِ', 'Isra\'', 'س ر ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَالْمِعْرَاجِ', 'Dan Mi\'raj', 'ع ر ج', '-', 'Wawu + Mi\'raj', '-', 'Ma\'thuf', '-', '-'),
    ('الَّذِي', 'Yang', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan oleh', 'ر و ي', '-', 'Bersambung dhamir hu', 'hu merujuk ke Hadits', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Bukhari'),
    ('الْبُخَارِيُّ', 'Al-Bukhari', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٣٤٢)؛', '(342);', '-', '-', '-', '-', '-', '-', '-'),
    ('وَمُسْلِمٌ', 'Dan Muslim', 'س ل م', '-', 'Wawu + Muslim', '-', 'Ma\'thuf', '-', '-'),
    ('(١٦٣)،', '(163),', '-', '-', '-', '-', '-', '-', '-'),
    ('أَنَّ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah/Amil Nawasikh', '-', '-'),
    ('رَسُولَ', 'Rasul', 'ر س ل', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('قَالَ:', 'Beliau bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«فُرِجَ', '«Telah dibuka', 'ف ر ج', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Saqf (Atap)'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('سَقْفِ', 'Atap', 'س ق ف', '-', '-', '-', 'Majrur', '-', '-'),
    ('بَيْتِي', 'Rumahku', 'ب ي ت', '-', 'Bersambung dhamir ya', 'ya merujuk ke Rasulullah', 'Mudhaf Ilaih', '-', '-'),
    ('وَأَنَا', 'Sementara aku (sedang)', '-', '-', 'Wawu Hal + Ana', 'Ana merujuk ke Rasulullah', 'Mubtada\'', '-', '-'),
    ('بِمَكَّةَ،', 'Di Makkah,', 'م ك ك', '-', 'Baa jar + Makkah', '-', 'Jar Majrur / Khabar', '-', '-'),
    ('فَنَزَلَ', 'Maka turunlah', 'ن ز ل', '-', 'Fa athaf + Nazala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Jibril'),
    ('جِبْرِيلُ...', 'Jibril...', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('ثُمَّ', 'Kemudian', '-', '-', '-', '-', 'Huruf Athaf', '-', '-'),
    ('أَخَذَ', 'Ia memegang', 'أ خ ذ', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Jibril'),
    ('بِيَدِي', 'Tanganku', 'ي د ي', '-', 'Baa + Yad + Ya (mutakallim)', 'ya merujuk ke Rasulullah', 'Jar Majrur / Maf\'ul', '-', '-'),
    ('فَعَرَجَ', 'Lalu ia naik', 'ع ر ج', '-', 'Fa athaf + Araja', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Jibril'),
    ('بِي', 'Membawaku', '-', '-', 'Baa + Ya (mutakallim)', 'ya merujuk ke Rasulullah', 'Jar Majrur', '-', '-'),
    ('إِلَى', 'Ke', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('السَّمَاءِ...', 'Langit...', 'س م و', '-', '-', '-', 'Majrur', '-', '-'),
    ('فَفَرَضَ', 'Maka Ia mewajibkan', 'ف ر ض', '-', 'Fa athaf + Faradha', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('اللَّهُ', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-')
]
blocks_101.append({'type': 'paragraph', 'ar': 'جَاءَ فِي حَدِيثِ الْإِسْرَاءِ وَالْمِعْرَاجِ الَّذِي رَوَاهُ الْبُخَارِيُّ (٣٤٢)؛ وَمُسْلِمٌ (١٦٣)، أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «فُرِجَ عَنْ سَقْفِ بَيْتِي وَأَنَا بِمَكَّةَ، فَنَزَلَ جِبْرِيلُ... ثُمَّ أَخَذَ بِيَدِي فَعَرَجَ بِي إِلَى السَّمَاءِ... فَفَرَضَ اللَّهُ', 'id': 'Telah disebutkan dalam hadits tentang Isra\' dan Mi\'raj yang diriwayatkan oleh Al-Bukhari (342); dan Muslim (163), bahwa Rasulullah SAW bersabda: "Atap rumahku dibuka sementara aku sedang berada di Makkah, lalu turunlah Jibril... Kemudian ia menggenggam tanganku lalu membawaku naik ke langit... Maka Allah pun mewajibkan', 'words': make_words(p4_words)})

data.append({
    'pageNumber': 101,
    'blocks': blocks_101
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 101 appended to data.js successfully.')
