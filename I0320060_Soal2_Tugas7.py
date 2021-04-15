import math

#fungsi sqrt
print("Masukkan angka disini niscaya akan keluar hasil akarnya")
angka = int(input("> "))
akar = math.sqrt(angka)
print("Akar dari", angka,"adalah",akar)
print("Biar enak dilihat kawan: ",math.ceil(akar))

print("="*100)

print("Malas bertemu dengan angka desimal yang harus dibulatkan?")
print("Masukkan saja angka anda disini")
bulat = float(input("> "))
print("Mau dibulatkan kemana sich kawan ?")
print("1. Atas")
print("2. Bawah")
pilihan = int(input("> "))

if pilihan == 1:
    #fungsi ceil
    print("Ini adalah hasil pembulatan ke atas kawan: ", math.ceil(bulat))
elif pilihan == 2:
    #fungsi floor
    print("Ini adalah hasil pembulatan ke bawah kawan: ", math.floor(bulat))
else:
    pass


