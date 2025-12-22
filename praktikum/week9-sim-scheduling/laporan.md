
# Laporan Praktikum Minggu IX
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : RIZKI FADIL MUBAROK 
- **NIM**   : 250202925  
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Setelah menyelesaikan tugas ini, mahasiswa mampu:

Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
Menyajikan output simulasi dalam bentuk tabel atau grafik.
Menjelaskan hasil simulasi secara tertulis.
Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan Simulasi Algoritma Penjadwalan CPU

Ringkasan Teori Simulasi Algoritma Penjadwalan CPU:

-Penjadwalan CPU bertujuan mengatur urutan eksekusi proses agar penggunaan CPU efisien dan adil.
-Algoritma penjadwalan (FCFS, SJF, Priority, Round Robin) memiliki karakteristik dan kinerja berbeda.
-Simulasi digunakan untuk mengevaluasi algoritma tanpa mengganggu sistem nyata.
-Parameter utama yang dianalisis meliputi waiting time, turnaround time, dan response time.
-Perbandingan hasil simulasi membantu menentukan algoritma yang paling sesuai dengan kondisi beban sistem.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```


---

## Hasil Eksekusi
<img width="1919" height="1079" alt="Screenshot 2025-12-22 101046" src="https://github.com/user-attachments/assets/1849fed7-17e7-46fe-906d-12d99a997d5d" />

![HASIL SS](<screenshots/Screenshot 2025-12-22 101105.png>)


---

## Analisis
- Jelaskan makna hasil percobaan Simulasi Algoritma Penjadwalan CPU

 **Makna hasil percobaan Simulasi Algoritma Penjadwalan CPU adalah** menunjukkan bagaimana setiap algoritma penjadwalan memengaruhi kinerja sistem. Dari hasil    simulasi dapat diketahui perbedaan nilai waiting time, turnaround time, dan response time antar algoritma, sehingga terlihat algoritma mana yang lebih efisien, lebih adil, atau lebih cocok untuk kondisi beban tertentu. Hasil percobaan ini membantu memahami bahwa tidak ada satu algoritma yang paling baik untuk semua situasi, melainkan harus dipilih sesuai kebutuhan sistem.
 
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).

**- Fungsi Kernel**
Kernel berperan sebagai inti sistem operasi yang mengatur penjadwalan CPU. Hasil simulasi menunjukkan bahwa keputusan kernel dalam memilih proses (berdasarkan algoritma penjadwalan) secara langsung memengaruhi waiting time dan turnaround time.

**System Call**
System call menjadi penghubung antara proses dan kernel. Saat proses meminta layanan CPU atau melakukan operasi I/O, system call memicu kernel untuk melakukan penjadwalan ulang, yang tercermin dalam hasil simulasi.

**Arsitektur Sistem Operasi**
Dalam arsitektur OS, modul penjadwalan CPU bekerja bersama manajemen proses dan sumber daya. Hasil simulasi menggambarkan bagaimana komponen-komponen tersebut saling berkoordinasi untuk mencapai efisiensi dan keadilan dalam penggunaan CPU.
  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?

-Perbedaan hasil simulasi Algoritma Penjadwalan CPU di lingkungan OS yang berbeda (Linux dan Windows) umumnya terlihat pada cara penjadwalan diimplementasikan, meskipun konsep dasarnya sama.
-Algoritma Penjadwalan
Linux menggunakan scheduler seperti Completely Fair Scheduler (CFS) yang menekankan keadilan waktu CPU, sedangkan Windows memakai priority-based preemptive scheduling. Akibatnya, pembagian waktu CPU dan respons proses bisa berbeda.
-Manajemen Prioritas
Linux lebih fleksibel dalam pengaturan prioritas proses, sementara Windows memiliki kelas prioritas yang lebih ketat. Hal ini memengaruhi waiting time dan response time.
-Hasil Kinerja
Dengan beban proses yang sama, Linux cenderung menghasilkan pembagian CPU yang lebih merata, sedangkan Windows lebih cepat merespons proses berprioritas tinggi.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum Simulasi Algoritma Penjadwalan CPU

1. Setiap algoritma penjadwalan CPU memiliki kelebihan dan kekurangan yang memengaruhi nilai waiting time dan turnaround time.
2. Simulasi memudahkan analisis dan perbandingan kinerja algoritma secara akurat dan efisien.
3. Pemilihan algoritma penjadwalan harus disesuaikan dengan karakteristik beban proses dan tujuan sistem.


---
**Tugas**
1. Buat program simulasi FCFS atau SJF.
2. Jalankan program dengan dataset uji.
3. Sajikan output dalam tabel atau grafik.
4. Tulis laporan praktikum pada laporan.md.
## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling? 
   **Jawaban:**
 **karena beberapa alasan penting berikut:**
**Sulit diuji langsung di sistem nyata**
Menguji algoritma scheduling langsung pada sistem operasi nyata berisiko mengganggu kinerja sistem dan sulit dikontrol kondisinya (beban kerja, jumlah proses, waktu kedatangan).

**Lingkungan dapat dikendalikan**
Dengan simulasi, kita bisa mengatur parameter seperti arrival time, burst time, dan priority secara pasti sehingga hasil antar algoritma dapat dibandingkan secara adil.

**Untuk menghemat waktu dan biaya**
Simulasi tidak memerlukan perangkat keras khusus atau modifikasi sistem operasi, sehingga lebih efisien dan praktis.

**Mudah membandingkan performa**
Berbagai algoritma (FCFS, SJF, Priority, Round Robin, dll.) dapat diuji dengan data yang sama untuk melihat perbedaan waiting time, turnaround time, dan response time.

**Menganalisis skenario ekstrem**
Simulasi memungkinkan pengujian kondisi jarang terjadi, seperti beban sistem sangat tinggi atau proses dengan waktu eksekusi sangat panjang.

**Membantu pembelajaran dan pemahaman**
Dalam konteks akademik, simulasi memudahkan mahasiswa memahami cara kerja algoritma scheduling tanpa harus memahami keseluruhan sistem operasi.Sulit diuji langsung di sistem nyata
Menguji algoritma scheduling langsung pada sistem operasi nyata berisiko mengganggu kinerja sistem dan sulit dikontrol kondisinya (beban kerja, jumlah proses, waktu kedatangan).

**Lingkungan dapat dikendalikan**
Dengan simulasi, kita bisa mengatur parameter seperti arrival time, burst time, dan priority secara pasti sehingga hasil antar algoritma dapat dibandingkan secara adil.

**Menghemat waktu dan biaya**
Simulasi tidak memerlukan perangkat keras khusus atau modifikasi sistem operasi, sehingga lebih efisien dan praktis.

**Mudah membandingkan performa**
Berbagai algoritma (FCFS, SJF, Priority, Round Robin, dll.) dapat diuji dengan data yang sama untuk melihat perbedaan waiting time, turnaround time, dan response time.

**Menganalisis skenario yang ekstrem**
Simulasi memungkinkan pengujian kondisi jarang terjadi, seperti beban sistem sangat tinggi atau proses dengan waktu eksekusi sangat panjang.

**Membantu pembelajaran dan pemahaman**
Dalam konteks akademik, simulasi memudahkan mahasiswa memahami cara kerja algoritma scheduling tanpa harus memahami keseluruhan sistem operasi.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   **Jawaban:**

**Perhitungan manual**: lambat, rawan salah, tidak cocok untuk dataset besar.

**Simulasi**: cepat, akurat, konsisten, dan mampu menangani data besar.

3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
   **Jawaban:**  
**Algoritma yang paling mudah diimplementasikan adalah FCFS (First Come First Served).**
Penjelasan :
FCFS hanya menjalankan proses berdasarkan urutan kedatangan.
Tidak perlu perhitungan kompleks, sorting, atau preemption.
Cukup menggunakan queue (antrian) sederhana.

**Sebaliknya:**
**SJF perlu membandingkan burst time.**
**Priority perlu pengelolaan prioritas dan bisa terjadi starvation.**
**Round Robin perlu time quantum dan context switching lebih rumit.**
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Belum bisa mengerjakan mandiri sepenuhnya
- Bagaimana cara Anda mengatasinya?  kerja kelompok

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
