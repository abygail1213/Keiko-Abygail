import math
print(f"Program menghitung luas oleh Abygail Evangeline Demelza")
print()
print("Menu:")
print("1. Menghitung luas persegi")
print("2. Menghitung luas lingkaran")

menu = input("Masukan nomor menu: ")

if menu == "1":
    sisi = float(input("Masukan sisi: "))
    luas = sisi * sisi
    print(f"Luas persegi adalah  {luas} satuan luas")

elif menu == "2":
    radius = float(input("Masukan radius: "))
    luas = 3.14 * (radius**2)
    print(f"Luas Lingkaran adalah  {round(luas, 2)} satuan luas")

else:
    print("nomor menu yang anda masukkan salah")
