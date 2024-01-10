suma_start = float(input())
if suma_start < 100 or suma_start > 10000:
    print(1)
    exit()

srok = int(input())
if srok < 1 or srok > 12:
    print(1)
    exit()

procent = float(input())
if procent < 0 or procent > 100:
    print(1)
    exit()

suma_end = suma_start + srok * ((suma_start * procent) / 1200)
print(suma_end)

