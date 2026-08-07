import math

print("### REQUEST TACTICAL DOLL ###")
nama = input("Masukkan nama Tactical Doll: ")
firepower = int(input("Masukkan Firepower: "))
rate_of_fire = int(input("Masukkan Rate of Fire: "))
accuracy = int(input("Masukkan Accuracy: "))
evasion = int(input("Masukkan Evasion: "))

dps = (firepower * rate_of_fire) / 60
dps_rounded = round(dps, 2)

ce = (30 * firepower) + ((40 * (rate_of_fire ** 2)) / 120) + (15 * (accuracy + evasion))
ce_floored = math.floor(ce)

print("\n### SUCCESS ###")
print(f"Tactical Doll: {nama}")
print(f"Firepower: {firepower}")
print(f"Rate of Fire: {rate_of_fire}")
print(f"Accuracy: {accuracy}")
print(f"Evasion: {evasion}")
print(f"Damage per Second: {dps_rounded}")
print(f"Combat Effectiveness: {ce_floored}")
