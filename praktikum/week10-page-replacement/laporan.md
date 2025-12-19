
# Laporan Praktikum Minggu [X]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : RIZKI FADIL MUBAROK  
- **NIM**   : 250202925
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
Setelah menyelesaikan tugas ini, mahasiswa mampu:

-Mengimplementasikan algoritma page replacement FIFO dalam program.
-Mengimplementasikan algoritma page replacement LRU dalam program.
-Menjalankan simulasi page replacement dengan dataset tertentu.
-Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
-Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan Manajemen Memori – Page Replacement (FIFO & LRU)

Ringkasan Teori Manajemen Memori – Page Replacement (FIFO & LRU):
-Manajemen memori bertujuan mengatur penggunaan memori utama agar proses dapat berjalan secara efisien.
-Page replacement digunakan ketika terjadi page fault dan memori fisik sudah penuh.
-Algoritma FIFO mengganti halaman yang pertama kali masuk ke memori.
-Algoritma LRU mengganti halaman yang paling lama tidak digunakan.
-Kinerja algoritma diukur dari jumlah page fault yang terjadi.

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
**- Jelaskan makna hasil percobaan  Manajemen Memori – Page Replacement (FIFO & LRU)**
 Hasil percobaan menunjukkan bahwa pemilihan algoritma page replacement sangat memengaruhi kinerja memori sistem.
 Algoritma FIFO cenderung menghasilkan jumlah page fault lebih banyak karena hanya berdasarkan urutan masuk halaman.
 Algoritma LRU lebih efisien karena mempertimbangkan riwayat penggunaan halaman.
 Semakin sedikit page fault yang terjadi, semakin baik kinerja manajemen memori sistem.

**- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).**
1. Fungsi Kernel
Kernel bertanggung jawab mengelola memori utama, termasuk menangani page fault dan menentukan halaman mana yang harus diganti. Hasil percobaan FIFO dan LRU mencerminkan keputusan kernel dalam memilih halaman yang dikeluarkan dari memori, yang berdampak langsung pada jumlah page fault.

2. System Call
Ketika proses mengakses halaman yang tidak ada di memori, terjadi page fault yang menyebabkan proses berinteraksi dengan kernel melalui mekanisme system call. Kernel kemudian memuat halaman dari penyimpanan sekunder dan menerapkan algoritma page replacement yang sesuai.

3. Arsitektur Sistem Operasi
Dalam arsitektur OS, manajemen memori merupakan bagian inti yang bekerja bersama CPU dan penyimpanan sekunder. Hasil percobaan FIFO dan LRU menunjukkan bagaimana modul manajemen memori dalam kernel berperan menjaga efisiensi penggunaan memori dan kinerja sistem secara keseluruhan.
  
**- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?**  

Algoritma yang digunakan
Linux umumnya menggunakan pendekatan berbasis LRU (atau mendekatinya), sehingga jumlah page fault relatif lebih sedikit. Windows juga menggunakan algoritma berbasis LRU, tetapi dengan modifikasi dan penyesuaian internal.

Manajemen memori internal
Linux lebih fleksibel dalam pengaturan cache dan buffer, sedangkan Windows memiliki mekanisme manajemen memori yang lebih terstruktur dan berbasis prioritas proses. Hal ini dapat memengaruhi frekuensi page fault.

Hasil kinerja
Pada beban dan pola akses yang sama, Linux cenderung lebih efisien dalam penggunaan memori, sementara Windows lebih fokus pada stabilitas dan respons aplikasi.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum Manajemen Memori – Page Replacement (FIFO & LRU)

-Algoritma FIFO lebih sederhana tetapi cenderung menghasilkan page fault lebih banyak.
-Algoritma LRU lebih efisien karena mempertimbangkan pola akses halaman.
-Pemilihan algoritma page replacement berpengaruh langsung terhadap kinerja manajemen memori sistem.

**Tugas**
Buat program simulasi page replacement FIFO dan LRU.
Jalankan simulasi dengan dataset uji.
Sajikan hasil simulasi dalam tabel atau grafik.
Tulis laporan praktikum pada laporan.md.

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
   **Jawaban:**
 - FIFO (First In First Out) mengganti halaman yang paling awal masuk ke memori, tanpa memperhatikan apakah halaman tersebut masih sering digunakan.

- LRU (Least Recently Used) mengganti halaman yang paling lama tidak diakses, sehingga lebih sesuai dengan pola penggunaan memori.
  
2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?
   **Jawaban:**
karena algoritma ini hanya mempertimbangkan urutan masuk halaman, bukan pola penggunaannya.
Akibatnya, ketika jumlah frame ditambah:
-Halaman yang masih sering digunakan bisa tetap tergantikan hanya karena masuk lebih awal.
-Penambahan frame justru dapat menyebabkan jumlah page fault meningkat, bukan menurun.
Fenomena inilah yang disebut Belady’s Anomaly, dan hal ini tidak terjadi pada algoritma berbasis stack seperti LRU karena LRU mempertahankan halaman yang baru saja digunakan.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:**
   LRU umumnya menghasilkan performa lebih baik dibanding FIFO karena mempertimbangkan pola akses halaman.

-LRU mengganti halaman yang paling lama tidak digunakan, sehingga halaman yang sering diakses tetap berada di memori.
-FIFO hanya berdasarkan urutan masuk halaman, tanpa melihat apakah halaman tersebut masih dibutuhkan.
-Akibatnya, LRU menghasilkan page fault lebih sedikit dan penggunaan memori yang lebih efisien.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Belum bisa mengerjakan tugas ini dengan mandiri sepenuhnya
- Bagaimana cara Anda mengatasinya?  Kerja kelompok

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
