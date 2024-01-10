cena_himikalka = 5.8
cena_marker = 7.2
cena_preparat = 1.2

broi_himikalki = int(input())
if broi_himikalki < 0 or broi_himikalki > 100:
    print(1)
    exit()

broi_marker = int(input())
if broi_marker < 0 or broi_marker > 100:
    print(1)
    exit()

litri_preparat = int(input())
if litri_preparat < 0 or litri_preparat > 50:
    print(1)
    exit()

procent_namalenie = int(input())
if procent_namalenie < 0 or procent_namalenie > 100:
    print(1)
    exit()

himikalki = cena_himikalka*broi_himikalki
marker = cena_marker*broi_marker
preparat = cena_preparat*litri_preparat
sum = ((100-procent_namalenie)*(himikalki + marker + preparat))/100
print(sum)
