
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

a. open()
Kernel pertama kali menerima system call:
-cat meminta kernel membuka file /etc/passwd hanya untuk dibaca (O_RDONLY).
-Kernel memeriksa izin akses (permission) dan memastikan pengguna memiliki hak untuk membaca file tersebut.
-Jika sukses, kernel mengembalikan file descriptor bernilai 3, yang menjadi “pegangan” program untuk mengakses file di memori kernel.
b. read()
Baris berikut menunjukkan pemanggilan read() berkali-kali:
Artinya:
-cat meminta kernel membaca isi file sebanyak 4096 byte.
-Kernel membaca data dari disk ke buffer kernel, kemudian menyalurkannya ke buffer ruang user milik cat.
-Nilai 2996 menunjukkan bahwa hanya 2996 byte berhasil dibaca (artinya file lebih kecil dari 4 KB).
c. write()
Baris berikut muncul:
cat menulis hasil pembacaan ke file descriptor 1, yaitu stdout (layar terminal).
Kernel memastikan data dikirim ke perangkat output dengan benar.
d. close()
Akhirnya muncul:
Setelah selesai membaca, program cat menutup file dengan close().
Kernel melepaskan semua resource: file descriptor, buffer, dan entry di tabel file kernel

1. Konteks Eksperimen
menghasilkan dua lapisan output berbeda:
Output program biasa (cat /etc/passwd) → yaitu isi file /etc/passwd yang tampil di layar.
Output strace → yaitu log system call (aktivitas yang dilakukan kernel di balik layar).
2. Makna Log Kernel (Output strace)
Log dari strace bukan hasil program itu sendiri, melainkan hasil pemantauan aktivitas komunikasi antara aplikasi dan kernel.
Contohnya:
Artinya:
cat memanggil fungsi (system call) yang disediakan kernel.
Kernel kemudian menangani akses file, membaca isi, dan menyalurkannya ke layar.
strace hanya mengintip dan menampilkan log proses internal ini.
3. Makna Output Program Biasa
 output program biasa adalah hasil logis dari instruksi yang dijalankan oleh aplikasi dalam user mode.
Ini bukan aktivitas kernel, melainkan hasil akhir dari proses I/O setelah kernel menyalurkan data ke program cat.
Aplikasi cat hanya menampilkan isi file yang dibacanya dari kernel, tanpa tahu detail bagaimana kernel membukanya.
4. Perbedaan 
| Aspek       | `dmesg` (Log Kernel)                | Program biasa (contoh `cat`)            |
| ----------- | ----------------------------------- | --------------------------------------- |
| Sumber data | Kernel buffer (memori kernel)       | File sistem (user data)                 |
| Isi output  | Status, error, hardware, driver     | Konten file, hasil proses               |
| Mode utama  | Kernel mode (melalui system call)   | User mode                               |
| Tujuan      | Debugging sistem, monitoring kernel | Menampilkan data / menjalankan aplikasi |

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. System call ialah hubungan antara aplikasi (user mode) dan kernel (kernel mode),sehingga aplikasi bisa meminta layanan seperti akses perangkat keras.
2. Kernel adalah inti sistem operasi yang bertugas mengatur dan mengelola semua sumber daya sistem seperti memori dan CPU,serta mencegah knflik antar proses.
3. Praktikum menunjukkan bagaimana kernel dan system call bekerja sama dalam menjalankan aplikasi,memastikan aplikasi dapat berinteraksi dengan perangkat keras secara aman dan efisien.  

---
## Tugas
1. Dokumentasikan hasil eksperimen strace dan dmesg dalam bentuk tabel observasi.
- strace

| **No** | **Pesan Kernel (dmesg)** | **Makna / Penjelasan** | **Kategori Aktivitas Kernel** |
| ------ | ------------------------ | :--------------------- | :---------------------------- |
| 1 | `systemd-journald[43]: Collecting audit messages is disabled.` | Kernel mencatat bahwa fitur *audit logging* tidak diaktifkan. Ini berarti pesan audit sistem tidak sedang dikumpulkan. | Logging / Audit |
| 2 | `systemd-journald[43]: Received client request to flush runtime journal.` | Kernel menerima permintaan dari `systemd-journald` untuk menyimpan log runtime ke disk. | Manajemen Log Sistem |
| 3 | `systemd-journald[43]: File /var/log/journal/.../system.journal corrupted or uncleanly shut down, renaming and replacing.` | Kernel mendeteksi file jurnal yang rusak akibat shutdown tidak bersih, lalu menggantinya dengan file baru. | File System / Recovery |
| 4 | `ACPI: AC Adapter [AC1] (off-line)` | Kernel mendeteksi bahwa adaptor daya (charger) sedang tidak terhubung. | Power Management  |
| 5 | `ACPI: battery: Slot [BAT1] (battery present)` | Kernel mengenali adanya baterai yang aktif dan terpasang di sistem. | Power Management |
| 6 | `kvm_intel: Using Hyper-V Enlightened VMCS` | Kernel memuat modul `kvm_intel` untuk virtualisasi, menandakan sistem berjalan di lingkungan virtual (misalnya WSL atau Hyper-V). | Virtualization / CPU Management |
| 7 | `intel_rapl_ms: PL4 support detected.` | Kernel mendeteksi dukungan untuk fitur *Power Limit 4* pada prosesor Intel (pengaturan batas konsumsi daya). | CPU / Power Control |
| 8 | `systemd-journald[43]: /var/log/journal/.../user-1000.journal: Journal file uses a different sequence number ID, rotating.` | Kernel menandakan rotasi file log karena ID urutan log berbeda. Ini mekanisme keamanan agar log tidak rusak | Log Rotation / Maintenance |
| 9 | `WSL (239) ERROR: CheckConnection: getaddrinfo() failed: -5` | Pesan kesalahan dari lingkungan WSL (Windows Subsystem for Linux). Menunjukkan kegagalan dalam melakukan resolusi alamat jaringan.  | Networking / Virtual Environment |
| 10 | `TCP: eth0: Driver has suspect GRO implementation, TCP performance may be compromised.` | Kernel memberi peringatan bahwa driver jaringan `eth0` memiliki implementasi *Generic Receive Offload (GRO)* yang bermasalah, berpotensi menurunkan performa TCP. | Networking / Driver |

- dmesg

| **No** | **Pesan Kernel (dmesg)**                                                                                                    | **Makna / Penjelasan**                                                                                                                                            | **Kategori Aktivitas Kernel**    |
| :----: | :-------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
|    1   | `systemd-journald[43]: Collecting audit messages is disabled.`                                                              | Kernel mencatat bahwa fitur *audit logging* tidak diaktifkan. Ini berarti pesan audit sistem tidak sedang dikumpulkan.                                            | Logging / Audit                  |
|    2   | `systemd-journald[43]: Received client request to flush runtime journal.`                                                   | Kernel menerima permintaan dari `systemd-journald` untuk menyimpan log runtime ke disk.                                                                           | Manajemen Log Sistem             |
|    3   | `systemd-journald[43]: File /var/log/journal/.../system.journal corrupted or uncleanly shut down, renaming and replacing.`  | Kernel mendeteksi file jurnal yang rusak akibat shutdown tidak bersih, lalu menggantinya dengan file baru.                                                        | File System / Recovery           |
|    4   | `ACPI: AC Adapter [AC1] (off-line)`                                                                                         | Kernel mendeteksi bahwa adaptor daya (charger) sedang tidak terhubung.                                                                                            | Power Management                 |
|    5   | `ACPI: battery: Slot [BAT1] (battery present)`                                                                              | Kernel mengenali adanya baterai yang aktif dan terpasang di sistem.                                                                                               | Power Management                 |
|    6   | `kvm_intel: Using Hyper-V Enlightened VMCS`                                                                                 | Kernel memuat modul `kvm_intel` untuk virtualisasi, menandakan sistem berjalan di lingkungan virtual (misalnya WSL atau Hyper-V).                                 | Virtualization / CPU Management  |
|    7   | `intel_rapl_ms: PL4 support detected.`                                                                                      | Kernel mendeteksi dukungan untuk fitur *Power Limit 4* pada prosesor Intel (pengaturan batas konsumsi daya).                                                      | CPU / Power Control              |
|    8   | `systemd-journald[43]: /var/log/journal/.../user-1000.journal: Journal file uses a different sequence number ID, rotating.` | Kernel menandakan rotasi file log karena ID urutan log berbeda. Ini mekanisme keamanan agar log tidak rusak.                                                      | Log Rotation / Maintenance       |
|    9   | `WSL (239) ERROR: CheckConnection: getaddrinfo() failed: -5`                                                                | Pesan kesalahan dari lingkungan WSL (Windows Subsystem for Linux). Menunjukkan kegagalan dalam melakukan resolusi alamat jaringan.                                | Networking / Virtual Environment |
|   10   | `TCP: eth0: Driver has suspect GRO implementation, TCP performance may be compromised.`                                     | Kernel memberi peringatan bahwa driver jaringan `eth0` memiliki implementasi *Generic Receive Offload (GRO)* yang bermasalah, berpotensi menurunkan performa TCP. | Networking / Driver              |

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
- Apa bagian yang paling menantang minggu ini?  masih bingung cara mengerjakannya 
- Bagaimana cara Anda mengatasinya?  melihat tutorial di sosmed atau minta bantuan teman untuk mengajarinya

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
