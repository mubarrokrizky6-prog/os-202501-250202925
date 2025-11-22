
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : RIZKI FADIL MUBAROK  
- **NIM**   : 250202925 
- **Kelas** : 1IKRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
mahasiswa mampu:
Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
Menyusun tabel hasil perhitungan dengan benar dan sistematis.
Membandingkan performa algoritma RR dan Priority.
Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

1. Penjadwalan CPU adalah mekanisme yang digunakan kernel untuk menentukan proses mana yang dieksekusi berikutnya agar pemanfaatan CPU maksimal dan respons sistem tetap baik.
2. Round Robin menggunakan time quantum untuk membagi waktu CPU secara merata kepada setiap proses, sehingga cocok untuk sistem interaktif dan time-sharing.
3. Priority Scheduling memilih proses berdasarkan tingkat prioritas sehingga proses penting dapat dijalankan lebih cepat, namun berpotensi menimbulkan starvation bagi proses berprioritas rendah.
4. Kedua algoritma bekerja melalui mekanisme context switching yang diatur oleh kernel, dan dipicu oleh interupsi timer atau kondisi tertentu yang menyebabkan proses melepaskan CPU.
5. Pemilihan algoritma penjadwalan mempengaruhi throughput, waktu tunggu, waktu respons, dan keadilan eksekusi proses dalam sistem operasi.

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
Tuliskan 2–3 poin kesimpulan dari praktikum Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

1. Round Robin memberikan keadilan karena setiap proses mendapat jatah waktu yang sama, namun performanya sangat dipengaruhi oleh ukuran time quantum.
2. Priority Scheduling mampu mengeksekusi proses penting lebih cepat, tetapi berpotensi menyebabkan starvation pada proses berprioritas rendah.
3. Pemilihan algoritma harus disesuaikan dengan kebutuhan: RR untuk sistem interaktif, sedangkan Priority untuk situasi yang membutuhkan pemrosesan berdasarkan tingkat kepentingan.


---
**Tugas**
1.Hitung waiting time dan turnaround time untuk algoritma RR dan Priority.
2.Sajikan hasil perhitungan dan Gantt Chart dalam laporan.md.
3.Bandingkan performa dan jelaskan pengaruh time quantum serta prioritas.
4.Simpan semua bukti (tabel, grafik, atau gambar) ke folder screenshots/.

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling? 
   **Jawaban:** 
-Round Robin: proses dieksekusi secara bergiliran dengan time quantum yang sama; adil dan cocok untuk sistem interaktif.
-Priority Scheduling: proses dipilih berdasarkan prioritas; bisa terjadi starvation pada proses prioritas rendah.

2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?
   **Jawaban:**
   Singkatnya:

* **Time quantum terlalu besar:**
  - Mirip FCFS, respons lambat, interaktivitas buruk.

* **Time quantum terlalu kecil:**
  - Terlalu sering *context switch*, overhead besar, performa menurun.

* **Time quantum ideal:**
  -Seimbang antara respons cepat dan overhead rendah.

3. Mengapa algoritma Priority dapat menyebabkan starvation?

   **Jawaban:**
   Algoritma Priority dapat menyebabkan starvation karena:
Proses dengan prioritas rendah bisa tidak pernah mendapat giliran jika selalu ada proses baru dengan prioritas lebih tinggi yang masuk.
Akibatnya, proses prioritas rendah terus tertunda dan bisa “kelaparan” (tidak dieksekusi dalam waktu sangat lama).


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  kurang paham,sampai kehabisan deatline
- Bagaimana cara Anda mengatasinya?  tanya tanya, cari tutor

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
