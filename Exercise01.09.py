daljina = int(input())
if daljina < 10 or daljina > 500:
    print(1)
    exit()

shirina = int(input())
if shirina < 10 or shirina > 300:
    print(1)
    exit()

visochina = int(input())
if visochina < 10 or visochina > 200:
    print(1)
    exit()

procent = float(input())
if procent < 0 or procent > 100:
    print(1)
    exit()

obem_cm = daljina*shirina*visochina
obem_litri = obem_cm/1000
obem_voda = ((100-procent)*obem_litri)/100
print(obem_voda)