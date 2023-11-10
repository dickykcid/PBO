print("Program menghitung luas dan volume prisma Segitiga")

"""
Programmer : Dicky Franssetiaji
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
panjangalas = 4
tinggialas = 5
tinggiprisma = 6

# rumus
luas = tinggiprisma*(panjangalas*3)+(2*((1/2)*panjangalas*tinggialas))
volume = ((1/2)*panjangalas*tinggialas)*tinggiprisma

#output
print("Panjang alas :",panjangalas)
print("Tinggi alas :",tinggialas)
print("Tinggi prisma:",tinggiprisma)
print("Luas :",luas)
print("Volume :",volume)
