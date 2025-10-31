![WhatsApp Image 2025-10-29 at 11 08 08](https://github.com/user-attachments/assets/ec612d69-b873-47c6-a326-81c8b191bc5f)
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux




---

## Identitas
- **Nama**  : RIZKI FADIL MYUBAROK  
- **NIM**   : 250202925 
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.  

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari peoses user


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```

---

## Hasil Eksekusi

<img width="1919" height="1079" alt="Screenshot 2025-10-31 143719" src="https://github.com/user-attachments/assets/83aa26be-3c06-46ec-b714-94851cfae898" />

<img width="1919" height="1079" alt="Screenshot 2025-10-31 143729" src="https://github.com/user-attachments/assets/3acd4908-8975-4f83-a466-6c4723b27f38" />

<img width="1919" height="1079" alt="Screenshot 2025-10-31 143740" src="https://github.com/user-attachments/assets/41cf8cae-972a-470b-996d-a496044a2b69" />


---

## Analisis
- Eksperimen 1 : - Jelaskan setiap output dan fungsinya. (whoami,id,groups)
- eksperimen 2 : - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND. 
- eksperimen 3 : - Catat PID proses `sleep`. 
- eksperimen 4 : - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  

**JAWABAN**

**eksperimen 1 :**
- whoami
Fungsi:
Menampilkan nama pengguna (username) yang sedang aktif atau login di sistem.

Contoh: whoami
`rizky`

Penjelasan output:Output rizky menunjukkan bahwa pengguna yang sedang menjalankan perintah saat ini bernama rizky.

2. id

Fungsi:
Menampilkan informasi identitas pengguna secara lengkap, termasuk:
- UID (User ID)
- GID (Group ID)
- Grup tambahan (secondary groups)

Contoh: id
`uid=1000(rizky) gid=1000(rizky) groups=1000(rizky),27(sudo),120(docker)`


Penjelasan output:
- uid=1000(rizky) → ID unik pengguna rizky
- gid=1000(rizky) → ID grup utama pengguna
- groups=... → daftar grup lain yang diikuti oleh pengguna
- Misal sudo artinya user punya hak administratif (superuser privileges).

3. groups

Fungsi:
Menampilkan daftar nama grup yang diikuti oleh pengguna saat ini.

Contoh: groups
`rizky sudo docker`


Penjelasan output:
User rizky tergabung dalam grup:
- rizky → grup utama
- sudo → memberi izin menjalankan perintah administratif
- docker → memberi izin mengelola kontainer Docker


**eksperimen 2 :**
Kolom Proses (PID, USER, %CPU, %MEM, COMMAND): 

- PID → Identitas unik setiap proses yang berjalan.
- USER → Nama pengguna pemilik proses.
- %CPU → Persentase penggunaan prosesor oleh proses.
- %MEM → Persentase penggunaan RAM oleh proses.
- COMMAND → Nama atau path perintah yang dijalankan.

**eksperimen  3 :**
- fadil        405  0.0  0.0   3124  1664 pts/0    S    14:49   0:00 sleep 1000
- fadil        407  0.0  0.0   4088  1920 pts/0    S+   14:49   0:00 grep --color=auto sleep

**eksperimen 4:**
Identifikasi proses induk (init/systemd):
- systemd atau init adalah proses pertama yang dijalankan oleh kernel saat sistem Linux dinyalakan.
- PID-nya selalu 1 (systemd(1) atau init(1)).
- Semua proses lain di sistem berasal dari atau bercabang dari proses ini.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum proses user


---

## D. Tugas & Quiz
### Tugas
1. Dokumentasikan hasil semua perintah dan jelaskan fungsi tiap perintah.  
2. Gambarkan hierarki proses dalam bentuk diagram pohon (`pstree`) di laporan.  
3. Jelaskan hubungan antara user management dan keamanan sistem Linux.  
4. Upload laporan ke repositori Git tepat waktu.

**JAWABAN**
1). a. whoami

Menampilkan nama pengguna yang sedang aktif di terminal. Berguna untuk memastikan identitas user yang sedang login ke sistem.

b). id

Menampilkan informasi identitas lengkap pengguna, seperti UID, GID, dan grup yang diikuti.
Digunakan untuk mengetahui hak akses dan peran user dalam sistem.

c). groups

Menampilkan nama-nama grup tempat user tergabung. Bermanfaat untuk memeriksa hak akses tambahan yang diberikan melalui keanggotaan grup (misalnya sudo).

d). ps aux | head -10

Menampilkan 10 proses pertama yang sedang aktif di sistem beserta informasi detailnya. Digunakan untuk memantau proses dan sumber daya sistem (CPU, memori, user, dll.).

e). top -n 1

Menampilkan daftar proses aktif secara real-time dalam satu tampilan (tanpa pembaruan terus-menerus).
Berguna untuk melihat proses yang paling banyak memakai CPU atau memori.

f). sleep 1000 &

Menjalankan proses yang “tidur” selama 1000 detik di background. Menunjukkan bagaimana cara menjalankan proses tanpa mengganggu terminal utama.

g). ps aux | grep sleep

Menampilkan proses dengan nama “sleep” yang sedang berjalan. Digunakan untuk mencari proses tertentu berdasarkan kata kunci.

h). kill <PID>

Menghentikan (mengakhiri) proses berdasarkan nomor PID-nya. Digunakan untuk mengontrol atau mematikan proses yang tidak diperlukan atau bermasalah.

i). pstree -p | head -20

Menampilkan hierarki proses (parent–child) beserta PID, dibatasi 20 baris pertama. Memudahkan untuk melihat hubungan antara proses induk (systemd/init) dan proses anak.
 
2.
![WhatsApp Image 2025-10-29 at 11 08 08](https://github.com/user-attachments/assets/63e6d86e-780b-437e-b6bc-d62b34bc8412)

3. User management dan keamanan sistem Linux saling berkaitan erat.
Pengelolaan user yang baik — seperti pembatasan hak akses, penggunaan grup, serta pengaturan izin file — adalah fondasi utama keamanan Linux.
Tanpa manajemen pengguna yang tepat, sistem akan rentan terhadap akses tidak sah, kebocoran data, dan penyalahgunaan sumber daya

   


### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?  
2. Apa perbedaan antara `kill` dan `killall`?  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?


**JAWABAN**


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
