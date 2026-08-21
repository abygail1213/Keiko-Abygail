banyak_perintah = int(input("Banyak perintah : "))

x = 0
y = 0

for _ in range(banyak_perintah):
    perintah = input("Masukkan perintah : ").strip().upper()
    
    if perintah == "U":
        y += 1
    elif perintah == "S":
        y -= 1
    elif perintah == "T":
        x += 1
    elif perintah == "B":
        x -= 1
    elif perintah == "HOME":
        break
    else:
        pass

print(f"Karakter Meong Brosss berada di koordinat ({x},{y})")
