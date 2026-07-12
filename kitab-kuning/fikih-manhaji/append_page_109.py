import json

with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['):content.rfind(';')]
data = json.loads(json_str)

blocks_109 = []

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

# Para 1 (Continuation of Adab delaying prayer)
# Text:
# إِخْرَاجِهَا عَنْ وَقْتِهَا، بَلْ رُبَّمَا تَسَبَّبَ عَنْ هَذَا التَّهَاوُنِ تَرْكُهَا، وَإِنَّمَا يُسَنُّ
# تَعْجِيلُ الصَّلَوَاتِ لِأَوَّلِ الْوَقْتِ، وَقَدْ سُئِلَ النَّبِيُّ ﷺ عَنْ أَفْضَلِ الْأَعْمَالِ؟
# فَقَالَ: «الصَّلَاةُ عَلَى وَقْتِهَا»، أَيْ عِنْدَ أَوَّلِ وَقْتِهَا. (رواه البخاري: ٥٠٤؛
# ومسلم: ٨٥).
p1_words = [
    ('إِخْرَاجِهَا', 'Mengeluarkannya', 'خ ر ج', '-', 'Ikhraji + ha', 'ha merujuk ke shalat', 'Majrur / Mashdar', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('وَقْتِهَا،', 'Waktunya,', 'و ق ت', '-', 'Waqti + ha', 'ha merujuk ke shalat', 'Majrur', '-', '-'),
    ('بَلْ', 'Bahkan', '-', '-', '-', '-', 'Huruf Athaf (Idhrab)', '-', '-'),
    ('رُبَّمَا', 'Bisa jadi', '-', '-', '-', '-', 'Huruf Jarr Syabih biz Zaid', '-', '-'),
    ('تَسَبَّبَ', 'Menyebabkan', 'س ب ب', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mazid', 'Hadzad Tahawun'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('هَذَا', 'Sikap (ini)', '-', '-', '-', '-', 'Isim Isyarah / Majrur', '-', '-'),
    ('التَّهَاوُنِ', 'Kelalaian/meremehkan', 'ه و ن', '-', '-', '-', 'Badal', '-', '-'),
    ('تَرْكُهَا،', 'Meninggalkannya sama sekali,', 'ت ر ك', '-', 'Tarku + ha', 'ha merujuk ke shalat', 'Fa\'il', '-', '-'),
    ('وَإِنَّمَا', 'Dan hanyasanya', '-', '-', 'Wawu + Inna + Ma kaffah', '-', 'Adat Hashr', '-', '-'),
    ('يُسَنُّ', 'Disunnahkan (dianjurkan)', 'س ن ن', '-', '-', '-', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mujarrad', 'Ta\'jil'),
    ('تَعْجِيلُ', 'Menyegerakan', 'ع ج ل', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('الصَّلَوَاتِ', 'Pelaksanaan shalat-shalat', 'ص ل ي', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('لِأَوَّلِ', 'Pada awal', 'أ و ل', '-', 'Lam jar + Awwal', '-', 'Jar Majrur', '-', '-'),
    ('الْوَقْتِ،', 'Waktunya,', 'و ق ت', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَقَدْ', 'Dan sungguh', '-', '-', 'Wawu + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('سُئِلَ', 'Pernah ditanya', 'س أ ل', '-', '-', '-', 'Fi\'il Madhi Majhul', 'Tsulasi Mujarrad', 'Nabi'),
    ('النَّبِيُّ', 'Nabi', 'ن ب أ', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Tentang', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَفْضَلِ', 'Seutama-utama', 'ف ض ل', '-', '-', '-', 'Majrur', '-', '-'),
    ('الْأَعْمَالِ؟', 'Amalan?', 'ع م ل', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('فَقَالَ:', 'Maka beliau menjawab:', 'ق و ل', '-', 'Fa + Qala', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Nabi'),
    ('«الصَّلَاةُ', '«Shalat', 'ص ل ي', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('عَلَى', 'Pada', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('وَقْتِهَا»،', 'Waktunya»,', 'و ق ت', '-', 'Waqti + ha', 'ha merujuk ke shalat', 'Jar Majrur / Khabar', '-', '-'),
    ('أَيْ', 'Yaitu', '-', '-', '-', '-', 'Huruf Tafsir', '-', '-'),
    ('عِنْدَ', 'Pada (di)', 'ع ن د', '-', '-', '-', 'Zharf', '-', '-'),
    ('أَوَّلِ', 'Awal', 'أ و ل', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَقْتِهَا.', 'Waktunya.', 'و ق ت', '-', 'Waqti + ha', 'ha merujuk ke shalat', 'Mudhaf Ilaih', '-', '-'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('البخاري:', 'Al-Bukhari:', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٥٠٤؛', '504;', '-', '-', '-', '-', '-', '-', '-'),
    ('ومسلم:', 'Dan Muslim:', 'س ل م', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('٨٥).', '85).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'يُسَنُّ' (11), 'الْأَعْمَالِ؟' (22), '٥٠٤؛' (33)
blocks_109.append({
    'type': 'paragraph',
    'ar': 'إِخْرَاجِهَا عَنْ وَقْتِهَا، بَلْ رُبَّمَا تَسَبَّبَ عَنْ هَذَا التَّهَاوُنِ تَرْكُهَا، وَإِنَّمَا يُسَنُّ تَعْجِيلُ الصَّلَوَاتِ لِأَوَّلِ الْوَقْتِ، وَقَدْ سُئِلَ النَّبِيُّ ﷺ عَنْ أَفْضَلِ الْأَعْمَالِ؟ فَقَالَ: «الصَّلَاةُ عَلَى وَقْتِهَا»، أَيْ عِنْدَ أَوَّلِ وَقْتِهَا. (رواه البخاري: ٥٠٤؛ ومسلم: ٨٥).',
    'id': 'mengeluarkannya (terlewat) dari waktunya, bahkan bisa jadi sifat kelalaian semacam ini berujung pada peninggalan shalat secara total. Dan justru yang amat dianjurkan (disunnahkan) adalah menyegerakan pelaksanaan shalat-shalat di awal waktu pelaksanaannya. Sungguh Nabi SAW pernah ditanya tentang amalan apa yang paling utama? Beliau pun menjawab: "Shalat tepat pada waktunya", maksudnya adalah pada awal waktunya. (HR. Al-Bukhari: 504; dan Muslim: 85).',
    'words': make_words(p1_words, [11, 22, 33])
})

# Para 2 (Shalat sebagian di dalam waktu, sebagian di luar)
# Text:
# وَاعْلَمْ أَنَّ مَنْ وَقَعَ بَعْضُ صَلَاتِهِ فِي الْوَقْتِ، وَبَعْضُهَا خَارِجَهُ: فَإِنَّهُ
# إِنْ وَقَعَ رَكْعَةٌ فِي الْوَقْتِ كَانَتِ الصَّلَاةُ أَدَاءً، وَإِلَّا كَانَتْ قَضَاءً؛ وَدَلِيلُ ذَلِكَ
# مَا رَوَاهُ الْبُخَارِيُّ (٥٥٤)؛ وَمُسْلِمٌ (٦٠٨)، عَنْ أَبِي هُرَيْرَةَ رضي الله
# عنه: أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «مَنْ أَدْرَكَ مِنَ الصُّبْحِ رَكْعَةً قَبْلَ أَنْ تَطْلُعَ
# الشَّمْسُ فَقَدْ أَدْرَكَ الصُّبْحَ، وَمَنْ أَدْرَكَ رَكْعَةً مِنَ الْعَصْرِ قَبْلَ أَنْ تَغْرُبَ
# الشَّمْسُ فَقَدْ أَدْرَكَ الْعَصْرَ». وَقَوْلُهُ ﷺ : «مَنْ أَدْرَكَ رَكْعَةً مِنَ الصَّلَاةِ فَقَدْ
# أَدْرَكَ الصَّلَاةَ» (رواه البخاري: ٥٥٥؛ ومسلم: ٦٠٧).
p2_words = [
    ('وَاعْلَمْ', 'Dan ketahuilah', 'ع ل م', '-', 'Wawu + I\'lam', '-', 'Fi\'il Amr', 'Tsulasi Mujarrad', 'Engkau (Anta)'),
    ('أَنَّ', 'Bahwa', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('مَنْ', 'Barangsiapa yang', '-', '-', '-', '-', 'Isim Syarat', '-', '-'),
    ('وَقَعَ', 'Jatuh (terlaksana)', 'و ق ع', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Ba\'dhu'),
    ('بَعْضُ', 'Sebagian', 'ب ع ض', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('صَلَاتِهِ', 'Dari shalatnya', 'ص ل ي', '-', 'Shalati + hi', 'hi merujuk ke man (seseorang)', 'Mudhaf Ilaih', '-', '-'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْوَقْتِ،', 'Waktunya,', 'و ق ت', '-', '-', '-', 'Majrur', '-', '-'),
    ('وَبَعْضُهَا', 'Sedangkan sebagian (rakaat) lainnya', 'ب ع ض', '-', 'Wawu + Ba\'dhu + ha', 'ha merujuk ke shalat', 'Ma\'thuf', '-', '-'),
    ('خَارِجَهُ:', 'Di luarnya (keluar waktu):', 'خ ر ج', '-', 'Kharija + hu', 'hu merujuk ke waktu', 'Zharf Makan', '-', '-'),
    ('فَإِنَّهُ', 'Maka sesungguhnya', '-', '-', 'Fa (Jawab) + Inna + hu', 'hu dhamir sya\'n', 'Amil Nawasikh', '-', '-'),
    ('إِنْ', 'Jika', '-', '-', '-', '-', 'Huruf Syarat', '-', '-'),
    ('وَقَعَ', 'Sempat terlaksana', 'و ق ع', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mujarrad', 'Rak\'atun'),
    ('رَكْعَةٌ', 'Satu rakaat (penuh)', 'ر ك ع', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْوَقْتِ', 'Waktu tersebut', 'و ق ت', '-', '-', '-', 'Majrur', '-', '-'),
    ('كَانَتِ', 'Maka shalat itu berstatus', 'ك و ن', '-', 'Kanat + Ta\' ta\'nits', '-', 'Fi\'il Madhi Naqish (Jawab Syarat)', 'Tsulasi Mujarrad', 'Asy-Shalatu'),
    ('الصَّلَاةُ', 'Shalat tersebut', 'ص ل ي', '-', '-', '-', 'Isim Kanat', '-', '-'),
    ('أَدَاءً،', 'Ada\' (tepat waktu),', 'أ د ي', '-', '-', '-', 'Khabar Kanat', '-', '-'),
    ('وَإِلَّا', 'Dan jika tidak (kurang dari 1 rakaat)', '-', '-', 'Wawu + In + Laa', '-', 'Huruf Syarat & Nafi', '-', '-'),
    ('كَانَتْ', 'Maka ia berstatus', 'ك و ن', '-', 'Kanat + Ta\' ta\'nits', '-', 'Fi\'il Madhi Naqish (Jawab Syarat)', 'Tsulasi Mujarrad', 'Asy-Shalatu'),
    ('قَضَاءً؛', 'Qadha (mengganti/terlewat);', 'ق ض ي', '-', '-', '-', 'Khabar Kanat', '-', '-'),
    ('وَدَلِيلُ', 'Adapun dalilnya', 'د ل ل', '-', 'Wawu + Dalilu', '-', 'Mubtada\'', '-', '-'),
    ('ذَلِكَ', 'Atas hal tersebut', 'ذ ل ك', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَا', 'Adalah apa yang', '-', '-', '-', '-', 'Khabar (Isim Maushul)', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan', 'ر و ي', '-', 'Rawa + hu', 'hu merujuk ke hadits', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Al-Bukhari'),
    ('الْبُخَارِيُّ', 'Oleh Al-Bukhari', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٥٥٤)؛', '(554);', '-', '-', '-', '-', '-', '-', '-'),
    ('وَمُسْلِمٌ', 'Dan Muslim', 'س ل م', '-', 'Wawu + Muslimun', '-', 'Ma\'thuf', '-', '-'),
    ('(٦٠٨)،', '(608),', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('أَبِي', 'Abu', 'أ ب و', '-', '-', '-', 'Majrur', '-', '-'),
    ('هُرَيْرَةَ', 'Hurairah', 'ه ر ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه:', 'Atasnya:', '-', '-', 'An + hu', 'hu merujuk ke Abu Hurairah', 'Jar Majrur', '-', '-'),
    ('أَنَّ', 'Bahwa sesungguhnya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('رَسُولَ', 'Rasul', 'ر س ل', '-', '-', '-', 'Isim Anna', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('قَالَ:', 'Telah bersabda:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi (Khabar Anna)', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('«مَنْ', '«Barangsiapa yang', '-', '-', '-', '-', 'Isim Syarat / Mubtada\'', '-', '-'),
    ('أَدْرَكَ', 'Mendapati', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mazid', 'Man'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الصُّبْحِ', 'Shalat shubuh', 'ص ب ح', '-', '-', '-', 'Majrur', '-', '-'),
    ('رَكْعَةً', 'Satu rakaat', 'ر ك ع', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('قَبْلَ', 'Sebelum', 'ق ب ل', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('تَطْلُعَ', 'Akan terbit', 'ط ل ع', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Syams'),
    ('الشَّمْسُ', 'Matahari', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('أَدْرَكَ', 'Ia telah mendapati', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mazid', 'Man'),
    ('الصُّبْحَ،', 'Shubuh seutuhnya,', 'ص ب ح', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('وَمَنْ', 'Dan barangsiapa yang', '-', '-', 'Wawu + Man', '-', 'Isim Syarat', '-', '-'),
    ('أَدْرَكَ', 'Mendapati', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mazid', 'Man'),
    ('رَكْعَةً', 'Satu rakaat', 'ر ك ع', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الْعَصْرِ', 'Shalat ashar', 'ع ص ر', '-', '-', '-', 'Majrur', '-', '-'),
    ('قَبْلَ', 'Sebelum', 'ق ب ل', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('تَغْرُبَ', 'Akan terbenam', 'غ ر ب', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Syams'),
    ('الشَّمْسُ', 'Matahari', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('أَدْرَكَ', 'Ia telah mendapati', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mazid', 'Man'),
    ('الْعَصْرَ».', 'Ashar seutuhnya».', 'ع ص ر', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('وَقَوْلُهُ', 'Dan sabda beliau', 'ق و ل', '-', 'Wawu + Qaulu + hu', 'hu merujuk ke Nabi', 'Ma\'thuf', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-'),
    ('«مَنْ', '«Barangsiapa yang', '-', '-', '-', '-', 'Isim Syarat', '-', '-'),
    ('أَدْرَكَ', 'Mendapati', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Syarat)', 'Tsulasi Mazid', 'Man'),
    ('رَكْعَةً', 'Satu rakaat', 'ر ك ع', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('مِنَ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('الصَّلَاةِ', 'Suatu shalat', 'ص ل ي', '-', '-', '-', 'Majrur', '-', '-'),
    ('فَقَدْ', 'Maka sungguh', '-', '-', 'Fa + Qad', '-', 'Huruf Tahqiq', '-', '-'),
    ('أَدْرَكَ', 'Ia telah mendapati', 'د ر ك', '-', '-', '-', 'Fi\'il Madhi (Jawab Syarat)', 'Tsulasi Mazid', 'Man'),
    ('الصَّلَاةَ»', 'Shalat tersebut seutuhnya»', 'ص ل ي', '-', '-', '-', 'Maf\'ul Bih', '-', '-'),
    ('(رواه', '(Diriwayatkan oleh', 'ر و ي', '-', '-', '-', 'Fi\'il Madhi', '-', '-'),
    ('البخاري:', 'Al-Bukhari:', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('٥٥٥؛', '555;', '-', '-', '-', '-', '-', '-', '-'),
    ('ومسلم:', 'Dan Muslim:', 'س ل م', '-', '-', '-', 'Ma\'thuf', '-', '-'),
    ('٦٠٧).', '607).', '-', '-', '-', '-', '-', '-', '-')
]
# Breaks: 'فَإِنَّهُ' (10), 'ذَلِكَ' (24), 'الله' (34), 'تَطْلُعَ' (49), 'تَغْرُبَ' (59), 'فَقَدْ' (74), '٦٠٧).' (82)
blocks_109.append({
    'type': 'paragraph',
    'ar': 'وَاعْلَمْ أَنَّ مَنْ وَقَعَ بَعْضُ صَلَاتِهِ فِي الْوَقْتِ، وَبَعْضُهَا خَارِجَهُ: فَإِنَّهُ إِنْ وَقَعَ رَكْعَةٌ فِي الْوَقْتِ كَانَتِ الصَّلَاةُ أَدَاءً، وَإِلَّا كَانَتْ قَضَاءً؛ وَدَلِيلُ ذَلِكَ مَا رَوَاهُ الْبُخَارِيُّ (٥٥٤)؛ وَمُسْلِمٌ (٦٠٨)، عَنْ أَبِي هُرَيْرَةَ رضي الله عنه: أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «مَنْ أَدْرَكَ مِنَ الصُّبْحِ رَكْعَةً قَبْلَ أَنْ تَطْلُعَ الشَّمْسُ فَقَدْ أَدْرَكَ الصُّبْحَ، وَمَنْ أَدْرَكَ رَكْعَةً مِنَ الْعَصْرِ قَبْلَ أَنْ تَغْرُبَ الشَّمْسُ فَقَدْ أَدْرَكَ الْعَصْرَ». وَقَوْلُهُ ﷺ : «مَنْ أَدْرَكَ رَكْعَةً مِنَ الصَّلَاةِ فَقَدْ أَدْرَكَ الصَّلَاةَ» (رواه البخاري: ٥٥٥؛ ومسلم: ٦٠٧).',
    'id': 'Ketahuilah, bahwasanya barangsiapa yang pelaksanaan sebagian shalatnya jatuh di dalam waktu, dan sebagian sisanya terlaksana di luar waktu (karena terlambat); maka kaidahnya adalah: Jika ia masih mendapati satu rakaat penuh (sebelum waktu habis), maka shalatnya tersebut berstatus Ada\' (tepat waktu). Dan apabila kurang dari 1 rakaat, maka statusnya adalah Qadha (terlewat). Adapun dalilnya adalah hadits riwayat Bukhari (554) dan Muslim (608), dari Abu Hurairah RA: Bahwasanya Rasulullah SAW bersabda: "Barangsiapa yang mendapati dari shalat Shubuh satu rakaat sebelum terbitnya matahari, maka sungguh ia telah mendapati shalat Shubuh tersebut, dan barangsiapa mendapati satu rakaat dari shalat Ashar sebelum matahari terbenam, maka sungguh ia telah mendapati shalat Ashar tersebut". Dan juga sabda beliau SAW: "Barangsiapa yang mendapati satu rakaat dari shalat apapun, maka sungguh ia telah mendapati shalat tersebut (Ada\')" (HR. Bukhari: 555; Muslim: 607).',
    'words': make_words(p2_words, [10, 24, 34, 49, 59, 74, 82])
})


# Heading 1: الْأَوْقَاتُ الَّتِي تُكْرَهُ فِيهَا الصَّلَاةُ :
h1_words = [
    ('الْأَوْقَاتُ', 'Waktu-waktu', 'و ق ت', 'Jamak', '-', '-', 'Mubtada\'', '-', '-'),
    ('الَّتِي', 'Yang mana', '-', '-', '-', '-', 'Na\'at / Isim Maushul', '-', '-'),
    ('تُكْرَهُ', 'Dimakruhkan (dilarang)', 'ك ر ه', '-', '-', '-', 'Fi\'il Mudhari\' Majhul (Shilah)', 'Tsulasi Mujarrad', 'Asy-Shalatu'),
    ('فِيهَا', 'Di dalamnya', '-', '-', 'Fii + ha', 'ha merujuk ke awqat', 'Jar Majrur', '-', '-'),
    ('الصَّلَاةُ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_109.append({'type': 'heading', 'ar': 'الْأَوْقَاتُ الَّتِي تُكْرَهُ فِيهَا الصَّلَاةُ :', 'id': 'Waktu-Waktu Yang Dimakruhkan/Dilarang Mengerjakan Shalat Padanya:', 'words': make_words(h1_words, [])})

# Sub Heading: تُكْرَهُ الصَّلَاةُ كَرَاهَةَ تَحْرِيمٍ :
h2_words = [
    ('تُكْرَهُ', 'Dimakruhkan (Dilarang)', 'ك ر ه', '-', '-', '-', 'Fi\'il Mudhari\' Majhul', 'Tsulasi Mujarrad', 'Asy-Shalatu'),
    ('الصَّلَاةُ', 'Shalat', 'ص ل ي', '-', '-', '-', 'Na\'ib Fa\'il', '-', '-'),
    ('كَرَاهَةَ', 'Dengan kemakruhan', 'ك ر ه', '-', '-', '-', 'Maf\'ul Muthlaq', '-', '-'),
    ('تَحْرِيمٍ', 'Tahrīm (diharamkan/dilarang keras)', 'ح ر م', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    (':', ':', '-', '-', '-', '-', '-', '-', '-')
]
blocks_109.append({'type': 'heading', 'ar': 'تُكْرَهُ الصَّلَاةُ كَرَاهَةَ تَحْرِيمٍ :', 'id': 'Pelaksanaan Shalat dilarang dengan jenis Karahah Tahrim (Haram/Dilarang keras) pada:', 'words': make_words(h2_words, [])})

# List Item 1:
# ١ - عِنْدَ الِاسْتِوَاءِ إِلَّا يَوْمَ الْجُمُعَةِ، وَبَعْدَ صَلَاةِ الصُّبْحِ حَتَّى
# تَرْتَفِعَ الشَّمْسُ كَرُمْحٍ فِي النَّظَرِ.
l1_words = [
    ('١', '1', '-', '-', '-', '-', '-', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('عِنْدَ', 'Pada waktu', 'ع ن د', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('الِاسْتِوَاءِ', 'Matahari persis di tengah', 'س و ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('إِلَّا', 'Terkecuali', '-', '-', '-', '-', 'Adat Istitsna\'', '-', '-'),
    ('يَوْمَ', 'Pada hari', 'ي و م', '-', '-', '-', 'Zharf Zaman / Mustatsna', '-', '-'),
    ('الْجُمُعَةِ،', 'Jum\'at,', 'ج م ع', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('وَبَعْدَ', 'Dan sesudah', 'ب ع د', '-', 'Wawu + Ba\'da', '-', 'Ma\'thuf', '-', '-'),
    ('صَلَاةِ', 'Pelaksanaan shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الصُّبْحِ', 'Shubuh', 'ص ب ح', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar / Ghayah', '-', '-'),
    ('تَرْتَفِعَ', 'Meningginya', 'ر ف ع', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mazid', 'Asy-Syamsu'),
    ('الشَّمْسُ', 'Matahari', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('كَرُمْحٍ', 'Sekadar satu ukuran tombak', 'ر م ح', '-', 'Kaf jar + Rumh', '-', 'Jar Majrur / Hal', '-', '-'),
    ('فِي', 'Di dalam', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('النَّظَرِ.', 'Pandangan (mata).', 'ن ظ ر', '-', '-', '-', 'Majrur', '-', '-')
]
# Breaks: 'حَتَّى' (10)
blocks_109.append({
    'type': 'paragraph',
    'ar': '١ - عِنْدَ الِاسْتِوَاءِ إِلَّا يَوْمَ الْجُمُعَةِ، وَبَعْدَ صَلَاةِ الصُّبْحِ حَتَّى تَرْتَفِعَ الشَّمْسُ كَرُمْحٍ فِي النَّظَرِ.',
    'id': '1 - Saat waktu istiwa\' (matahari tepat di puncak langit sebelum tergelincir), terkecuali pada hari Jumat. Serta dilarang juga sesudah pelaksanaan shalat Shubuh hingga matahari terbit meninggi seukuran satu batang tombak dalam pandangan mata telanjang.',
    'words': make_words(l1_words, [10])
})


# List Item 2:
# ٢ - وَبَعْدَ صَلَاةِ الْعَصْرِ حَتَّى تَغْرُبَ الشَّمْسُ.
l2_words = [
    ('٢', '2', '-', '-', '-', '-', '-', '-', '-'),
    ('-', '-', '-', '-', '-', '-', '-', '-', '-'),
    ('وَبَعْدَ', 'Dan setelah', 'ب ع د', '-', 'Wawu + Ba\'da', '-', 'Zharf Zaman / Ma\'thuf', '-', '-'),
    ('صَلَاةِ', 'Pelaksanaan shalat', 'ص ل ي', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('الْعَصْرِ', 'Ashar', 'ع ص ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar / Ghayah', '-', '-'),
    ('تَغْرُبَ', 'Terbenam', 'غ ر ب', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Syams'),
    ('الشَّمْسُ.', 'Matahari.', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-')
]
blocks_109.append({
    'type': 'paragraph',
    'ar': '٢ - وَبَعْدَ صَلَاةِ الْعَصْرِ حَتَّى تَغْرُبَ الشَّمْسُ.',
    'id': '2 - Dan sesudah pelaksanaan shalat Ashar hingga matahari benar-benar terbenam di ufuk barat.',
    'words': make_words(l2_words, [])
})


# Para 3 (Dalil for Karahah)
# وَدَلِيلُ ذَلِكَ مَا رَوَاهُ مُسْلِمٌ (٨٣١) عَنْ عُقْبَةَ بْنِ عَامِرٍ رضي الله عنه
# قَالَ: ثَلَاثُ سَاعَاتٍ كَانَ رَسُولُ اللهِ ﷺ يَنْهَانَا أَنْ نُصَلِّيَ فِيهِنَّ، وَأَنْ نَقْبُرَ
# مَوْتَانَا: حِينَ تَطْلُعُ الشَّمْسُ بَازِغَةً حَتَّى تَرْتَفِعَ، وَحِينَ يَقُومُ قَائِمُ الظَّهِيرَةِ
# حَتَّى تَمِيلَ الشَّمْسُ، وَحِينَ تَضَيَّفُ الشَّمْسُ لِلْغُرُوبِ حَتَّى تَغْرُبَ.
p3_words = [
    ('وَدَلِيلُ', 'Dan adapun dalilnya', 'د ل ل', '-', 'Wawu + Dalilu', '-', 'Mubtada\'', '-', '-'),
    ('ذَلِكَ', 'Terkait hal tersebut', 'ذ ل ك', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('مَا', 'Adalah apa yang', '-', '-', '-', '-', 'Khabar (Isim Maushul)', '-', '-'),
    ('رَوَاهُ', 'Diriwayatkan', 'ر و ي', '-', 'Rawa + hu', 'hu merujuk ke hadits', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Muslim'),
    ('مُسْلِمٌ', 'Oleh Muslim', 'س ل م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('(٨٣١)', '(831)', '-', '-', '-', '-', '-', '-', '-'),
    ('عَنْ', 'Dari', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('عُقْبَةَ', 'Uqbah', 'ع ق ب', '-', '-', '-', 'Majrur', '-', '-'),
    ('بْنِ', 'Bin (Putra)', 'ب ن ي', '-', '-', '-', 'Na\'at / Badal', '-', '-'),
    ('عَامِرٍ', 'Amir', 'ع م ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('رضي', 'Telah meridhai', 'ر ض ي', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Allah'),
    ('الله', 'Allah', '-', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('عنه', 'Atasnya', '-', '-', 'An + hu', 'hu merujuk ke Uqbah', 'Jar Majrur', '-', '-'),
    ('قَالَ:', 'Ia berkata:', 'ق و ل', '-', '-', '-', 'Fi\'il Madhi', 'Tsulasi Mujarrad', 'Uqbah'),
    ('ثَلَاثُ', 'Tiga', 'ث ل ث', '-', '-', '-', 'Zharf Zaman', '-', '-'),
    ('سَاعَاتٍ', 'Waktu/masa', 'س و ع', 'Jamak', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('كَانَ', 'Pernah', 'ك و ن', '-', '-', '-', 'Fi\'il Madhi Naqish', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('رَسُولُ', 'Rasul', 'ر س ل', '-', '-', '-', 'Isim Kana', '-', '-'),
    ('اللهِ', 'Allah', '-', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('ﷺ', 'SAW', '-', '-', '-', '-', '-', '-', '-'),
    ('يَنْهَانَا', 'Melarang kami', 'ن ه ي', '-', 'Yanha + na', 'na merujuk ke sahabat', 'Fi\'il Mudhari\' (Khabar Kana)', 'Tsulasi Mujarrad', 'Rasulullah'),
    ('أَنْ', 'Bahwa', '-', '-', '-', '-', 'Huruf Mashdariyyah', '-', '-'),
    ('نُصَلِّيَ', 'Mengerjakan shalat', 'ص ل ي', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mazid', 'Kami (Nahnu)'),
    ('فِيهِنَّ،', 'Di dalamnya,', '-', '-', 'Fii + hinna', 'hinna merujuk ke tiga waktu', 'Jar Majrur', '-', '-'),
    ('وَأَنْ', 'Dan (melarang) bahwa', '-', '-', 'Wawu + An', '-', 'Ma\'thuf', '-', '-'),
    ('نَقْبُرَ', 'Kami menguburkan', 'ق ب ر', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Kami (Nahnu)'),
    ('مَوْتَانَا:', 'Orang yang mati di antara kami:', 'م و ت', 'Jamak', 'Mauta + na', 'na merujuk ke sahabat', 'Maf\'ul Bih', '-', '-'),
    ('حِينَ', 'Yaitu ketika', 'ح ي ن', '-', '-', '-', 'Zharf Zaman / Badal', '-', '-'),
    ('تَطْلُعُ', 'Mulai terbit', 'ط ل ع', '-', '-', '-', 'Fi\'il Mudhari\' (Mudhaf Ilaih)', 'Tsulasi Mujarrad', 'Syams'),
    ('الشَّمْسُ', 'Matahari', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('بَازِغَةً', 'Nampak memancar cahayanya', 'ب ز غ', '-', '-', '-', 'Hal', '-', '-'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('تَرْتَفِعَ،', 'Ia meninggi,', 'ر ف ع', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mazid', 'Syams'),
    ('وَحِينَ', 'Dan ketika', 'ح ي ن', '-', 'Wawu + Hina', '-', 'Ma\'thuf', '-', '-'),
    ('يَقُومُ', 'Berdirinya/berhentinya', 'ق و م', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mujarrad', 'Qaim (penunggang)'),
    ('قَائِمُ', 'Orang yang memancangkan diri (unta karena kepanasan)', 'ق و م', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('الظَّهِيرَةِ', 'Di tengah hari yang panas (Istiwa\')', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('تَمِيلَ', 'Matahari tergelincir', 'م ي ل', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Syams'),
    ('الشَّمْسُ،', 'Matahari,', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('وَحِينَ', 'Dan ketika', 'ح ي ن', '-', 'Wawu + Hina', '-', 'Ma\'thuf', '-', '-'),
    ('تَضَيَّفُ', 'Telah condong', 'ض ي ف', '-', '-', '-', 'Fi\'il Mudhari\'', 'Tsulasi Mazid', 'Syams'),
    ('الشَّمْسُ', 'Matahari', 'ش م س', '-', '-', '-', 'Fa\'il', '-', '-'),
    ('لِلْغُرُوبِ', 'Menuju arah terbenamnya', 'غ ر ب', '-', 'Lam jar + Ghurub', '-', 'Jar Majrur', '-', '-'),
    ('حَتَّى', 'Hingga', '-', '-', '-', '-', 'Huruf Jar', '-', '-'),
    ('تَغْرُبَ.', 'Terbenam sempurna.', 'غ ر ب', '-', '-', '-', 'Fi\'il Mudhari\' Manshub', 'Tsulasi Mujarrad', 'Syams')
]
# Breaks: 'عنه' (12), 'نَقْبُرَ' (25), 'الظَّهِيرَةِ' (36), 'تَغْرُبَ.' (45)
blocks_109.append({
    'type': 'paragraph',
    'ar': 'وَدَلِيلُ ذَلِكَ مَا رَوَاهُ مُسْلِمٌ (٨٣١) عَنْ عُقْبَةَ بْنِ عَامِرٍ رضي الله عنه قَالَ: ثَلَاثُ سَاعَاتٍ كَانَ رَسُولُ اللهِ ﷺ يَنْهَانَا أَنْ نُصَلِّيَ فِيهِنَّ، وَأَنْ نَقْبُرَ مَوْتَانَا: حِينَ تَطْلُعُ الشَّمْسُ بَازِغَةً حَتَّى تَرْتَفِعَ، وَحِينَ يَقُومُ قَائِمُ الظَّهِيرَةِ حَتَّى تَمِيلَ الشَّمْسُ، وَحِينَ تَضَيَّفُ الشَّمْسُ لِلْغُرُوبِ حَتَّى تَغْرُبَ.',
    'id': 'Adapun dalilnya adalah hadits yang diriwayatkan oleh Muslim (831) dari Uqbah bin Amir RA, ia berkata: "Ada tiga waktu (masa) di mana Rasulullah SAW melarang kami mengerjakan shalat sunnah padanya, dan melarang kami menguburkan jenazah orang yang mati di antara kami: (1) Saat matahari terbit menampakkan diri hingga ia meninggi sempurna, (2) saat persis di tengah hari yang menyengat (waktu unta berhenti melangkah) sampai matahari tergelincir ke barat, dan (3) saat matahari sangat condong ke ufuk barat untuk terbenam hingga benar-benar tenggelam."',
    'words': make_words(p3_words, [12, 25, 36, 45])
})

# Para 4 (Glossary Bazighah)
# [بَازِغَةً: الْمُرَادُ أَوَّلُ ظُهُورِ قُرْصِهَا. وَقَائِمُ الظَّهِيرَةِ: أَصْلُهُ أَنَّ الْبَعِيرَ
p4_words = [
    ('[بَازِغَةً:', '[Bazighah:', 'ب ز غ', '-', '-', '-', 'Mubtada\'', '-', '-'),
    ('الْمُرَادُ', 'Maksudnya adalah', 'ر و د', '-', '-', '-', 'Mubtada\' Tsani', '-', '-'),
    ('أَوَّلُ', 'Permulaan', 'أ و ل', '-', '-', '-', 'Khabar (dari murad)', '-', '-'),
    ('ظُهُورِ', 'Munculnya', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('قُرْصِهَا.', 'Piringan mataharinya.', 'ق ر ص', '-', 'Qurshi + ha', 'ha merujuk ke Syams', 'Mudhaf Ilaih', '-', '-'),
    ('وَقَائِمُ', 'Sedangkan Qaim', 'ق و م', '-', 'Wawu + Qaimu', '-', 'Mubtada\'', '-', '-'),
    ('الظَّهِيرَةِ:', 'Adz-Dhahirah:', 'ظ ه ر', '-', '-', '-', 'Mudhaf Ilaih', '-', '-'),
    ('أَصْلُهُ', 'Asal usul (kata)-nya adalah', 'أ ص ل', '-', 'Ashlu + hu', 'hu merujuk ke qaimu dzahirah', 'Khabar / Mubtada\' Tsani', '-', '-'),
    ('أَنَّ', 'Bahwasanya', '-', '-', '-', '-', 'Amil Nawasikh', '-', '-'),
    ('الْبَعِيرَ', 'Unta jantan', 'ب ع ر', '-', '-', '-', 'Isim Anna', '-', '-')
]
# Breaks: 'الْبَعِيرَ' (9)
blocks_109.append({
    'type': 'paragraph',
    'ar': '[بَازِغَةً: الْمُرَادُ أَوَّلُ ظُهُورِ قُرْصِهَا. وَقَائِمُ الظَّهِيرَةِ: أَصْلُهُ أَنَّ الْبَعِيرَ',
    'id': '[Penjelasan Kosakata: "Bazighah": yang dimaksud adalah awal mula tampaknya piringan matahari. "Qaimu Adz-Dhahirah": asal usul kata ini digunakan tatkala mendeskripsikan unta...',
    'words': make_words(p4_words, [9])
})


data.append({
    'pageNumber': 109,
    'blocks': blocks_109
})

js_content = 'const fikihData = ' + json.dumps(data, ensure_ascii=False, indent=4) + ';\n'
with open('D:/Project/ahmdd-zulfikar.github.io/kitab-kuning/fikih-manhaji/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print('Page 109 appended to data.js successfully.')
