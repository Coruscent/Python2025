#Zadanie 1. wyznacz wartosc wyrazenia 10^2 + 136:4.15 * sqr(2)
#Wynik zapisz do zmiennej x#
x = 10**2 + 136/4.15*(2**0.5)
print(x)
#Zadanie 2. Oblicz wskaznik BMI osoby, ktorej waga = 139kg
#a wzrost = 211cm. Wynik zapisz do zmiennej BMI
BMI = 139/2.11**2
print(BMI)
#Zadanie 3. Zdefiniuj sekwencje seq="AGGTCTCAGGCGCTATCA"
#nastepnie zamien wszystkie tyminy na uracyl. Ile uracyli znajduje sie w sekwencji?'''
seq = "AGGTCTCAGGCGCTATCA"
seq = seq.replace('T','U')
print(seq)
seq.count('U')
print(seq.count('U'))
#Zadanie 4. Sprawdz czy wyrazenie x^14 +5x -145 jest wieksze
#od wyrazenia x^12 +10x -221 dla x=3
x = 3
y=x**14+5*x-145>x**12+10*x-221
print(y)
#''Zadanie 5. Z sekwencji seq = "AGGTCTCAGGCGCTATCA" utworz liste
#gdzie kazdy element to pojedynczy nukleotyd. Nastepnie stworz liste
#uniklanych nukleotydow oraz slownik w ktorym kluczem beda uniklane nukleotydy
#a wartoscia liczba ich wystapien w sekwencji.'
seq1 = "AGGTCTCAGGCGCTATCA"
print(list(seq1))
print(sorted(list(set(seq1))))
print(seq1.count('A'))
print(seq1.count('T'))
print(seq1.count('G'))
print(seq1.count('C'))
list_liczba= (seq1.count('A'),seq1.count('T'),seq1.count('G'),seq1.count('C'))
print(list_liczba)
list_unikalnyNukleotydow = sorted(list(set(seq1)))
print(list_unikalnyNukleotydow)
dict(zip(list_unikalnyNukleotydow,list_liczba))
print(dict(zip(list_unikalnyNukleotydow,list_liczba)))