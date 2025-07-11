class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

def merge_sort(arr, key='ipk', reverse=True):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, key, reverse)
        merge_sort(right, key, reverse)

        i = j = k = 0

        while i < len(left) and j < len(right):
            # Bandingkan berdasarkan key (default: IPK)
            left_val = getattr(left[i], key)
            right_val = getattr(right[j], key)
            
            if (left_val >= right_val) if reverse else (left_val <= right_val):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Data contoh
data_mhs = [
    Mahasiswa("Andi", "101", 3.75),
    Mahasiswa("Budi", "102", 3.90),
    Mahasiswa("Citra", "103", 3.65),
    Mahasiswa("Dewi", "104", 3.95),
    Mahasiswa("Eka", "105", 3.80)
]

# Sebelum diurutkan
print("Sebelum diurutkan:")
for m in data_mhs:
    print(f"{m.nim} {m.nama}: {m.ipk}")

# Proses pengurutan
merge_sort(data_mhs, key='ipk', reverse=True)

# Setelah diurutkan
print("\nSetelah diurutkan (Descending IPK):")
for m in data_mhs:
    print(f"{m.nim} {m.nama}: {m.ipk}")