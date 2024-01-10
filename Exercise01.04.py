suma_stranici = int(input())
if suma_stranici < 1 or suma_stranici > 1000:
    print(1)
    exit()

stranici_na_chas = int(input())
if stranici_na_chas < 1 or stranici_na_chas > 1000:
    print(1)
    exit()

target_dni = int(input())
if target_dni < 1 or target_dni > 1000:
    print(1)
    exit()

vreme = int(suma_stranici / stranici_na_chas)
chasove_na_den = int(vreme/target_dni)
print(chasove_na_den)
