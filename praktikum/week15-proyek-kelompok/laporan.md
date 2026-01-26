
# Laporan Praktikum Minggu 15
Topik: Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)

---

## Pembagian Peran dan Kontribusi
Nama : Rizki Fadil Mubarok 

 Nim  : (250202925) 
 
 Kelas: 1IKRA 
 
 Peran: Implementasi CPU Scheduling, integrasi program, dan Dockerisasi.

 Nama : Rizal Prasetyo
 
 Nim  : (250202965) 
 
 Kelas: 1IKRA
 
 Peran: Implementasi Page Replacement, pengujian dataset, dan dokumentasi.

---

## Tujuan
Setelah menyelesaikan proyek ini, mahasiswa mampu:

-Bekerja kolaboratif dalam tim dengan pembagian peran yang jelas.

-Mengintegrasikan beberapa konsep sistem operasi dalam satu aplikasi sederhana.

-Mengelola proyek menggunakan Git (branch/PR/commit yang rapi).

-Menyusun dokumentasi dan laporan proyek yang sistematis.

-Melakukan presentasi dan demo hasil proyek.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)

1. CPU Scheduling
Menentukan urutan proses agar penggunaan CPU efisien.

2. Algoritma Penjadwalan
FCFS, SJF, dan Round Robin memengaruhi waktu tunggu dan respons proses.

3. Manajemen Memori
Mengatur alokasi memori agar proses berjalan stabil.

4. Container
Menjalankan proses secara terisolasi dengan berbagi kernel host.

5. Pembatasan Sumber Daya
CPU dan memori dibatasi agar tidak terjadi monopoli proses.


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

![Screenshot hasil](screenshots/main.py(Menu CLI).png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  ## jawaban
-Algoritma SJF cenderung menghasilkan rata-rata waiting time yang lebih kecil daripada FCFS.

-Pada Page Replacement, LRU menghasilkan page fault yang lebih sedikit dibanding FIFO untuk dataset tertentu.

-Struktur modular memudahkan pengembangan dan pengujian setiap algoritma secara terpisah.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)

-Penjadwalan CPU memengaruhi kinerja sistem, terutama waktu tunggu dan keadilan antar proses.

-Manajemen memori dan container memungkinkan proses berjalan stabil melalui isolasi dan pembatasan sumber daya.

-Integrasi scheduling, memori, dan container meningkatkan efisiensi serta mencegah konflik penggunaan sumber daya

Proyek ini berhasil mengintegrasikan konsep CPU Scheduling dan Page Replacement dalam satu aplikasi terminal berbasis Docker. Melalui proyek ini, mahasiswa memperoleh pemahaman yang lebih praktis mengenai algoritma sistem operasi serta pengalaman kerja tim dan pengelolaan proyek perangkat lunak..


## Tugas
- Implementasikan proyek sesuai spesifikasi (minimal 2 modul).
- Sediakan dataset contoh dan dokumentasi run (code/README.md).
- Buat Dockerfile dan pastikan demo berjalan.
- Tulis laporan proyek pada laporan.md.
  
## Quiz
1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?
   
   **Jawaban:**
   
Tantangan terbesar yaitu menyatukan berbagai modul algoritma dalam satu aplikasi dengan alur input dan output yang konsisten. Solusinya iaalah menggunakan struktur modular dan satu file utama (main.py) sebagai pengatur alur program.

2. Mengapa Docker membantu proses demo dan penilaian proyek?  

   **Jawaban:**
   
Docker memastikan aplikasi berjalan di lingkungan yang sama tanpa bergantung pada konfigurasi sistem host, sehingga demo menjadi lebih stabil, reproducible, dan mudah dijalankan oleh dosen maupun asisten.

3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan.
   
   **Jawaban:**
Modul Page Replacement, khususnya algoritma LRU, akan lebih terdampak karena membutuhkan pencatatan dan pencarian riwayat akses halaman yang lebih kompleks dibanding FCFS atau FIFO.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  
   Kelompok kami hanya teridir dari 2 orang, 2 anomali yang lain tidak pernah berangkat (afk) selalu ada saja alasan nya yang ga masuk di akal.
- Bagaimana cara Anda mengatasinya?
  
    kami kick mereka ber 2, dari pada mereka hanya numpang nama saja, sekian curhatan dari kami ber 2 yang g jago2 bgt ngoding :)

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
