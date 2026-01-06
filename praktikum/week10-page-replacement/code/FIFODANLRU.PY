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
