# Latihan 2: Membaca file teks dengan iterasi langsung
with open("data/catatan.txt", "r", encoding="utf-8") as file:
    for baris in file:
        print(baris.strip())