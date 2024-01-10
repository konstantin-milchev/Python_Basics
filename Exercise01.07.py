pileshko_menu = 10.35
riba_menu = 12.40
vegetariansko_menu = 8.15

broi_pileta = int(input())
if broi_pileta < 0 or broi_pileta > 99:
    print(1)
    exit()

broi_riba = int(input())
if broi_riba < 0 or broi_riba > 99:
    print(1)
    exit()

broi_vegetariansko = int(input())
if broi_vegetariansko < 0 or broi_vegetariansko > 99:
    print(1)
    exit()

suma_pileshko = pileshko_menu*broi_pileta
suma_riba = riba_menu*broi_riba
suma_vegetariansko = vegetariansko_menu*broi_vegetariansko
dostavka = 2.5
suma = suma_pileshko + suma_riba + suma_vegetariansko
desert = 0.2*suma
suma_obshto = suma+desert+dostavka
print(suma_obshto)
