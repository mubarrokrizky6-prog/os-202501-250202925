
# Laporan Praktikum Minggu [X]
Topik:  Penjadwalan CPU – FCFS dan SJF



---

## Identitas
- **Nama**  : RIZKI FADIL MUBAROK 
- **NIM**   : 250202925 
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori
*Tuliskan ringkasan teori (3–5 poin) yang mendasari Scheduling FCFS dan SJF

**jawaban**
Ringkasan teori yang mendasari algoritma Scheduling FCFS dan SJF:

1. Penjadwalan CPU bertujuan mengatur urutan eksekusi proses agar penggunaan CPU efisien dan waktu tunggu rata-rata minimal.
2. FCFS (First Come, First Served) mengeksekusi proses berdasarkan urutan kedatangan tanpa memperhatikan lama waktu eksekusi.
3. SJF (Shortest Job First) mengeksekusi proses dengan waktu eksekusi paling pendek terlebih dahulu untuk meminimalkan waktu tunggu rata-rata.
4. FCFS bersifat non-preemptive, sedangkan SJF dapat bersifat non-preemptive maupun preemptive (Shortest Remaining Time First).
5. Pemilihan algoritma yang tepat bergantung pada karakteristik sistem dan tujuan efisiensi, keadilan, serta waktu respons yang diinginkan.


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time. 

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| P1 | 6 | 0 | 0 | 6 | 0 | 6 |
| P2 | 8 | 1 | 6 | 14 | 5 | 13 |
| P3 | 7 | 2 | 14 | 21 | 12 | 19 |
| P4 | 3 | 3 | 21 | 24 | 18 | 21 |

   rata-rata Waiting Time (WT) = 8,75

   rata-rata Turnaround Time (TAT) = 14,75

   Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    14   21   24





   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  

| Proses | Burst Time | Arrival Time | Star Time | Finis Time |WT | TAT|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| P4 | 3 | 3 | 3 | 6 | 0 | 3 |
| P1 | 6 | 0 | 6  | 12  | 6  |  12 |
| P3 | 7 | 2 | 12 | 19 | 10 | 17 |
| P2 | 8 | 1 | 19  | 27 | 18  | 26 |
   
   rata-rata Waiting Time (WT) = 8,5

   rata-rata Turnaround Time (TAT) = 14,5

Gantt Chart:

    | P1 | P2 | P3 | P4 |
     0    6    12   19   27

   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

   | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
   |------------|------------------|----------------------|------------|-------------|
   | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
   | SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |


4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - *Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```
---

## Hasil Eksekusi

---

## Analisis
 - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
- *Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
- Tambahkan kesimpulan singkat di akhir laporan.

**jawaban**
1. RATA RATA  FCFS 
- rata-rata Waiting Time (WT) = 8,75
- rata-rata Turnaround Time (TAT) = 14,75

RATA RATA FJS
- rata-rata Waiting Time (WT) = 8,5
- rata-rata Turnaround Time (TAT) = 14,5

2. SJF lebih unggul dari FCFS ketika sistem memiliki proses dengan waktu eksekusi yang bervariasi dan waktu eksekusi setiap proses dapat diperkirakan. Dalam kondisi ini, SJF dapat meminimalkan waktu tunggu rata-rata karena proses yang lebih cepat diselesaikan terlebih dahulu.

Sebaliknya, FCFS lebih unggul dari SJF ketika semua proses memiliki waktu eksekusi yang hampir sama atau ketika waktu eksekusi proses tidak diketahui sebelumnya. FCFS juga lebih sesuai untuk sistem yang mengutamakan keadilan dan kesederhanaan, karena setiap proses dieksekusi sesuai urutan kedatangannya tanpa memperhatikan durasi.

---

## Kesimpulan
Algoritma FCFS lebih sederhana dan adil karena proses dieksekusi berdasarkan urutan kedatangan, namun dapat menyebabkan waktu tunggu tinggi jika ada proses dengan burst time besar di awal (efek “convoy”).

Algoritma SJF lebih efisien karena meminimalkan rata-rata waktu tunggu dengan mengeksekusi proses berdurasi pendek terlebih dahulu.

Namun, SJF sulit diterapkan pada sistem nyata karena memerlukan perkiraan waktu eksekusi proses dan dapat menyebabkan proses panjang mengalami kelaparan (starvation).

---

## D. Tugas & Quiz
### Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
4. Simpan seluruh hasil dan analisis ke `laporan.md`. 

**jawaban**
1. 



2. 

   | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
   |------------|------------------|----------------------|------------|-------------|
   | FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
   | SJF | 8,5 | 14,5 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

3. Berikut analisis kelebihan dan kelemahan tiap algoritma penjadwalan CPU:

a. FCFS (First Come, First Served)

    Kelebihan:

     - Sederhana dan mudah diterapkan.
     - Adil karena berdasarkan urutan kedatangan.
    Kelemahan:

     -Dapat menyebabkan proses cepat menunggu lama (convoy effect).
     -Tidak efisien dalam waktu tunggu rata-rata.

b. SJF (Shortest Job First)

    Kelebihan:

     -Menghasilkan waktu tunggu rata-rata paling kecil.
      -Efisien untuk sistem batch yang mengetahui waktu proses sebelumnya.
    Kelemahan:

     - Sulit diterapkan karena waktu eksekusi tidak selalu diketahui.
     - Dapat menyebabkan starvation untuk proses yang lama.

c. Priority Scheduling

    Kelebihan:

     - Dapat mengatur urutan proses berdasarkan tingkat kepentingan.
     - Cocok untuk sistem real-time.
    Kelemahan:

     - Proses berprioritas rendah bisa tertunda lama (starvation).
     - Membutuhkan mekanisme aging untuk menjaga keadilan.

d. Round Robin (RR)

   Kelebihan:

     - Memberikan kesempatan yang sama untuk semua proses.
     - Cocok untuk sistem interaktif karena waktu respons cepat.
    Kelemahan:

     - Terjadi banyak pergantian konteks jika waktu quantum terlalu kecil.
     - Tidak efisien untuk proses dengan durasi sangat pendek atau sangat panjang.

e. Multilevel Queue

    Kelebihan:

     - Dapat memisahkan proses berdasarkan kategori (interaktif, batch, dsb).
     -Dapat menggunakan kebijakan penjadwalan berbeda di tiap antrian.
    Kelemahan:

     -Kurang fleksibel karena proses tidak bisa berpindah antar antrian.
     - Kompleks dalam pengaturan prioritas antar antrian.





### Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa perbedaan utama antara FCFS dan SJF?  
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  

**jawaban**
1.-FCFS mengeksekusi proses berdasarkan urutan kedatangan, sehingga lebih sederhana namun dapat menyebabkan proses lama membuat proses lain menunggu.
- SJF mengeksekusi proses dengan waktu eksekusi paling pendek terlebih dahulu, sehingga lebih efisien dalam waktu tunggu, tetapi kurang adil karena proses panjang bisa tertunda dan memerlukan informasi waktu eksekusi sebelumnya.

2.SJF dapat menghasilkan rata-rata waktu    tunggu minimum karena algoritma ini selalu mengeksekusi proses dengan waktu eksekusi paling pendek terlebih dahulu. Dengan cara ini, proses-proses cepat segera selesai dan tidak tertahan oleh proses yang lebih lama.

3.Kelemahan SJF jika diterapkan pada sistem interaktif adalah:

a. Sulit mengetahui waktu eksekusi proses      sebelumnya karena pada sistem interaktif lama waktu setiap proses tidak dapat diprediksi dengan pasti.

b. Proses yang memiliki waktu eksekusi panjang bisa tertunda terus-menerus (starvation) karena proses pendek selalu didahulukan.

c. Kurang responsif terhadap perubahan prioritas, padahal sistem interaktif membutuhkan respons cepat terhadap input pengguna.

Akibatnya, SJF tidak cocok digunakan pada sistem interaktif yang membutuhkan keadilan dan waktu tanggap cepat.






---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
