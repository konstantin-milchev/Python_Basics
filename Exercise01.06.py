cena_naylon = 1.5
cena_boia = 14.5
cena_razreditel = 5

plosht_naylon = int(input())
if plosht_naylon < 0 or plosht_naylon > 100:
    print(1)
    exit()

litri_boia = int(input())
if litri_boia < 0 or litri_boia > 100:
    print(1)
    exit()

litri_razreditel = int(input())
if litri_razreditel < 0 or litri_razreditel > 30:
    print(1)
    exit()

chasove = int(input())
if chasove < 0 or chasove > 9:
    print(1)
    exit()

suma_naylon = (plosht_naylon + 2)*cena_naylon
suma_boia = (litri_boia*1.1)*cena_boia
suma_razreditel = litri_razreditel*cena_razreditel
suma_torbichka = 0.4
suma_materiali = suma_boia + suma_razreditel + suma_naylon + suma_torbichka
suma_maistor = suma_materiali*0.3*chasove
suma_obshto = suma_materiali + suma_maistor
print(suma_obshto)