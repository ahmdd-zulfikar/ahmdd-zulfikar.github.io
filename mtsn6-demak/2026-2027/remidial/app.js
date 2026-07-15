const GAS_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbyGlGepwK3HRIRc4mjPrEKeVcvq7dDHt8IsR2zoSwiqEogw0rFj4-rmugUFMPMK30x3eQ/exec";

let db;
let classData = null;
let activeStudent = null;
let wrongQuestions = [];

const soalBank = [
    {
        id: 1, type: "PG",
        text: `Sebuah penggaris plastik dijepitkan pada ujung meja. Bagian ujung penggaris yang bebas ditekuk lalu dilepaskan sehingga bergerak naik-turun beberapa kali sebelum berhenti. Gerakan naik-turun penggaris tersebut menunjukkan adanya getaran. Pernyataan mana yang paling tepat menjelaskan mengapa gerakan tersebut termasuk getaran?`,
        options: [
            "A. Karena penggaris mengalami perpindahan tempat dari satu titik ke titik lain.",
            "B. Karena penggaris bergerak monoton ke satu arah hingga berhenti.",
            "C. Karena penggaris bergerak bolak-balik melalui titik setimbang secara periodik.",
            "D. Karena penggaris berubah bentuk akibat adanya gaya dari luar."
        ]
    },
    {
        id: 2, type: "PG",
        text: `Perhatikan gambar berikut!<br><br>Sebuah bandul bergerak bolak-balik dengan lintasan berawal dari A. Waktu yang diperlukan bandul tersebut untuk melakukan satu kali getaran adalah 4 detik. Periode dan frekuensi getaran bandul tersebut secara berturut-turut adalah...`,
        options: [
            "A. 4 s dan 0,25 Hz",
            "B. 4 s dan 1 Hz",
            "C. 1 s dan 0,25 Hz",
            "D. 2 s dan 1 Hz"
        ]
    },
    {
        id: 3, type: "PG",
        text: `Sebuah kapal peneliti menggunakan sonar untuk mengukur kedalaman laut. Sonar memancarkan bunyi ke dasar laut dan sinyal pantulan diterima kembali setelah 4 sekon. Jika cepat rambat bunyi di dalam air laut adalah 1.500 m/s, kedalaman laut pada titik tersebut adalah...`,
        options: [
            "A. 3.000 m",
            "B. 6.000 m",
            "C. 9.000 m",
            "D. 12.000 m"
        ]
    },
    {
        id: 4, type: "PG",
        text: `Seorang siswa melakukan percobaan dengan mengetuk tiga gelas identik yang berisi air dengan volume berbeda menggunakan sendok yang sama. Ia menyimpulkan bahwa semakin banyak air dalam gelas, semakin rendah nada suara yang dihasilkan. Kesimpulan ini paling tepat didasari oleh pemahaman bahwa....`,
        options: [
            "A. Air berperan sebagai medium perambat bunyi dari gelas ke telinga.",
            "B. Semakin banyak volume air, semakin besar tekanan hidrostatisnya sehingga menghambat getaran.",
            "C. Air yang lebih banyak menambah massa sistem gelas-air, menyebabkan frekuensi getaran menurun.",
            "D. Getaran sendok yang lebih kuat pada gelas berisi air sedikit akan menghasilkan nada yang lebih tinggi."
        ]
    },
    {
        id: 5, type: "PG",
        text: `Seorang astronom pemula menggunakan teropong bintang untuk pertama kalinya. Ia berhasil memperbesar bayangan sebuah planet, tetapi ia mengeluhkan bahwa bayangan planet yang dilihatnya terlihat terbalik. Analisis yang paling tepat untuk menjelaskan mengapa hal ini terjadi adalah....`,
        options: [
            "A. Lensa okuler terbalik pemasangannya sehingga membalikkan arah bayangan.",
            "B. Cahaya dari planet terlalu kuat sehingga secara otomatis membalikkan bayangan di lensa objektif.",
            "C. Lensa objektif membentuk bayangan terbalik, dan lensa okuler hanya memperbesar bayangan terbalik tersebut tanpa membalikkannya kembali.",
            "D. Teropong tersebut hanya dirancang untuk benda sangat jauh (bintang), dan tidak dapat bekerja dengan benar untuk benda yang \"relatif\" dekat seperti planet."
        ]
    },
    {
        id: 6, type: "PG",
        text: `Perhatikan tabel data sifat fisik beberapa unsur berikut!<br>
        <div class="overflow-x-auto my-3"><table class="w-full text-sm text-left text-slate-500 border border-slate-200">
            <thead class="text-xs text-slate-700 uppercase bg-slate-50 border-b border-slate-200">
                <tr><th class="px-4 py-2">No</th><th class="px-4 py-2">Unsur</th><th class="px-4 py-2">Wujud</th><th class="px-4 py-2">Konduktor</th></tr>
            </thead>
            <tbody>
                <tr class="bg-white border-b"><td class="px-4 py-2">1</td><td class="px-4 py-2">Fe</td><td class="px-4 py-2">Padat</td><td class="px-4 py-2">Ya</td></tr>
                <tr class="bg-slate-50 border-b"><td class="px-4 py-2">2</td><td class="px-4 py-2">O</td><td class="px-4 py-2">Gas</td><td class="px-4 py-2">Tidak</td></tr>
                <tr class="bg-white border-b"><td class="px-4 py-2">3</td><td class="px-4 py-2">Cu</td><td class="px-4 py-2">Padat</td><td class="px-4 py-2">Ya</td></tr>
                <tr class="bg-slate-50"><td class="px-4 py-2">4</td><td class="px-4 py-2">S</td><td class="px-4 py-2">Padat</td><td class="px-4 py-2">Tidak</td></tr>
            </tbody>
        </table></div>Berdasarkan data yang disajikan dalam tabel, manakah yang merupakan pasangan unsur yang pasti termasuk golongan non-logam?`,
        options: [
            "A. Unsur 1 dan 3",
            "B. Unsur 2 dan 4",
            "C. Unsur 1 dan 2",
            "D. Unsur 3 dan 4"
        ]
    },
    {
        id: 7, type: "PG",
        text: `Perhatikan ilustrasi proses penyaringan air garam berikut.<br>Jika air garam tersebut dianggap sebagai sebuah campuran, maka pernyataan yang paling benar mengenai komponen penyusunnya adalah...`,
        options: [
            "A. Garam dan air masing-masing adalah campuran dari unsur-unsur.",
            "B. Garam adalah senyawa dan air adalah unsur.",
            "C. Garam adalah senyawa (NaCl) dan air (H2O) juga merupakan senyawa.",
            "D. Garam dan air keduanya adalah unsur yang membentuk campuran."
        ]
    },
    {
        id: 8, type: "PG",
        text: `Senyawa cuka memiliki rumus kimia CH3COOH. Berdasarkan rumus tersebut, jumlah atom masing-masing unsur penyusunnya adalah...`,
        options: [
            "A. 1 atom C, 3 atom H, dan 2 atom O",
            "B. 2 atom C, 4 atom H, dan 2 atom O",
            "C. 2 atom C, 3 atom H, dan 2 atom O",
            "D. 1 atom C, 4 atom H, dan 2 atom O"
        ]
    },
    {
        id: 9, type: "PG",
        text: `Perhatikan gambar metode pemisahan campuran berikut!<br>
        <div class="flex flex-col items-center justify-center p-4 my-4 bg-slate-50 border border-slate-200 rounded-lg w-full max-w-sm mx-auto">
            <div class="text-center mb-2"><i class="fas fa-filter text-3xl text-slate-400"></i></div>
            <div class="bg-amber-100 border border-amber-300 text-amber-800 text-xs px-2 py-1 rounded mb-2">A (Padatan tertahan di atas saringan)</div>
            <div class="h-8 w-1 border-l-2 border-dashed border-slate-400"></div>
            <div class="text-center my-2"><i class="fas fa-flask text-3xl text-blue-400"></i></div>
            <div class="bg-blue-100 border border-blue-300 text-blue-800 text-xs px-2 py-1 rounded">B (Cairan bening di bawah)</div>
        </div>Berdasarkan gambar, bagian yang ditunjukkan oleh huruf A dan B secara berurutan adalah....`,
        options: [
            "A. Filtrat dan Residu",
            "B. Residu dan Filtrat",
            "C. Endapan dan Suspensi",
            "D. Filtrat dan Larutan"
        ]
    },
    {
        id: 10, type: "PG",
        text: `Perhatikan tabel jenis zat dan contohnya berikut ini!<br>
        <div class="overflow-x-auto my-3"><table class="w-full text-sm text-left text-slate-500 border border-slate-200">
            <thead class="text-xs text-slate-700 uppercase bg-slate-50 border-b border-slate-200">
                <tr><th class="px-4 py-2">No</th><th class="px-4 py-2">Jenis Zat</th><th class="px-4 py-2">Contoh</th></tr>
            </thead>
            <tbody>
                <tr class="bg-white border-b"><td class="px-4 py-2">1</td><td class="px-4 py-2">Unsur</td><td class="px-4 py-2">Besi (Fe), Oksigen (O2)</td></tr>
                <tr class="bg-slate-50 border-b"><td class="px-4 py-2">2</td><td class="px-4 py-2">Senyawa</td><td class="px-4 py-2">Air (H2O), Garam Dapur (NaCl)</td></tr>
                <tr class="bg-white border-b"><td class="px-4 py-2">3</td><td class="px-4 py-2">Campuran Homogen</td><td class="px-4 py-2">Air Sirup, Udara</td></tr>
                <tr class="bg-slate-50"><td class="px-4 py-2">4</td><td class="px-4 py-2">Campuran Heterogen</td><td class="px-4 py-2">Air dengan Pasir, Air dengan Minyak</td></tr>
            </tbody>
        </table></div>Berdasarkan tabel di atas, pasangan data yang berhubungan dengan tepat antara jenis zat dan contohnya adalah ...`,
        options: [
            "A. 1, 2, dan 3",
            "B. 1, 3, dan 4",
            "C. 2, 3 dan 4",
            "D. 1, 2, 3 dan 4"
        ]
    },
    {
        id: 11, type: "PG",
        text: `Perhatikan gambar struktur Bumi berikut.<br>
        <div class="overflow-x-auto my-3"><table class="w-full text-sm text-left text-slate-500 border border-slate-200">
            <tbody>
                <tr class="bg-white border-b"><td class="px-4 py-2 font-medium">1. Kerak bumi</td><td class="px-4 py-2">A. Cairan Besi dan nikel</td></tr>
                <tr class="bg-slate-50 border-b"><td class="px-4 py-2 font-medium">2. Mantel bumi</td><td class="px-4 py-2">B. Padatan besi dan nikel</td></tr>
                <tr class="bg-white border-b"><td class="px-4 py-2 font-medium">3. Inti Luar</td><td class="px-4 py-2">C. Batuan silikat padat dan kental</td></tr>
                <tr class="bg-slate-50"><td class="px-4 py-2 font-medium">4. Inti dalam</td><td class="px-4 py-2">D. Silika dan Alumunium/Magnesium</td></tr>
            </tbody>
        </table></div>Pasangan antara lapisan bumi dan kandungan materinya yang benar adalah ...`,
        options: [
            "A. 1-D, 2-C, 3-A, 4-B",
            "B. 1-D, 2-A, 3-C, 4-B",
            "C. 1-C, 2-D, 3-B, 4-A",
            "D. 1-A, 2-C, 3-D, 4-B"
        ]
    },
    {
        id: 12, type: "PG",
        text: `Perhatikan pernyataan mengenai ciri salah satu lapisan struktur bumi berikut!<br>"Lapisan ini berada di bawah mantel bumi, berwujud cair (pekat seperti magma) yang terdiri dari campuran lelehan besi dan nikel, serta tidak mengandung air."<br>Berdasarkan ciri-ciri di atas, lapisan struktur bumi yang dimaksud adalah ....`,
        options: [
            "A. Kerak Bumi",
            "B. Mantel Bumi (Astenosfer)",
            "C. Inti Luar (Outer core)",
            "D. Inti Dalam (Inner core)"
        ]
    },
    {
        id: 13, type: "PG",
        text: `Bentuk muka bumi berupa daratan yang menonjol tinggi ke atas, memiliki puncak, lereng, dan ketinggian lebih dari 600 meter di atas permukaan laut adalah ....`,
        options: [
            "A. Dataran rendah",
            "B. Bukit",
            "C. Gunung",
            "D. Dataran Tinggi"
        ]
    },
    {
        id: 14, type: "PG",
        text: `Perhatikan gambar berikut yang menunjukkan tiga tipe gerakan lempeng bumi.<br>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-4 w-full max-w-2xl mx-auto">
            <div class="flex flex-col items-center p-4 bg-slate-50 border border-slate-200 rounded-lg shadow-sm text-center">
                <div class="font-semibold text-sm mb-3">Gambar 1</div>
                <div class="flex gap-4 text-rose-500 text-2xl font-bold">
                    <i class="fas fa-arrow-left"></i> <i class="fas fa-arrow-right"></i>
                </div>
                <div class="text-xs mt-3 text-slate-500">Lempeng saling menjauh & magma naik</div>
            </div>
            <div class="flex flex-col items-center p-4 bg-slate-50 border border-slate-200 rounded-lg shadow-sm text-center">
                <div class="font-semibold text-sm mb-3">Gambar 2</div>
                <div class="flex gap-2 text-blue-500 text-2xl font-bold">
                    <i class="fas fa-arrow-right"></i> <div class="w-1 h-6 bg-slate-400 skew-x-[20deg]"></div> <i class="fas fa-arrow-left"></i>
                </div>
                <div class="text-xs mt-3 text-slate-500">Lempeng bertumbukan & menunjam</div>
            </div>
            <div class="flex flex-col items-center p-4 bg-slate-50 border border-slate-200 rounded-lg shadow-sm text-center">
                <div class="font-semibold text-sm mb-3">Gambar 3</div>
                <div class="flex gap-2 text-emerald-500 text-2xl font-bold">
                    <i class="fas fa-arrow-up"></i> <i class="fas fa-arrow-down"></i>
                </div>
                <div class="text-xs mt-3 text-slate-500">Lempeng saling bergeser sejajar</div>
            </div>
        </div>Berdasarkan ilustrasi tersebut, pasangan tipe gerakan lempeng yang tepat secara berurutan adalah....`,
        options: [
            "A. Divergen - Konvergen - Transform",
            "B. Transform - Divergen - Konvergen",
            "C. Konvergen - Transform - Divergen",
            "D. Divergen - Transform - Konvergen"
        ]
    },
    {
        id: 15, type: "PG",
        text: `Perhatikan informasi berikut:<br>1) Terjadi di daerah sekitar gunung api aktif dan sering disertai aktivitas magma.<br>2) Terjadi akibat pergeseran lempeng tektonik dan biasanya memiliki kekuatan besar serta dampak luas.<br>3) Terjadi karena runtuhan batuan di daerah gua atau tambang dan umumnya berskala kecil.<br>4) Terjadi akibat aktivitas manusia seperti peledakan atau uji coba nuklir.<br><br>Berdasarkan informasi tersebut, urutan jenis gempa bumi yang tepat adalah ....`,
        options: [
            "A. Vulkanik - Tektonik - Runtuhan - Buatan",
            "B. Tektonik - Vulkanik - Runtuhan - Buatan",
            "C. Vulkanik - Runtuhan - Tektonik - Buatan",
            "D. Tektonik - Buatan - Vulkanik - Runtuhan"
        ]
    },
    {
        id: 16, type: "PGK",
        text: `II. PILIHAN GANDA KOMPLEK<br>Pilihlah 2 jawaban yang paling tepat dengan memberi tanda centang pada kolom yang tersedia!<br><br>Sebuah jam meja tua menggunakan bandul sebagai pengatur waktu. Suatu hari, jam tersebut melambat (periode getarannya membesar). Setelah diperiksa, kemungkinan penyebab langsung dari kelambatan jam tersebut adalah...`,
        options: [
            "A. Beban bandul secara tidak sengaja bergerak naik, sehingga panjang tali efektif berkurang.",
            "B. Tali bandul mengalami peregangan kecil akibat usia, sehingga panjang tali efektif bertambah.",
            "C. Ruangan menjadi lebih panas, menyebabkan massa beban bandul sedikit bertambah.",
            "D. Jam tersebut dipindahkan ke lantai dua yang memiliki ketinggian lebih tinggi dari permukaan tanah."
        ]
    },
    {
        id: 17, type: "PGK",
        text: `Perhatikan beberapa contoh gelombang berikut!<br>1) Gelombang pada tali yang dihentakkan<br>2) Gelombang bunyi saat berbicara<br>3) Gelombang cahaya matahari<br>4) Gelombang pada slinky (pegas) yang didorong-tarik<br>5) Gelombang radio<br><br>Berdasarkan contoh di atas, pasangan contoh gelombang yang termasuk dalam kategori gelombang transversal adalah...`,
        options: [
            "A. 1, 3, dan 5",
            "B. 2 dan 4",
            "C. 1, 2, dan 4",
            "D. 3, 4, dan 5"
        ]
    },
    {
        id: 18, type: "PGK",
        text: `Manakah di antara alat-alat berikut yang secara khusus berfungsi untuk mengamati benda-benda yang sangat kecil yang tidak terlihat oleh mata normal?`,
        options: [
            "A. Mikroskop",
            "B. Teropong",
            "C. Kaca Pembesar (Lup)",
            "D. Periskop"
        ]
    },
    {
        id: 19, type: "PGK",
        text: `Perhatikan tabel data zat-zat kimia berikut.<br>
        <div class="overflow-x-auto my-3"><table class="w-full text-sm text-left text-slate-500 border border-slate-200">
            <thead class="text-xs text-slate-700 uppercase bg-slate-50 border-b border-slate-200">
                <tr><th class="px-4 py-2">No</th><th class="px-4 py-2">Nama Zat</th><th class="px-4 py-2">Fungsi / Sifat</th></tr>
            </thead>
            <tbody>
                <tr class="bg-white border-b"><td class="px-4 py-2">1</td><td class="px-4 py-2">Gula</td><td class="px-4 py-2">Pemanis</td></tr>
                <tr class="bg-slate-50 border-b"><td class="px-4 py-2">2</td><td class="px-4 py-2">Oksigen</td><td class="px-4 py-2">Pernapasan</td></tr>
                <tr class="bg-white border-b"><td class="px-4 py-2">3</td><td class="px-4 py-2">Air</td><td class="px-4 py-2">Pelarut</td></tr>
                <tr class="bg-slate-50"><td class="px-4 py-2">4</td><td class="px-4 py-2">Helium</td><td class="px-4 py-2">Pengisi balon</td></tr>
            </tbody>
        </table></div>Berdasarkan data dalam tabel, manakah yang merupakan senyawa?`,
        options: [
            "A. 1 dan 3",
            "B. 2 dan 4",
            "C. 3 dan 4",
            "D. 1 dan 4"
        ]
    },
    {
        id: 20, type: "PGK",
        text: `Perhatikan beberapa proses pemisahan campuran berikut!<br>1) Memisahkan ampas kopi dari air kopi menggunakan kertas filter.<br>2) Mengambil garam dari air laut dengan cara memanaskannya hingga air menguap.<br>3) Memisahkan campuran minyak goreng dan air dalam sebuah wadah gelas dengan membuang air di bagian bawah menggunakan pipet.<br>4) Menjernihkan air sumur yang keruh dengan melewatkannya pada wadah yang berisi lapisan ijuk, pasir, dan kerikil.<br><br>Manakah pernyataan yang menerapkan prinsip pemisahan campuran secara filtrasi?`,
        options: [
            "A. 1 dan 4",
            "B. 2 dan 3",
            "C. 3 dan 4",
            "D. 1 dan 2"
        ]
    },
    {
        id: 21, type: "PGK",
        text: `Rina secara tidak sengaja menjatuhkan bongkahan kapur barus ke dalam sebuah wadah berisi pasir kering. Kapur barus pecah dan bercampur homogen dengan butiran-butiran pasir. Untuk memisahkan kembali kedua zat tersebut, Rina dapat melakukan beberapa metode.<br>Manakah usulan metode pemisahan yang tepat untuk memisahkan campuran kapur barus dan pasir tersebut?`,
        options: [
            "A. Campuran dimasukkan ke dalam air dan diaduk, kemudian disaring untuk memisahkan pasir dari larutan kapur barus.",
            "B. Campuran digoyangkan dalam air sehingga pasir mengendap dan kapur barus mengapung di permukaan, lalu airnya dibuang.",
            "C. Campuran dipanaskan secara perlahan dalam wadah tertutup, lalu uap kapur barus yang menempel di bagian atas wadah didinginkan kembali.",
            "D. Campuran dilarutkan dalam alkohol, kemudian disaring untuk memisahkan pasirnya, dan alkohol diuapkan untuk mendapatkan kembali kapur barus."
        ]
    },
    {
        id: 22, type: "PGK",
        text: `Perhatikan nama-nama gunung berikut!<br>1) Gunung Merapi<br>2) Gunung Muria<br>3) Gunung Slamet<br>4) Gunung Prau<br><br>Berdasarkan daftar di atas, yang tergolong dalam gunung berapi aktif di wilayah Jawa Tengah ditunjukkan oleh nomor ...`,
        options: [
            "A. 1",
            "B. 2",
            "C. 3",
            "D. 4"
        ]
    },
    {
        id: 23, type: "PGK",
        text: `Perhatikan tabel protokol tindakan mitigasi untuk setiap status gunung berapi berikut.<br>
        <div class="overflow-x-auto my-3"><table class="w-full text-sm text-left text-slate-500 border border-slate-200">
            <thead class="text-xs text-slate-700 uppercase bg-slate-50 border-b border-slate-200">
                <tr><th class="px-4 py-2">Status</th><th class="px-4 py-2">Tindakan Mitigasi</th></tr>
            </thead>
            <tbody>
                <tr class="bg-white border-b"><td class="px-4 py-2 font-medium text-green-600">Normal (Level I)</td><td class="px-4 py-2">Pemantauan visual dan instrumental rutin</td></tr>
                <tr class="bg-slate-50 border-b"><td class="px-4 py-2 font-medium text-yellow-600">Waspada (Level II)</td><td class="px-4 py-2">Kesiapsiagaan masyarakat di sekitar gunung</td></tr>
                <tr class="bg-white border-b"><td class="px-4 py-2 font-medium text-orange-500">Siaga (Level III)</td><td class="px-4 py-2">Larangan aktivitas di zona berbahaya</td></tr>
                <tr class="bg-slate-50"><td class="px-4 py-2 font-medium text-red-600">Awas (Level IV)</td><td class="px-4 py-2">Evakuasi warga dari zona berbahaya</td></tr>
            </tbody>
        </table></div>Manakah pasangan status dan tindakan yang sesuai dengan tabel di atas?`,
        options: [
            "A. Saat status Waspada, dilakukan evakuasi total warga.",
            "B. Saat status Siaga, dilakukan sosialisasi rencana evakuasi.",
            "C. Saat status Awas, dilakukan pemantauan visual rutin dari pos pengamatan.",
            "D. Saat status Normal, dilakukan penutupan total akses pendakian."
        ]
    },
    {
        id: 24, type: "PGK",
        text: `Gunung berapi yang sedang meletus mengeluarkan berbagai jenis material, baik dalam bentuk padat, cair, maupun gas. Dari daftar di bawah ini, manakah dua bahan yang termasuk dalam kategori material padat (eflata) yang dikeluarkan langsung dari kawah gunung berapi?`,
        options: [
            "A. Lava",
            "B. Lapili",
            "C. Bom (Batu besar)",
            "D. Solfator"
        ]
    },
    {
        id: 25, type: "PGK",
        text: `Perhatikan tabel kategori gempa bumi berdasarkan magnitudo (Skala Richter/SR) dan efek kerusakan yang ditimbulkan berikut!<br>
        <div class="overflow-x-auto my-3"><table class="w-full text-sm text-left text-slate-500 border border-slate-200">
            <thead class="text-xs text-slate-700 uppercase bg-slate-50 border-b border-slate-200">
                <tr><th class="px-4 py-2">Kategori</th><th class="px-4 py-2">Skala Richter (SR)</th><th class="px-4 py-2">Efek Kerusakan</th></tr>
            </thead>
            <tbody>
                <tr class="bg-white border-b"><td class="px-4 py-2">1 - Kecil</td><td class="px-4 py-2">3.0 - 3.9</td><td class="px-4 py-2">Jarang menimbulkan kerusakan</td></tr>
                <tr class="bg-slate-50 border-b"><td class="px-4 py-2">2 - Sedang</td><td class="px-4 py-2">4.0 - 4.9</td><td class="px-4 py-2">Jendela bergetar</td></tr>
                <tr class="bg-white border-b"><td class="px-4 py-2">3 - Merusak</td><td class="px-4 py-2">5.0 - 5.9</td><td class="px-4 py-2">Kerusakan bangunan lemah</td></tr>
                <tr class="bg-slate-50 border-b"><td class="px-4 py-2">4 - Besar</td><td class="px-4 py-2">7.0 - 7.9</td><td class="px-4 py-2">Kerusakan serius pada area luas</td></tr>
                <tr class="bg-white"><td class="px-4 py-2 font-bold text-red-600">5 - Sangat Besar</td><td class="px-4 py-2 font-bold text-red-600">> 8.0</td><td class="px-4 py-2 font-bold text-red-600">Kerusakan dahsyat</td></tr>
            </tbody>
        </table></div>Berdasarkan tabel di atas, pasangan kategori gempa dan efeknya yang tepat adalah...`,
        options: [
            "A. 1 dan 2",
            "B. 2 dan 3",
            "C. 3 dan 4",
            "D. 4 dan 5"
        ]
    }
];

window.onload = async () => {
    try {
        const gasResponse = await fetch(GAS_WEB_APP_URL);
        const configData = await gasResponse.json();
        
        if (configData.firebaseConfig) {
            const app = window.initializeApp(configData.firebaseConfig);
            db = window.getFirestore(app);
            await fetchClass8B();
        } else {
            throw new Error("Invalid config");
        }
    } catch (e) {
        console.error(e);
        document.getElementById('loading-text').innerText = "Gagal memuat data dari server.";
    }
};

async function fetchClass8B() {
    try {
        const querySnapshot = await window.getDocs(window.collection(db, "classes"));
        let targetClass = null;

        querySnapshot.forEach((doc) => {
            const data = doc.data();
            const name = (data.className || "").toUpperCase();
            // Cek spesifik untuk 8B / VIII B
            if (name.includes("8B") || name.includes("VIII B") || name.includes("VIIIB")) {
                targetClass = { id: doc.id, ...data };
            }
        });

        if (targetClass && targetClass.students) {
            classData = targetClass;
            renderStudents(classData.students);
            document.getElementById('loading-overlay').classList.add('hidden');
        } else {
            document.getElementById('loading-text').innerText = "Kelas VIII B tidak ditemukan di Database.";
        }
    } catch (e) {
        console.error("Error fetching class", e);
        document.getElementById('loading-text').innerText = "Error memuat database.";
    }
}

function normalizeStr(str) { 
    return (str || '').replace(/\s/g, '').split('').sort().join(''); 
}

function chunkString(str, chunkSize, maxChunks) {
    if(!str) str = "";
    let padded = str.padEnd(chunkSize * maxChunks, ' ').toUpperCase();
    let chunks = [];
    for(let i = 0; i < maxChunks; i++) {
        chunks.push(padded.slice(i * chunkSize, (i + 1) * chunkSize));
    }
    return chunks;
}

function parseUraianInput(inputStr, expectedLength) {
    let scores = [];
    if((inputStr||'').includes(',')) scores = (inputStr||'').split(',').map(s => parseFloat(s) || 0);
    else scores = (inputStr||'').split('').map(s => parseFloat(s) || 0);
    while(scores.length < expectedLength) scores.push(0);
    return scores;
}

function renderStudents(students) {
    const tbody = document.getElementById('student-list');
    tbody.innerHTML = '';

    const kkm = classData.metaKkm || 75;
    const numPG = classData.numPG || 5;
    const numPGK = classData.numPGK || 2;
    const numUraian = classData.numUraian || 2;
    const weightPG = classData.weightPG || 1;
    const weightPGK = classData.weightPGK || 2;
    const weightUraian = classData.weightUraian || 5;
    
    const keyPGArr = (classData.keyPG || '').split('');
    const optsPGK = classData.optsPGK || 1;
    const cleanKeyPGK = (classData.keyPGK || '').replace(/,/g, '');
    const keyPGKArr = chunkString(cleanKeyPGK, optsPGK, numPGK).map(normalizeStr);

    students.forEach((student, index) => {
        let scorePG = 0, scorePGK = 0, scoreUraian = 0;
        
        let stuPGArr = (student.pg || '').split('');
        let cleanStuPGK = (student.pgk || '').replace(/,/g, '');
        let stuPGKArr = chunkString(cleanStuPGK, optsPGK, numPGK).map(normalizeStr);
        let stuUraianArr = parseUraianInput(student.uraian, numUraian);

        let pgDetails = [];
        let pgkDetails = [];

        for(let i=0; i<numPG; i++) {
            let status = 0;
            let ans = stuPGArr[i];
            if (!ans || ans === ' ' || ans === '-') status = -1;
            else if(ans === keyPGArr[i]) {
                scorePG += weightPG;
                status = 1;
            }
            pgDetails.push(status);
        }

        for(let i=0; i<numPGK; i++) {
            let status = 0;
            let ans = stuPGKArr[i];
            if (!ans || ans === '') status = -1;
            else if(ans === keyPGKArr[i] && keyPGKArr[i] !== '') {
                scorePGK += weightPGK;
                status = 1;
            }
            pgkDetails.push(status);
        }

        for(let i=0; i<numUraian; i++) {
            let earned = stuUraianArr[i] || 0;
            if(earned > weightUraian) earned = weightUraian; 
            scoreUraian += earned;
        }

        let maxScore = (numPG * weightPG) + (numPGK * weightPGK) + (numUraian * weightUraian);
        let rawTotal = scorePG + scorePGK + scoreUraian;
        let totalScore = maxScore > 0 ? Math.round((rawTotal / maxScore) * 100) : 0;
        
        student.calculatedTotal = totalScore;
        student.pgDetails = pgDetails;
        student.pgkDetails = pgkDetails;

        const combinedStatus = [...pgDetails, ...pgkDetails];
        let wrongCount = 0;
        combinedStatus.forEach(status => {
            if (status !== 1 && status !== undefined) wrongCount++;
        });
        if (wrongCount > 25) wrongCount = 25; 

        const tr = document.createElement('tr');
        tr.className = "hover:bg-teal-50/30 ";

        let statusHtml = '';
        let btnHtml = '';

        if (totalScore < kkm) {
            statusHtml = `<div class="flex flex-col items-center justify-center gap-1">
                <span class="bg-rose-100 text-rose-700 px-3 py-1 rounded-full text-[10px] font-bold">REMIDIAL</span>
                <span class="text-xs font-bold text-slate-500">Nilai: ${totalScore} (Salah ${wrongCount})</span>
            </div>`;
            btnHtml = `<button onclick="window.startRemidial('${student.name}', ${index})" class="bg-teal-600 hover:bg-teal-700 text-white px-4 py-2 rounded-xl text-xs font-bold shadow-sm  hover:-.5 w-full">Kerjakan</button>`;
        } else {
            statusHtml = `<div class="flex flex-col items-center justify-center gap-1">
                <span class="bg-emerald-100 text-emerald-700 px-3 py-1 rounded-full text-[10px] font-bold">TUNTAS</span>
                <span class="text-xs font-bold text-slate-500">Nilai: ${totalScore}</span>
            </div>`;
            btnHtml = `<button disabled class="bg-slate-200 text-slate-400 px-4 py-2 rounded-xl text-xs font-bold cursor-not-allowed w-full">Selesai</button>`;
        }

        tr.innerHTML = `
            <td class="px-6 py-4 text-center font-bold text-slate-400 border-b border-slate-100">${index + 1}</td>
            <td class="px-6 py-4 font-semibold text-slate-700 border-b border-slate-100">${student.name}</td>
            <td class="px-6 py-4 text-center border-b border-slate-100">${statusHtml}</td>
            <td class="px-6 py-4 text-center border-b border-slate-100">${btnHtml}</td>
        `;
        tbody.appendChild(tr);
    });

    document.getElementById('search-student').addEventListener('input', (e) => {
        const keyword = e.target.value.toLowerCase();
        Array.from(tbody.children).forEach(row => {
            const name = row.children[1].innerText.toLowerCase();
            if (name.includes(keyword)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
}

window.startRemidial = function(studentName, studentIndex) {
    const student = classData.students[studentIndex];
    activeStudent = student;
    const combinedStatus = [...(student.pgDetails || []), ...(student.pgkDetails || [])];
    
    wrongQuestions = [];
    const limit = Math.min(25, combinedStatus.length);

    for (let i = 0; i < limit; i++) {
        if (combinedStatus[i] !== 1 && i < soalBank.length) {
            wrongQuestions.push(soalBank[i]);
        }
    }

    if (wrongQuestions.length === 0) {
        alert("Tidak ada soal PG/PGK yang salah.");
        return;
    }

    document.getElementById('active-student-name').innerText = studentName;
    document.getElementById('wrong-count').innerText = wrongQuestions.length;

    renderQuiz();

    document.getElementById('step-1').classList.add('hidden');
    document.getElementById('step-2').classList.remove('hidden');
};

window.backToStep1 = function() {
    document.getElementById('step-2').classList.add('hidden');
    document.getElementById('step-1').classList.remove('hidden');
}

function renderQuiz() {
    const container = document.getElementById('quiz-container');
    container.innerHTML = '';

    wrongQuestions.forEach((q, index) => {
        const isPGK = q.type === "PGK";
        const inputType = isPGK ? "checkbox" : "radio";
        
        let optionsHtml = '';
        q.options.forEach((opt, optIndex) => {
            const inputId = `q_${q.id}_opt_${optIndex}`;
            const nameAttr = isPGK ? `q_${q.id}[]` : `q_${q.id}`;
            
            let controlIndicator = '';
            if(isPGK) {
                controlIndicator = `
                    <div class="checkbox-square w-5 h-5 rounded border-2 border-slate-300 flex items-center justify-center ">
                        <i class="fa-solid fa-check text-white text-xs hidden"></i>
                    </div>`;
            } else {
                controlIndicator = `<div class="radio-circle w-5 h-5 rounded-full border-2 border-slate-300 "></div>`;
            }

            optionsHtml += `
                <div class="relative">
                    <input type="${inputType}" name="${nameAttr}" id="${inputId}" value="${optIndex}" class="${inputType}-custom  absolute inset-0 z-[-1]">
                    <label for="${inputId}" class="flex items-start gap-4 p-4 rounded-xl border-2 border-slate-100 cursor-pointer hover:bg-slate-50  font-medium text-slate-700">
                        ${controlIndicator}
                        <div class="flex-1 leading-relaxed">${opt}</div>
                    </label>
                </div>
            `;
        });

        const qCard = document.createElement('div');
        qCard.className = "bg-white p-6 sm:p-8 rounded-3xl shadow-sm border border-slate-200/60";
        qCard.innerHTML = `
            <div class="flex items-start gap-4 mb-6">
                <div class="w-10 h-10 shrink-0 bg-slate-100 rounded-xl flex items-center justify-center font-bold text-slate-500 font-heading">
                    ${q.id}
                </div>
                <div class="flex-1 text-slate-800 leading-relaxed font-medium pt-2">
                    ${q.text}
                </div>
            </div>
            <div class="pl-14 space-y-3">
                ${optionsHtml}
            </div>
        `;
        container.appendChild(qCard);
    });
}

window.submitQuiz = async function() {
    let allAnswered = true;
    wrongQuestions.forEach(q => {
        const isPGK = q.type === "PGK";
        const nameAttr = isPGK ? `q_${q.id}[]` : `q_${q.id}`;
        const inputs = document.querySelectorAll(`input[name="${nameAttr}"]:checked`);
        if (inputs.length === 0) allAnswered = false;
    });

    if (!allAnswered) {
        if(!confirm("Anda belum menjawab semua soal! Yakin ingin mengumpulkan?")) {
            return;
        }
    }

    const numPG = classData.numPG || 5;
    const numPGK = classData.numPGK || 2;
    const optsPGK = classData.optsPGK || 1;
    
    let stuPGArr = (activeStudent.pg || '').padEnd(numPG, ' ').split('');
    let oldStuPGKArr = chunkString((activeStudent.pgk || '').replace(/,/g, ''), optsPGK, numPGK);

    wrongQuestions.forEach((q) => {
        const isPGK = q.type === "PGK";
        const nameAttr = isPGK ? `q_${q.id}[]` : `q_${q.id}`;
        const inputs = document.querySelectorAll(`input[name="${nameAttr}"]:checked`);
        
        let ansChars = [];
        inputs.forEach(inp => {
            ansChars.push(String.fromCharCode(65 + parseInt(inp.value)));
        });
        const finalAns = ansChars.sort().join(''); // misal "A" atau "AB"
        
        const globalIndex = q.id - 1; // 0 sampai 24
        
        if (globalIndex < numPG) {
            stuPGArr[globalIndex] = finalAns.charAt(0) || ' ';
        } else if (globalIndex < numPG + numPGK) {
            const pgkIndex = globalIndex - numPG;
            oldStuPGKArr[pgkIndex] = finalAns.padEnd(optsPGK, ' ').substring(0, optsPGK);
        }
    });

    activeStudent.pg = stuPGArr.join('');
    activeStudent.pgk = oldStuPGKArr.join(',');

    // Calculate new score for display
    let newScorePG = 0;
    let newScorePGK = 0;
    const weightPG = classData.weightPG || 1;
    const weightPGK = classData.weightPGK || 2;
    const keyPGArr = (classData.keyPG || '').split('');
    const cleanKeyPGK = (classData.keyPGK || '').replace(/,/g, '');
    const keyPGKArr = chunkString(cleanKeyPGK, optsPGK, numPGK).map(normalizeStr);
    
    for(let i=0; i<numPG; i++) {
        if(stuPGArr[i] === keyPGArr[i] && keyPGArr[i]) newScorePG += weightPG;
    }
    for(let i=0; i<numPGK; i++) {
        if(oldStuPGKArr[i] === keyPGKArr[i] && keyPGKArr[i]) newScorePGK += weightPGK;
    }
    
    let scoreUraian = 0;
    const numUraian = classData.numUraian || 2;
    const weightUraian = classData.weightUraian || 5;
    let stuUraianArr = parseUraianInput(activeStudent.uraian, numUraian);
    for(let i=0; i<numUraian; i++) {
        let earned = stuUraianArr[i] || 0;
        if(earned > weightUraian) earned = weightUraian; 
        scoreUraian += earned;
    }
    
    let maxScore = (numPG * weightPG) + (numPGK * weightPGK) + (numUraian * weightUraian);
    let rawTotal = newScorePG + newScorePGK + scoreUraian;
    let newTotalScore = maxScore > 0 ? Math.round((rawTotal / maxScore) * 100) : 0;

    document.getElementById('step-2').classList.add('hidden');
    document.getElementById('loading-text').innerText = "Menyimpan Jawaban...";
    document.getElementById('loading-overlay').classList.remove('hidden');
    
    try {
        await window.setDoc(window.doc(db, "classes", classData.id), classData, {merge: true});
        document.getElementById('loading-overlay').classList.add('hidden');
        
        document.getElementById('final-score').innerText = newTotalScore;
        document.getElementById('step-3').classList.remove('hidden');
    } catch(e) {
        console.error(e);
        document.getElementById('loading-overlay').classList.add('hidden');
        alert("Gagal menyimpan data ke server. Periksa koneksi internet Anda.");
    }
}
