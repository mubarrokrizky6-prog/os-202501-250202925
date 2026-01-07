
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock



---

## Identitas
- **Nama**  : RIZKI FADIL MUBAROK
- **NIM**   : 250202925 
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

-Membuat program sederhana untuk mendeteksi deadlock.
-Menjalankan simulasi deteksi deadlock dengan dataset uji.
-Menyajikan hasil analisis deadlock dalam bentuk tabel.
-Memberikan interpretasi hasil uji secara logis dan sistematis.
-Menyusun laporan praktikum sesuai format yang ditentukan.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan Simulasi dan Deteksi Deadlock

-Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya yang sedang dipegang proses lain, sehingga tidak ada proses yang dapat melanjutkan eksekusi.

-Deadlock terjadi jika empat kondisi Coffman terpenuhi secara bersamaan, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait.

-Resource Allocation Graph (RAG) digunakan untuk memodelkan hubungan antara proses dan sumber daya, serta membantu menganalisis ada tidaknya siklus yang mengindikasikan deadlock.

-Deteksi deadlock dilakukan dengan algoritma pendeteksian (misalnya deteksi siklus atau matriks alokasi–permintaan) untuk mengidentifikasi proses yang terlibat deadlock tanpa mencegahnya sejak awal.

-Simulasi deadlock membantu memahami bagaimana konflik alokasi sumber daya terjadi dan bagaimana sistem operasi dapat mendeteksi serta menangani deadlock melalui terminasi proses atau preemption sumber daya.

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
- Jelaskan makna hasil percobaan Simulasi dan Deteksi Deadlock
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS) Simulasi dan Deteksi Deadlock
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)  Simulasi dan Deteksi Deadlock ?

  **JAWABAN**
  1. -Hasil simulasi menunjukkan bahwa deadlock dapat terjadi ketika proses saling menunggu sumber daya, sehingga sistem tidak dapat melanjutkan eksekusi proses.
     -Percobaan membuktikan bahwa algoritma deteksi deadlock mampu mengidentifikasi proses-proses yang terlibat dalam kondisi deadlock secara tepat.
     -Percobaan ini menegaskan pentingnya pengelolaan dan deteksi deadlock dalam sistem operasi untuk menjaga kinerja dan kestabilan sistem.

   2.   #. Hasil simulasi menunjukkan bahwa kernel mengatur seluruh alokasi sumber daya dan menggunakan data tersebut untuk mendeteksi kondisi deadlock saat                  proses saling menunggu.

        #. Deadlock terjadi karena proses melakukan system call untuk meminta atau mengunci sumber daya, sehingga terbentuk ketergantungan yang dicatat oleh                  kernel.

        #. Percobaan membuktikan bahwa dalam arsitektur sistem operasi, deteksi deadlock harus berada di tingkat kernel agar sistem dapat mengenali dan menangani             kebuntuan proses secara efektif.
        
   3.   -Implementasi KernePada Linux, mekanisme pengelolaan sumber daya lebih transparan dan fleksibel, sehingga simulasi deadlock dan proses deteksinya lebih mudah diamati. Pada Windows, banyak mekanisme bersifat tertutup, sehingga hasil deteksi deadlock biasanya tidak terlihat secara langsung oleh pengguna.

-System Call dan API
Linux menggunakan system call standar POSIX (misalnya fork, wait, lock) yang memudahkan pemantauan alokasi sumber daya. Windows menggunakan API tingkat tinggi (WinAPI), sehingga proses deteksi deadlock lebih tersembunyi di balik lapisan sistem.

-Hasil Simulasi
Pada Linux, deadlock dapat disimulasikan dan dideteksi secara eksplisit melalui tool atau program pengguna. Pada Windows, deadlock lebih sering ditangani secara internal oleh sistem, sehingga hasil simulasi tampak lebih stabil meskipun potensi deadlock tetap ada.

-Pendekatan Arsitektur
Linux cenderung memberikan kontrol lebih besar kepada pengguna dan developer untuk mengamati deadlock, sedangkan Windows menekankan kestabilan sistem dengan penanganan otomatis oleh kernel.   

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum Simulasi dan Deteksi Deadlock

-Praktikum menunjukkan bahwa deadlock dapat terjadi ketika proses saling menunggu sumber daya, sehingga sistem tidak dapat melanjutkan eksekusi proses.
-Hasil percobaan membuktikan bahwa mekanisme deteksi deadlock mampu mengidentifikasi proses-proses yang terlibat berdasarkan pola alokasi dan permintaan sumber daya.
-Praktikum menegaskan pentingnya peran kernel sistem operasi dalam mengelola sumber daya dan menjaga kestabilan sistem melalui deteksi deadlock.

---
**Tugas**
1. Buat program simulasi deteksi deadlock.
2. Jalankan program dengan dataset uji.
3. Sajikan hasil analisis dalam tabel dan narasi.
4. Tulis laporan praktikum pada laporan.md.

   
## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?
   **Jawaban:**  -Deadlock Prevention
                  Bertujuan mencegah deadlock sejak awal dengan menghilangkan salah satu dari empat kondisi deadlock (misalnya melarang hold and wait). Cara ini                     aman, tetapi sering mengurangi efisiensi sistem.

-Deadlock Avoidance
Bertujuan menghindari deadlock dengan cara mengevaluasi setiap permintaan sumber daya agar sistem tetap berada pada safe state (contoh: Banker’s Algorithm). Metode ini lebih fleksibel, tetapi membutuhkan informasi lengkap tentang kebutuhan sumber daya proses.

-Deadlock Detection
Membiarkan deadlock terjadi terlebih dahulu, lalu mendeteksinya dan menanganinya (misalnya dengan menghentikan proses). Cara ini lebih sederhana, tetapi dapat menyebabkan gangguan sementara pada sistem.


2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Jawaban:**
   -Tidak semua deadlock bisa dicegah atau dihindari tanpa mengorbankan kinerja sistem. Prevention dan avoidance sering membatasi penggunaan sumber daya atau membutuhkan informasi lengkap yang tidak selalu tersedia.
-Deadlock dapat muncul secara dinamis akibat interaksi proses yang kompleks dan tidak terduga, sehingga sistem perlu mekanisme untuk mengenali kondisi tersebut saat terjadi.
-Menjaga kestabilan sistem dengan memungkinkan kernel mengidentifikasi proses yang macet dan melakukan penanganan (misalnya terminasi atau preemption sumber daya), agar sistem dapat kembali berjalan normal.


3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   **Jawaban:**
**Kelebihan**
-Lebih fleksibel karena tidak membatasi cara proses meminta dan menggunakan sumber daya.
-Efisien untuk sistem dengan deadlock jarang terjadi, karena pemeriksaan hanya dilakukan secara berkala.
-Implementasi lebih sederhana dibanding avoidance, karena tidak memerlukan informasi kebutuhan maksimum proses.

**Kekurangan**
-Deadlock dibiarkan terjadi terlebih dahulu, sehingga proses bisa macet sementara.
-Membutuhkan overhead tambahan untuk menjalankan algoritma deteksi, terutama pada sistem besar.
-Penanganan deadlock dapat merugikan proses, misalnya terminasi atau rollback yang menyebabkan kehilangan data atau waktu komputasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Tidak ada mungkin
- Bagaimana cara Anda mengatasinya?  Berusaha

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
