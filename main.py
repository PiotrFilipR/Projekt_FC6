import sys
import csv


dane = []

nazwa_plik_wejsciowy = 1
nazwa_plik_wyjsciowy = 2

if len(sys.argv) < 4:
    print('Nie podano argumentów...')
    quit()

f_in = sys.argv[nazwa_plik_wejsciowy]
f_out = sys.argv[nazwa_plik_wyjsciowy]

with open(f_in, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        dane.append(line)


nowe_dane = (sys.argv[3:])
nowe_dane_split = []

for re in nowe_dane:
    podzielony_tekst = re.split(",")
    nowe_dane_split.append(podzielony_tekst)

print(dane)
print(nowe_dane_split)

for zmiana in nowe_dane_split:

    nowa_wartosc = zmiana[2]

    dane[int(zmiana[0])][int(zmiana[1])] = nowa_wartosc

with open(f_out, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(dane)
