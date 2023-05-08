import sys
import csv
import json
import pickle

class Reader:

    def __init__(self, nazwa_pliku):
        self.nazwa_pliku = nazwa_pliku

    def get_data(self):
        if self.nazwa_pliku[-3:] == 'txt':
            with open(self.nazwa_pliku, 'r') as f:
                dane = f.readlines()
            return dane
        elif self.nazwa_pliku[-3:] == 'csv':
            with open(self.nazwa_pliku, 'r') as f:
                dane = []
                reader = csv.reader(f)
                for line in reader:
                    dane.append(line)
            return dane
        elif self.nazwa_pliku[-4:] == 'json':
            with open(self.nazwa_pliku, 'r') as f:
                dane = json.load(f)
            return dane
        elif self.nazwa_pliku[-3:] == 'pkl':
            with open(self.nazwa_pliku, 'rb') as f:
                dane = pickle.load(f)
                return dane
        else:
            return 'Podany zły format pliku wejściowego'

class Writer(Reader):

    def write_data(self, dane):
        if self.nazwa_pliku[-3:] == "txt":
            with open(self.nazwa_pliku, 'w') as f:
                return json.dump(dane, f)
        elif self.nazwa_pliku[-3:] == "csv":
            with open(self.nazwa_pliku, 'w') as f:
                writer = csv.writer(f)
                return writer.writerows(dane)
        elif self.nazwa_pliku[-4:] == "json":
            with open(self.nazwa_pliku, 'w') as f:
                return json.dump(dane, f)
        elif self.nazwa_pliku[-3:] == "pkl":
            with open(self.nazwa_pliku, 'wb') as f:
                return pickle.dump(dane, f)
        else:
            print('Podany zły format pliku wyjściowego')


nazwa_plik_wejsciowy = 1
nazwa_plik_wyjsciowy = 2

if len(sys.argv) < 4:
    print('Nie podano argumentów...')
    quit()

f_in = sys.argv[nazwa_plik_wejsciowy]
f_out = sys.argv[nazwa_plik_wyjsciowy]

dane = Reader(f_in).get_data()

nowe_dane = (sys.argv[3:])
nowe_dane_split = []

for re in nowe_dane:
    podzielony_tekst = re.split(',')
    nowe_dane_split.append(podzielony_tekst)

print(dane)
print(nowe_dane_split)

for zmiana in nowe_dane_split:

    nowa_wartosc = zmiana[2]

    dane[int(zmiana[0])][int(zmiana[1])] = nowa_wartosc


Writer(f_out).write_data(dane)

