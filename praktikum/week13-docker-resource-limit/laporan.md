
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)



---

## Identitas
- **Nama**  : RIZKI FADIL MUBAROK  
- **NIM**   : 250202925  
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

-Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
-Membangun image dan menjalankan container.
-Menjalankan container dengan pembatasan CPU dan memori.
-Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
-Menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan Docker – Resource Limit (CPU & Memori)
a. Docker memungkinkan pembatasan penggunaan CPU dan memori pada container menggunakan mekanisme cgroups.
b. Pembatasan resource mencegah satu container mendominasi sumber daya sistem.
c. Pengaturan resource limit meningkatkan stabilitas dan keandalan sistem dalam lingkungan multi-container.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
## - Jelaskan makna hasil percobaan Docker – Resource Limit (CPU & Memori)
  ## jawab
1. Efektivitas pembatasan resource
Hasil percobaan menunjukkan bahwa Docker mampu membatasi penggunaan CPU dan memori container sesuai konfigurasi yang diberikan, sehingga penggunaan resource tidak melebihi batas yang ditentukan.

2. Pengaruh langsung terhadap performa aplikasi
Container dengan batas CPU rendah menunjukkan proses yang lebih lambat, sedangkan batas memori yang ketat dapat menyebabkan aplikasi berhenti (OOM Kill) jika melebihi kapasitas yang diizinkan.

3. Perlindungan terhadap sistem host
Dengan adanya resource limit, sistem host tetap stabil meskipun container menjalankan aplikasi yang berat atau boros resource.

4. Simulasi kondisi produksi
Percobaan ini membuktikan bahwa resource limit berguna untuk mensimulasikan kondisi lingkungan produksi, sehingga pengujian aplikasi menjadi lebih realistis dan terkontrol.

## - Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
 ## jawaba
a. Fungsi Kernel (Manajemen Resource)
Hasil pembatasan CPU dan memori pada container menunjukkan peran kernel Linux dalam manajemen resource. Kernel mengatur penjadwalan CPU dan alokasi memori melalui mekanisme cgroups, sehingga setiap proses di dalam container hanya dapat menggunakan resource sesuai batas yang ditetapkan.

b. System Call
Aplikasi di dalam container tetap menggunakan system call yang sama (misalnya untuk alokasi memori atau eksekusi proses). Namun, kernel memeriksa batas cgroups saat system call tersebut dijalankan, sehingga permintaan resource dapat dibatasi atau ditolak sesuai konfigurasi Docker.

c. Arsitektur Sistem Operasi
Dalam arsitektur OS berbasis kernel monolitik (Linux), Docker berjalan di user space sebagai container runtime, sementara isolasi dan pembatasan resource dilakukan di kernel space. Hasil percobaan membuktikan bahwa container tidak memiliki kernel sendiri, melainkan bergantung langsung pada kernel host.

d. Isolasi Proses dan Stabilitas Sistem
Hasil percobaan yang menunjukkan container tidak mengganggu sistem host menegaskan konsep arsitektur OS tentang isolasi proses, di mana kernel menjaga agar kegagalan atau beban berlebih pada satu proses tidak berdampak pada proses lain.

## - Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
## -Linux (Native Container Support)
Pada Linux, Docker berjalan langsung di atas kernel Linux. Pembatasan CPU dan memori menggunakan cgroups dan namespaces bekerja secara native, sehingga hasil percobaan lebih akurat, stabil, dan sesuai dengan teori manajemen resource OS.

## -Windows (Virtualisasi Tambahan)
Pada Windows, Docker umumnya berjalan melalui VM (WSL2 atau Hyper-V) yang menjalankan kernel Linux. Akibatnya, pembatasan resource diterapkan terlebih dahulu pada VM, lalu pada container, sehingga hasilnya kurang langsung dibanding Linux.

## -Performa dan Akurasi Limit
Di Linux, efek limit CPU dan memori terlihat jelas pada container. Di Windows, penggunaan resource masih dipengaruhi oleh konfigurasi VM, sehingga performa container bisa berbeda meskipun limit Docker sama.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum Docker – Resource Limit (CPU & Memori)
-Docker mampu membatasi penggunaan CPU dan memori pada container secara efektif menggunakan mekanisme cgroups, sehingga resource dapat dikontrol sesuai kebutuhan.
-Penerapan resource limit mencegah satu container menggunakan sumber daya secara berlebihan dan mengganggu container lain.
-Pengaturan batas CPU dan memori meningkatkan stabilitas serta efisiensi sistem dalam menjalankan banyak container secara bersamaan.

---
## Tugas

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?
   **Jawaban:**
a. Mencegah penggunaan resource berlebihan
Tanpa batasan, satu container dapat menggunakan seluruh CPU atau memori host, sehingga menyebabkan container lain atau sistem menjadi lambat bahkan tidak responsif.

b. Menjaga stabilitas sistem
Pembatasan resource membantu mencegah terjadinya crash atau Out Of Memory (OOM) yang dapat memengaruhi keseluruhan sistem host.

c. Distribusi resource yang adil
Dengan adanya limit, setiap container mendapatkan jatah resource sesuai kebutuhan, sehingga semua layanan dapat berjalan secara seimbang.

d. Meningkatkan keandalan aplikasi
Aplikasi menjadi lebih terkontrol dan dapat diuji perilakunya saat berada dalam kondisi resource terbatas, mirip dengan lingkungan produksi.  

2. Apa perbedaan VM dan container dalam konteks isolasi resource?
   **Jawaban:**
a. ingkat Isolasi
VM memiliki isolasi yang lebih kuat karena setiap VM menjalankan sistem operasi lengkap dengan kernel sendiri. Container hanya mengisolasi aplikasi dan dependensinya, serta berbagi kernel host, sehingga isolasinya lebih ringan.

b. Pengelolaan Resource
Pada VM, CPU dan memori dialokasikan secara tetap (fixed) sejak VM dijalankan. Pada container, resource bersifat dinamis dan dibatasi menggunakan cgroups, sehingga lebih fleksibel.

c. Overhead dan Efisiensi
VM membutuhkan resource lebih besar karena adanya OS tambahan, sedangkan container lebih ringan dan efisien dalam penggunaan CPU dan memori.

d. Keamanan Isolasi
Karena kernel terpisah, VM umumnya lebih aman dalam hal isolasi resource. Container cukup aman, tetapi ketergantungan pada kernel host membuat isolasinya relatif lebih lemah dibanding VM.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?
   **Jawaban:**
a. Aplikasi dapat berhenti secara tiba-tiba (OOM Kill)
Jika penggunaan memori melebihi batas yang ditentukan, kernel akan menjalankan Out Of Memory (OOM) Killer dan menghentikan proses di dalam container.

b. Penurunan performa aplikasi
Aplikasi dapat menjadi lebih lambat karena sering melakukan memory allocation dan garbage collection untuk menyesuaikan dengan batas memori.

c. Potensi kegagalan layanan
Aplikasi yang tidak dirancang untuk kondisi memori terbatas dapat mengalami error, crash, atau tidak dapat melayani permintaan pengguna.

d. Mendorong optimasi aplikasi
Dengan adanya limit memori, pengembang terdorong untuk mengoptimalkan penggunaan memori agar aplikasi lebih efisien dan stabil.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Banyak tugas SO yg belum saya selesaikan,
- Bagaimana cara Anda mengatasinya?  dikerjakan semampunya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
