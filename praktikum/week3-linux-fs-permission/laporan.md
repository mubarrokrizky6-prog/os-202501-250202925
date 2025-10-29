
# Laporan Praktikum Minggu 3
Topik: Manajemen File dan Permission di Linux



---

## Identitas
- **Nama**  : Rizki fadil mubarok
- **NIM**   : 250202925 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh: 
Mahasiswa mampu :
-Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
-Menggunakan chmod dan chown untuk manajemen hak akses file.
-Menjelaskan hasil output dari perintah Linux dasar.
-Menyusun laporan praktikum dengan struktur yang benar.
-Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
-Linux memakai sistem berkas hierarki dengan root / sebagai pusatnya.
-Setiap file punya izin read (r), write (w), dan execute (x) untuk owner, group, dan others.
-Manajemen file dilakukan dengan perintah seperti ls, cp, mv, rm, dan mkdir.
-Izin dan kepemilikan diatur dengan chmod, chown, dan chgrp.
-Permission berfungsi menjaga keamanan dan membatasi akses pengguna.



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
- Jelaskan makna hasil percobaan.
    Hasil percobaan menunjukkan bahwa Linux mengatur file dengan izin akses tertentu untuk menjaga            keamanan, dan izin serta kepemilikan file dapat diubah menggunakan perintah seperti chmod, chown,         dan chgrp. 
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
     Hasil percobaan berkaitan dengan teori karena kernel mengatur akses file melalui system call             seperti open(), read(), write(), dan chmod(). Saat pengguna menjalankan perintah manajemen file, OS      melalui kernel memeriksa izin (permission) sesuai arsitektur Linux yang memisahkan user mode dan         kernel mode, sehingga keamanan dan kontrol akses file tetap terjaga.
-    Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
     Perbedaannya, di Linux manajemen file dan permission diatur dengan sistem rwx (read, write,              execute) dan berbasis user–group–others, sedangkan di Windows menggunakan ACL (Access Control List)      yang lebih detail dan berbasis user account. Selain itu, Linux mengatur izin lewat command line dan      kernel,    sedangkan Windows lebih banyak melalui GUI (grafis).
---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
Kesimpulan praktikum Manajemen File dan Permission di Linux adalah:
(1) Terdapat tiga jenis hak akses dasar untuk file/direktori: read (baca), write (tulis), dan execute (eksekusi).
(2) Hak akses ini dibagi menjadi tiga kategori pemilik: owner (pemilik), group (kelompok), dan other (lainnya). 
(3) Perintah chmod digunakan untuk mengubah hak akses file, yang dapat dilakukan menggunakan notasi simbolik (misalnya, u+r) atau notasi oktal (misalnya, 755). 

---

## Quiz
1. Apa fungsi dari perintah chmod?
   **Jawaban:** Fungsi chmod ialah untuk mengubah mode akses atau izin pada berkas dan direktori di sistem operasi mirip Unix seperti Linux. 
2. Apa arti dari kode permission rwxr-xr--?
   **Jawaban:**  
3. Jelaskan perbedaan antara chown dan chmod.
   **Jawaban:** Perbedaannya ialah chmod mengubah izin (mode) file atau direktori (siapa yang dapat membaca,menulis,atau mengeksekusi),sedangkan chown mengubah kepemilikan file atau direktori (siapa pemiliknya dan grup pemiliknya). chmod adalah singkatan dari "change mode",sedangkan chown adalah singkatan dari "change owner".  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? belum paham materi  
- Bagaimana cara Anda mengatasinya? Berusaha dan belajar giat, pahami konsepnya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
