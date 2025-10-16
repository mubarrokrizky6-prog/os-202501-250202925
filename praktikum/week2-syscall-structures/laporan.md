
# Laporan Praktikum Minggu [X]
Topik: Struktur System Call dan Fungsi Kernel

---

## Identitas
- **Nama**  : Rizki fadil mubarok  
- **NIM**   : 250202925
- **Kelas** : 1KRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  Memahami interaksi aplikasi dan sistem operasi
        Mempelajari komunikasi antar ruang proses
        Mengamati manajemen sumber daya kernel

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1) System call adalah antarmuka yang memungkinkan aplikasi meminta layanan dari kernel
2) Kernel bertanggung jawab mengelola sumber daya sistem seperti memori dan CPU dengan izin istimewa
3) Proses pengguna harus memanggil system call untuk mengakses perangkat keras dan melakukan operasi terlarang

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


---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. System call ialah hubungan antara aplikasi (user mode) dan kernel (kernel mode),sehingga aplikasi bisa meminta layanan seperti akses perangkat keras.
2. Kernel adalah inti sistem operasi yang bertugas mengatur dan mengelola semua sumber daya sistem seperti memori dan CPU,serta mencegah knflik antar proses.
3. Praktikum menunjukkan bagaimana kernel dan system call bekerja sama dalam menjalankan aplikasi,memastikan aplikasi dapat berinteraksi dengan perangkat keras secara aman dan efisien.  

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
   **Jawaban:**  yaitu sebagai satuan antara program aplikasi dan kernel sistem operasi,memungkinkan program untuk meminta layanan dari sistem operasi.
2. Sebutkan 4 kategori system call yang umum digunakan.
   **Jawaban:**  Manajemen proses,manajemen file,manajemen perangkat,dan komunikasi
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   **Jawaban:** karena alasan keamanan dan integritas sistem 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  masih bingung cara mengerjakannya ;)
- Bagaimana cara Anda mengatasinya?  melihat tutorial di sosmed atau minta bantuan teman untuk mengajarinya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
