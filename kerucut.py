print("Program menghitung luas dan volume Kerucut")

"""
Programmer : Dicky Franssetiaji
Pertemuan : 1
Tanggal : 22 Oktober 2023
"""

# Nilai
r = 5
tinggikerucut = 10
tinggiselimut = 15
π = 3.14

# rumus 
luas = (π*r*tinggiselimut)+(π*r*r)
volume = (1/3)*π*r*r*tinggikerucut

#output
print("Jari-jari :",r)
print("Tinggi Selimut :",tinggiselimut)
print("Tinggi Kerucut :",tinggikerucut)
print("Luas :",luas)
print("Volume :",volume)
