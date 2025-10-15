
# Laporan Praktikum Minggu 1
Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Rizki fadil mubarok  
- **NIM**   : 250202925 
- **Kelas** : 1IKRA

---

## Tujuan  
Supaya mahasiswa mampu memahami konsep dasar sistem opereasi dan kernel,seperti menejemen memori,manjemen proses
dan menejemen perangkat keras,serta mampu mengimplementasikan dan menguji fungsionalitasnya
---

## Dasar Teori
-basis data berfokus pada pengelolaan data terstruktur untuk disimpan,diakses,dan dikelola secara efisien,sementara teori kernel berpusat pada inti sistem       operasi yang mengelola sumber daya perangkat keras dan menyediakan layanan dasar untuk program aplikas
-kernel berfokus pada pemahaman dan interaksi dengan proses,memori,dan perangkat keras sistem
- Basis data adalah kumpulan data yang terintegrasi,saling berhubungan,dan tersimpan secara digital untuk memberikan informasi saat dibutuhkan. 
  Kernel ialah inti dari sistem operasi yang mengelola semua sumber daya perangkat keras seperti CPU,memori,dan perangkat input/output.
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
<img width="1920" height="1020" alt="fadil@LAPTOP-F8F6U5EV_ _mnt_c_Users_FADIL 10_10_2025 14_49_01" src="https://github.com/user-attachments/assets/0ae6c232-9dff-4ad2-abea-cd1dfe631665" />


---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

1. Makna hasil percobaan
a. uname -a

Menampilkan informasi kernel dan sistem operasi:

Linux LAPTOP-F8F6U5EV 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun 5 18:30:46 UTC 2025 x86_64 GNU/Linux


 Makna:

Sistem operasi: Linux

Kernel: versi 6.6.87.2-microsoft-standard-WSL2 (berarti dijalankan di Windows Subsystem for Linux versi 2)

Arsitektur: x86_64 (64-bit)

PREEMPT_DYNAMIC: kernel mendukung preemption dinamis (memungkinkan penjadwalan thread real-time lebih responsif).

b. lsmod | head

Menampilkan daftar modul kernel (driver) yang sedang aktif:

tls, intel_rapl_msr, intel_rapl_common, kvm_intel, kvm, irqbypass, ...


 Makna:

kvm_intel & kvm: kernel module untuk virtualisasi (KVM = Kernel-based Virtual Machine).

intel_rapl_*: pengaturan power management untuk CPU Intel.

tls: mendukung Thread Local Storage, fitur sinkronisasi thread di kernel.

Ini menunjukkan kernel di WSL2 tetap memuat modul yang mirip dengan kernel Linux biasa (meski dijalankan di atas Windows).

c. dmesg | head

Menampilkan log awal kernel (boot message):

Linux version 6.6.87.2-microsoft-standard-WSL2 ...
Command line: ... WSL_ROOT_INIT=1 ...
KERNEL supported cpus: Intel GenuineIntel, AMD AuthenticAMD


 Makna:

Kernel yang digunakan berasal dari Microsoft WSL2 (bukan kernel Linux murni, tapi modifikasi dari Microsoft).

Ada parameter WSL_ROOT_INIT → kernel ini disesuaikan agar bisa berjalan tanpa BIOS/bootloader tradisional, karena WSL2 dijalankan sebagai virtual machine ringan di atas Windows.

nr_cpus=12 → kernel mendeteksi 12 logical CPU.

Bagian “BIOS-e820” menunjukkan peta memori (RAM map) yang diinisialisasi kernel.
. Fungsi Kernel dan Kaitannya dengan Hasil

2. Hasil Teori
Kernel adalah inti dari sistem operasi yang bertugas mengatur sumber daya komputer (CPU, memori, perangkat I/O) dan menyediakan layanan dasar bagi aplikasi.
Fungsi utama kernel meliputi:

Manajemen proses (penjadwalan, pembuatan, dan penghentian proses)

Manajemen memori (alokasi dan proteksi memori)

Manajemen perangkat keras (melalui driver)

Manajemen file system

Menjembatani komunikasi antara user space dan hardware

🔹 Kaitannya dengan hasil percobaan:

Perintah uname -a menampilkan versi dan tipe kernel yang digunakan:

Linux 6.6.87.2-microsoft-standard-WSL2 ...
Ini membuktikan bahwa kernel aktif di sistem kamu adalah Linux kernel yang telah dimodifikasi Microsoft untuk WSL2.

Perintah lsmod menunjukkan daftar modul kernel (driver) yang dimuat seperti kvm_intel, tls, ac.
→ Ini menggambarkan fungsi kernel dalam manajemen perangkat keras. Modul-modul tersebut berfungsi seperti “plugin” yang membuat kernel dapat berinteraksi dengan CPU dan perangkat lainnya.

Perintah dmesg menampilkan log kernel saat proses inisialisasi sistem.
→ Ini menunjukkan bagaimana kernel bekerja sejak awal boot untuk mengatur memori, CPU, dan sistem virtualisasi.

Intinya: hasil percobaan menggambarkan peran kernel sebagai “otak” OS yang menginisialisasi, mengatur, dan mengendalikan seluruh komponen sistem.

 2. System Call dan Kaitannya dengan Hasil

🔹 Teori:
System call adalah antarmuka antara program di user space dan kernel space.
Program biasa tidak bisa langsung mengakses perangkat keras, sehingga mereka harus memanggil system call agar kernel yang melakukannya.

Contoh system call di Linux:
open(), read(), write(), fork(), execve(), ioctl(), dll.

🔹 Kaitannya dengan hasil percobaan:

Saat kamu mengetik perintah seperti lsmod atau dmesg, shell (bash) memanggil beberapa system call:

open() → membuka file di /proc/modules (untuk menampilkan modul kernel)

read() → membaca isi file sistem kernel

write() dan printf() → menampilkan hasil ke layar

Kernel menjawab permintaan itu dan mengembalikan data ke program di user space.
Jadi perintah-perintah ini adalah contoh nyata penggunaan system call untuk berinteraksi dengan kernel.

Intinya: hasil percobaan membuktikan bahwa komunikasi antara user space (bash/terminal) dan kernel (Linux di WSL2) berjalan melalui system call interface.

 3. Arsitektur Sistem Operasi dan Kaitannya dengan Hasil

🔹 Teori:
Arsitektur OS modern biasanya dibagi dua bagian besar:

User Space: tempat program dan aplikasi berjalan.

Kernel Space: tempat kernel bekerja (melindungi hardware dan sumber daya sistem).

Jenis arsitektur kernel:

Monolithic kernel (seperti Linux): semua fungsi inti (driver, manajemen proses, sistem file) dijalankan di satu ruang kernel.

Microkernel: hanya fungsi minimal di kernel; layanan lainnya di user space.

🔹 Kaitannya dengan hasil:
Kernel yang digunakan (6.6.87.2-microsoft-standard-WSL2) berbasis Linux monolithic kernel, sehingga seluruh modul (kvm_intel, irqbypass, dll) bekerja langsung di ruang kernel.Namun, karena dijalankan di WSL2, kernel Linux ini berjalan di atas Hyper-V (virtualisasi Windows).

3.Perbedaan Linux dan Windows
Perbedaan utama antara Linux dan Windows yang memengaruhi hasil:

Arsitektur dan Kernel: Linux adalah open-source dan Unix-like, sedangkan Windows adalah proprietary dari Microsoft. Ini memengaruhi bagaimana sistem menangani proses, file, dan keamanan.
File System: Linux menggunakan case-sensitive file systems (seperti ext4), sedangkan Windows biasanya case-insensitive (NTFS). Ini bisa mengubah bagaimana program menangani nama file.
Path dan Direktori: Di Linux, path dimulai dengan '/', dan menggunakan '/' sebagai pemisah. Di Windows, path dimulai dengan drive letter seperti 'C:', dan menggunakan '' sebagai pemisah.
Eksekusi Program: Eksekusi file .exe di Windows versus file executable di Linux (tanpa ekstensi). Skrip shell seperti bash di Linux vs batch atau PowerShell di Windows.
Dependensi dan Library: Linux sering menggunakan shared libraries (.so), sedangkan Windows menggunakan DLL. Ini bisa menyebabkan masalah kompatibilitas.
Lingkungan Pengguna: Variabel lingkungan, hak akses, dan perilaku default berbeda.
Output dan Debugging: Output dari perintah atau program mungkin berbeda karena perbedaan dalam shell atau interpreter.

---

## Kesimpulan
-Praktikum ini membantu memahami arsitektur dasar,seperti struktur data yang digunakan,manajemen memori,penjadwalan proses,dan sistem file,yang memungkinkan   perangkat lunak berjalan secara efisien di atas hardware.
-Pengalaman langsung dalam praktikum meningkatkan pemahaman konsep-konsep abstrak 
-mahasiswa dapat untuk memecahkan masalah nyata terkait kinerja sistem dan penanganan data.


---

## Quiz
1. Sebutkan tiga fungsi utama sistem operaasi 
   Jawaban: - Menjalankan operasi dasar fungsi utama dari sistem operasi
            - Mengatur kerja hardware dan software
            - Mengkoordinasi kerja perangkat komputer
3. Jelaskan perbedaan antara kernel dan user mode   
   Jawaban: karnel adalah keamanan yang diatur oleh system itu sendiri
            sedangkn user mode adalah keamanan yang diatur penggunanya atau orang yang mengatur
5. sebutkan contoh OS dengan arsitektur monolithic dan microkernel  
   Jawaban: contoh OS dengan arsitektur monolothic adalah Linux,unix(FreeBSD)
            sedangkan contoh microkernel adalah QNX dan L4

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
   Yang menantang bagi saya untuk minggu ini adalah meng coding-coding,karena sebelumnya saya
   blm pernah sama sekali coding-coding,di samping itu sy juga jarang pegang laptop  
- Bagaimana cara Anda mengatasinya?
  cara mengatasinya ialah dengan meminta tolong kepada teman yang sejurusan,bagamana caranya menggunakan web git,bagaimana cara push,dan upload tugas
  supoaya saya kedepanya bisa paham dan bisa melakukanya mandiri

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
