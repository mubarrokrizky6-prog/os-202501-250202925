
# Laporan Praktikum Minggu 2
Topik: Struktur System Call dan Fungsi Kernel

---

## Identitas
- **Nama**  : Rizki fadil mubarok  
- **NIM**   : 250202925
- **Kelas** : 1IKRA

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
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
<img width="1919" height="1079" alt="Screenshot 2025-10-17 131138" src="https://github.com/user-attachments/assets/2d5acd61-5735-46ed-b9e8-6ca1fbf71880" />
<img width="1919" height="1079" alt="Screenshot 2025-10-17 131149" src="https://github.com/user-attachments/assets/2470454c-6539-41eb-a3e1-1eeac86942fc" />
<img width="1919" height="1079" alt="Screenshot 2025-10-17 131241" src="https://github.com/user-attachments/assets/aae20fe2-f205-46cb-810e-4eb53ce6c384" />

---

## Analisis
- Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.
- Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

  
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
