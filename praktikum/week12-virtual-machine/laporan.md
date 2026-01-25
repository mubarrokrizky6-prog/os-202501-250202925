
# Laporan Praktikum Minggu 12
Topik: Virtualisasi Menggunakan Virtual Machine 

---

## Identitas
- **Nama**  : RIZKI FADIL MUABAROK 
- **NIM**   : 250202925
- **Kelas** : 1IKRA

---

## Tujuan  
> Setelah menyelesaikan tugas ini, mahasiswa mampu:

Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
Membuat dan menjalankan sistem operasi guest di dalam VM.
Mengatur konfigurasi resource VM (CPU, RAM, storage).
Menjelaskan mekanisme proteksi OS melalui virtualisasi.
Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan Virtualisasi Menggunakan Virtual Machine

a. Virtualisasi adalah teknik yang memungkinkan satu perangkat keras fisik menjalankan beberapa sistem operasi secara bersamaan dengan bantuan hypervisor.
b. Hypervisor berfungsi sebagai lapisan pengelola yang mengatur akses Guest OS ke sumber daya hardware serta menjaga isolasi antar mesin virtual.
c. Mesin virtual (Virtual Machine) bertindak sebagai komputer virtual yang memiliki CPU, memori, dan storage virtual sendiri.
d. Konsep isolasi dalam virtualisasi meningkatkan keamanan dan stabilitas sistem karena gangguan pada satu VM tidak memengaruhi sistem lain.
e. Virtualisasi meningkatkan efisiensi penggunaan hardware dan memudahkan pengujian, pengembangan, serta pembelajaran sistem operasi.


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
- Jelaskan makna hasil percobaan Virtualisasi Menggunakan Virtual Machine
  - Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
 Kesimpulan Praktikum Virtualisasi Menggunakan Virtual Machine:
-Virtualisasi memungkinkan menjalankan beberapa sistem operasi secara bersamaan pada satu perangkat keras tanpa saling mengganggu karena adanya isolasi antar mesin virtual.
-Hypervisor berperan penting dalam mengelola dan membagi sumber daya hardware (CPU, RAM, dan storage) secara efisien kepada setiap mesin virtual.
-Penggunaan virtual machine meningkatkan keamanan dan fleksibilitas sistem, karena memudahkan pengujian, pemulihan (snapshot), dan pengelolaan sistem operasi tanpa memengaruhi sistem utama.


---
**##Tugas**
1. Instal dan jalankan OS guest menggunakan VM.
2. Konfigurasikan resource VM sesuai instruksi.
3. Dokumentasikan proses instalasi dan konfigurasi.
4. Tulis laporan praktikum pada laporan.md.


## Quiz
1. Apa perbedaan antara host OS dan guest OS? 
   **Jawaban:**
 1. Host OS
-Sistem operasi utama yang terpasang langsung pada perangkat keras (hardware).
-Mengelola sumber daya fisik seperti CPU, RAM, hard disk, dan perangkat I/O.
-Menjadi lingkungan induk tempat software virtualisasi dijalankan.

2. Guest OS
-Sistem operasi tamu yang dijalankan di dalam mesin virtual (virtual machine).
-Tidak berinteraksi langsung dengan hardware, tetapi melalui host OS atau hypervisor.
-Menggunakan sumber daya yang dialokasikan oleh host OS.
-Contoh: Linux Ubuntu yang dijalankan di VirtualBox pada Windows.

2. Apa peran hypervisor dalam virtualisasi?
   **Jawaban:**
a.  Mengelola sumber daya hardware
b.  Menjadi perantara antara hardware dan Guest OS
c.  Menjaga isolasi antar mesin virtual
d.  Mengatur siklus hidup mesin virtual
e.  Meningkatkan keamanan dan stabilitas sistem
 
3. Mengapa virtualisasi meningkatkan keamanan sistem? 
   **Jawaban:**
   Virtualisasi meningkatkan keamanan karena mengisolasi sistem, membatasi akses hardware, dan memudahkan pemulihan, sehingga risiko dan dampak serangan dapat        diminimalkan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Banyak ujian, cobaan, dan tantangan  
- Bagaimana cara Anda mengatasinya?  berusaha dan berdoa

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
