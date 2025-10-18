
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
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

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
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

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
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
