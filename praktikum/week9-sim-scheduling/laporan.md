
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
 a. Inisialisasi Dataset

```processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]
burst_time = [6, 8, 7, 3]
```

Menyimpan nama proses, arrival time (AT), dan burst time (BT).

Data sudah terurut berdasarkan waktu kedatangan → sesuai prinsip FCFS.

 b. Inisialisasi Variabel
```
start_time = [0] * n
finish_time = [0] * n
waiting_time = [0] * n
turnaround_time = [0] * n
```

Digunakan untuk menyimpan:
```
start_time → waktu mulai eksekusi

finish_time → waktu selesai eksekusi

waiting_time → waktu menunggu

turnaround_time → waktu total di sistem
```
 c. Proses Penjadwalan FCFS
```
for i in range(n):
```

Perulangan memproses setiap proses sesuai urutan kedatangan.

 Proses pertama
```
start_time[i] = arrival_time[i]
```

Karena CPU masih kosong, proses langsung dieksekusi.

 Proses berikutnya
```
start_time[i] = max(finish_time[i - 1], arrival_time[i])
```

Proses baru hanya bisa berjalan jika:

CPU sudah kosong, atau

proses sudah tiba

 d. Perhitungan Waktu
```
finish_time[i] = start_time[i] + burst_time[i]
waiting_time[i] = start_time[i] - arrival_time[i]
turnaround_time[i] = finish_time[i] - arrival_time[i]
```

Rumus FCFS:
```
WT = Start Time − Arrival Time

TAT = Finish Time − Arrival Time
```
 e. Perhitungan Rata-rata
```
avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n
```

Digunakan untuk evaluasi performa algoritma.

2️ Perbandingan Hasil Simulasi vs Perhitungan Manual
Hasil Simulasi Program

| Proses |  AT |  BT | Start | Finish |  WT | TAT |
| :----: | :-: | :-: | :---: | :----: | :-: | :-: |
|   P1   |  0  |  6  |   0   |    6   |  0  |  6  |
|   P2   |  1  |  8  |   6   |   14   |  5  |  13 |
|   P3   |  2  |  7  |   14  |   21   |  12 |  19 |
|   P4   |  3  |  3  |   21  |   24   |  18 |  21 |


Rata-rata Waiting Time = 8.75

Rata-rata Turnaround Time = 14.75

Hasil Perhitungan Manual

Hasil manual (dari Gantt Chart FCFS):

| P1 | P2 | P3 | P4 |
0    6    14   21   24


 Semua nilai WT dan TAT sama persis
 Artinya simulasi tervalidasi dan benar

3️ Kelebihan dan Keterbatasan Simulasi
 Kelebihan

Akurat dan konsisten
Hasil simulasi sesuai dengan teori dan perhitungan manual.

Otomatis dan efisien
Menghindari kesalahan hitung saat jumlah proses banyak.

Mudah dimodifikasi
Dataset dapat diubah untuk eksperimen lain.

Merepresentasikan konsep FCFS dengan jelas
Cocok untuk pembelajaran dasar penjadwalan CPU.

Keterbatasan

Tidak mendukung preemptive scheduling
Proses tidak bisa dipotong di tengah eksekusi.

Tidak mempertimbangkan context switching
Padahal di sistem nyata ada overhead waktu.

Rentan Convoy Effect
Proses panjang di awal membuat proses lain menunggu lama.

Belum mencerminkan sistem operasi nyata sepenuhnya
Kernel OS lebih kompleks (interrupt, I/O wait, multi-core).
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
