
# Laporan Praktikum Minggu [X]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : RIZKI FADIL MUBAROK  
- **NIM**   : 250202925
- **Kelas** : 1IKRA

---

## Tujuan
-Mengimplementasikan algoritma page replacement FIFO dalam program.
-Mengimplementasikan algoritma page replacement LRU dalam program.
-Menjalankan simulasi page replacement dengan dataset tertentu.
-Membandingkan performa FIFO dan LRU berdasarkan jumlah page fault.
-Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
Ringkasan Teori Manajemen Memori – Page Replacement (FIFO & LRU):
-Manajemen memori bertujuan mengatur penggunaan memori utama agar proses dapat berjalan secara efisien.
-Page replacement digunakan ketika terjadi page fault dan memori fisik sudah penuh.
-Algoritma FIFO mengganti halaman yang pertama kali masuk ke memori.
-Algoritma LRU mengganti halaman yang paling lama tidak digunakan.
-Kinerja algoritma diukur dari jumlah page fault yang terjadi.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
# Reference string dan jumlah frame
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames_count = 3


# ================= FIFO =================
def fifo_page_replacement(ref_string, frames_count):
    frames = []
    page_faults = 0

    print("=== FIFO Page Replacement ===")

    for page in ref_string:
        if page in frames:
            print(f"Page {page} -> HIT  | Frames: {frames}")
        else:
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)      # Hapus halaman paling awal
                frames.append(page)
            print(f"Page {page} -> FAULT| Frames: {frames}")

    print(f"\nTotal Page Fault (FIFO): {page_faults}")
    print("-" * 40)


# ================= LRU =================
def lru_page_replacement(ref_string, frames_count):
    frames = []
    page_faults = 0

    print("=== LRU Page Replacement ===")

    for page in ref_string:
        if page in frames:
            frames.remove(page)    # Update urutan penggunaan
            frames.append(page)
            print(f"Page {page} -> HIT  | Frames: {frames}")
        else:
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames.pop(0)      # Hapus halaman paling lama digunakan
                frames.append(page)
            print(f"Page {page} -> FAULT| Frames: {frames}")

    print(f"\nTotal Page Fault (LRU): {page_faults}")
    print("-" * 40)


# ================= Main =================
fifo_page_replacement(reference_string, frames_count)
lru_page_replacement(reference_string, frames_count)

---

## Hasil Eksekusi

<img width="1541" height="909" alt="Screenshot 2026-01-06 123223" src="https://github.com/user-attachments/assets/6c6354aa-d703-409c-851e-37deb4d80f9a" />

<img width="1264" height="815" alt="Screenshot 2026-01-06 123243" src="https://github.com/user-attachments/assets/069ab3d2-30a5-416c-8c33-8c1e85974729" />

---

## Analisis
5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

| Algoritma | Jumlah Page Fault | Keterangan                                                                                              |
| :-------- | :---------------: | :------------------------------------------------------------------------------------------------------ |
| **FIFO**  |       **10**      | Mengganti halaman berdasarkan urutan masuk pertama tanpa memperhatikan frekuensi atau waktu penggunaan. |
| **LRU**   |       **9**       | Mengganti halaman yang paling lama tidak digunakan sehingga lebih sesuai dengan pola akses program.     |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.

Perbedaan jumlah page fault terjadi karena strategi pemilihan halaman yang diganti berbeda:

FIFO tidak mempertimbangkan apakah halaman masih sering digunakan atau tidak, sehingga halaman penting bisa terhapus meskipun akan segera dipakai kembali.

LRU mempertimbangkan riwayat penggunaan halaman, sehingga halaman yang sering diakses akan dipertahankan lebih lama di memori.

Pola reference string memiliki locality of reference, yang lebih cocok ditangani oleh algoritma LRU dibanding FIFO.
  
   - Analisis algoritma mana yang lebih efisien dan alasannya.

Algoritma yang lebih efisien:  LRU

Alasannya:

LRU menghasilkan jumlah page fault lebih sedikit dibanding FIFO pada simulasi ini.

LRU menyesuaikan penggantian halaman dengan perilaku aktual program.

FIFO berpotensi mengalami Belady’s Anomaly, sedangkan LRU tidak.

---

## Kesimpulan
Berdasarkan hasil praktikum manajemen memori dengan algoritma page replacement FIFO dan LRU, dapat disimpulkan bahwa kedua algoritma berhasil diimplementasikan dan dijalankan sesuai dengan dataset yang diberikan. Hasil simulasi menunjukkan bahwa algoritma FIFO menghasilkan 10 page fault, sedangkan algoritma LRU menghasilkan 9 page fault.

Perbedaan jumlah page fault tersebut terjadi karena FIFO tidak mempertimbangkan riwayat penggunaan halaman, sehingga dapat mengganti halaman yang masih sering digunakan. Sebaliknya, LRU mempertimbangkan pola akses halaman dengan mempertahankan halaman yang baru saja digunakan, sehingga lebih efisien dalam menangani locality of reference.

Dengan demikian, algoritma LRU lebih efisien dibanding FIFO pada simulasi ini karena mampu mengurangi jumlah page fault dan memanfaatkan memori secara lebih optimal. Pemilihan algoritma page replacement yang tepat sangat berpengaruh terhadap kinerja sistem operasi dalam mengelola memori utama.

**Tugas**
Buat program simulasi page replacement FIFO dan LRU.
Jalankan simulasi dengan dataset uji.
Sajikan hasil simulasi dalam tabel atau grafik.
Tulis laporan praktikum pada laporan.md.

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
   **Jawaban:**
 - FIFO (First In First Out) mengganti halaman yang paling awal masuk ke memori, tanpa memperhatikan apakah halaman tersebut masih sering digunakan.

- LRU (Least Recently Used) mengganti halaman yang paling lama tidak diakses, sehingga lebih sesuai dengan pola penggunaan memori.
  
2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?
   **Jawaban:**
karena algoritma ini hanya mempertimbangkan urutan masuk halaman, bukan pola penggunaannya.
Akibatnya, ketika jumlah frame ditambah:
-Halaman yang masih sering digunakan bisa tetap tergantikan hanya karena masuk lebih awal.
-Penambahan frame justru dapat menyebabkan jumlah page fault meningkat, bukan menurun.
Fenomena inilah yang disebut Belady’s Anomaly, dan hal ini tidak terjadi pada algoritma berbasis stack seperti LRU karena LRU mempertahankan halaman yang baru saja digunakan.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:**
   LRU umumnya menghasilkan performa lebih baik dibanding FIFO karena mempertimbangkan pola akses halaman.

-LRU mengganti halaman yang paling lama tidak digunakan, sehingga halaman yang sering diakses tetap berada di memori.
-FIFO hanya berdasarkan urutan masuk halaman, tanpa melihat apakah halaman tersebut masih dibutuhkan.
-Akibatnya, LRU menghasilkan page fault lebih sedikit dan penggunaan memori yang lebih efisien.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Belum bisa mengerjakan tugas ini dengan mandiri sepenuhnya
- Bagaimana cara Anda mengatasinya?  Kerja kelompok

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
