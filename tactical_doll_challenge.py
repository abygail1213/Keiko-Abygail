import math

def calculate_stats(firepower, rate_of_fire, accuracy, evasion):
    dps = round((firepower * rate_of_fire) / 60, 2)
    ce = math.floor((30 * firepower) + ((40 * (rate_of_fire ** 2)) / 120) + (15 * (accuracy + evasion)))
    return dps, ce

print("### MY TACTICAL DOLL ###")
my_nama = input("Masukkan nama Tactical Doll: ")
my_fp = int(input("Masukkan Firepower: "))
my_rof = int(input("Masukkan Rate of Fire: "))
my_acc = int(input("Masukkan Accuracy: "))
my_eva = int(input("Masukkan Evasion: "))

print("\n### ENEMY TACTICAL DOLL ###")
enemy_nama = input("Masukkan nama Tactical Doll: ")
enemy_fp = int(input("Masukkan Firepower: "))
enemy_rof = int(input("Masukkan Rate of Fire: "))
enemy_acc = int(input("Masukkan Accuracy: "))
enemy_eva = int(input("Masukkan Evasion: "))

my_dps, my_ce = calculate_stats(my_fp, my_rof, my_acc, my_eva)
enemy_dps, enemy_ce = calculate_stats(enemy_fp, enemy_rof, enemy_acc, enemy_eva)

print("\n### RESULT ###")
print(f"{my_nama}")
print(f"Damage per Second: {my_dps}")
print(f"Combat Effectiveness: {my_ce}")

print(f"\n{enemy_nama}")
print(f"Damage per Second: {enemy_dps}")
print(f"Combat Effectiveness: {enemy_ce}")

if my_dps >= enemy_dps and my_ce >= enemy_ce:
    print("\nKeputusan: Gass lawan")
else:
    print("\nKeputusan: Kabuuur")
