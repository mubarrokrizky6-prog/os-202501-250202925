
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux




---

## Identitas
- **Nama**  : RIZKI FADIL MYUBAROK  
- **NIM**   : 250202925 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
mahasiswa mampu :
-Menjelaskan konsep proses dan user dalam sistem operasi Linux.
-Menampilkan daftar proses yang sedang berjalan dan statusnya.
-Menggunakan perintah untuk membuat dan mengelola user.
-Menghentikan atau mengontrol proses tertentu menggunakan PID.
-Menjelaskan kaitan antara manajemen user dan keamanan sistem.



---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
a. Proses adalah program yang sedang dieksekusi dan dikelola oleh kernel melalui PID.
b. Kernel bertugas membuat, menjalankan, menjadwalkan, dan menghentikan proses dengan bantuan system call.
c.Linux bersifat multiuser, maksudnya banyak pengguna dapat mengakses sistem secara bersamaan dengan hak akses berbeda.
d. User dan grup memiliki UID dan GID untuk mengatur izin terhadap file, proses, dan sumber daya sistem.
e.System call menjadi penghubung antara perintah user dengan pengelolaan proses dan user di tingkat kernel.

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
 Hasil percobaan menunjukkan bahwa Linux mampu mengelola proses dan pengguna dengan baik melalui perintah sistem. Setiap proses dikendalikan oleh kernel,           sedangkan pengaturan user dan hak akses menunjukkan penerapan keamanan dan manajemen sumber daya sesuai teori sistem operasi. 
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
Hasil percobaan sesuai dengan teori bahwa kernel berfungsi sebagai pengendali utama proses dan user di sistem operasi. Saat perintah dijalankan, Linux menggunakan system call untuk berkomunikasi antara program (user space) dan kernel (kernel space). Hal ini menunjukkan bahwa arsitektur OS bekerja secara berlapis — pengguna memberi perintah melalui shell, kernel memprosesnya, lalu hasil dikembalikan ke pengguna. percobaan membuktikan peran kernel dan system call dalam mengatur proses, hak akses, serta sumber daya sistem.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
Pada Linux, manajemen proses dan user dilakukan melalui perintah terminal dan berbasis hak akses (root dan user biasa), sedangkan Windowslebih banyak menggunakan antarmuka grafis dan akun administrator. Linux menampilkan detail proses dengan perintah seperti `ps`, `top`, atau `kill`, sedangkan Windows menggunakan Task Manager atau perintah `tasklist`. Selain itu, Linux lebih transparan terhadap system call dan struktur kernel, sedangkan Windows menyembunyikan banyak proses sistem demi keamanan dan kemudahan pengguna.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
-Kernel Linux berperan penting dalam mengatur proses, mulai dari pembuatan hingga penghentian, agar sistem berjalan stabil dan efisien.
-Sistem multiuser Linux memungkinkan pengaturan hak akses yang berbeda untuk tiap pengguna demi keamanan dan kontrol sistem.
-Perintah dan system call pada Linux menunjukkan bagaimana interaksi antara user mode dan kernel mode terjadi dalam pengelolaan proses serta user.


---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux?  
   **Jawaban:**  init atau systemd berfungsi sebagai pengendali utama proses dan layanan di Linux, yang memastikan sistem dapat berjalan dan dikelola dengan benar sejak awal booting.
2. Apa perbedaan antara kill dan killall?
   **Jawaban:**
   -kill digunakan jika kamu tahu PID proses yang ingin dihentikan.
   -killall digunakan jika kamu tahu nama programnya, bukan PID-nya.
   -kill menghentikan satu proses berdasarkan PID, sedangkan killall menghentikan semua proses dengan nama tertentu.
4. Mengapa user root memiliki hak istimewa di sistem Linux? 
   **Jawaban:**  User root memiliki hak istimewa karena berperan sebagai pengelola utama sistem Linux, yang bertanggung jawab atas pengaturan, keamanan, dan pemeliharaan seluruh sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
