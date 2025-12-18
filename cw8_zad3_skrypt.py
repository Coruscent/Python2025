
import random
#CMD -> py "C:etc\etc\cw8_zad3_skrypt.py"
def losowa_sekwencja(dlugosc):
 """
 Otwiera skrypt z linii komend, przyjmuje od użytkownika liczbę a,b, tworzy sekwencję seq1, seq2. Liczy różnice tymin między seq1 oraz seq2.
 """
 nukleotydy = ["A", "C", "G", "T"]
 return "".join(random.choice(nukleotydy) for _ in range(dlugosc))

while True:
    try:
        a = int(input("Podaj pierwszą dodatnią liczbę całkowitą a: "))
        b = int(input("Podaj drugą dodatnią liczbę całkowitą b: "))

        if a <= 0 or b <= 0:
            print("Błąd: obie liczby muszą być dodatnimi liczbami całkowitymi.")
            continue

        break

    except ValueError:
        print("Błąd: podaj poprawne liczby całkowite.")

seq1 = losowa_sekwencja(a)
seq2 = losowa_sekwencja(b)

t1 = seq1.count("T")
t2 = seq2.count("T")

roznica = t1 - t2

print(f"Sekwencja 1 (długość {a}): {seq1}")
print(f"Liczba tymin w sekwencji 1: {t1}")

print(f"Sekwencja 2 (długość {b}): {seq2}")
print(f"Liczba tymin w sekwencji 2: {t2}")

print(f"Różnica w liczbie tymin (pierwsza - druga): {roznica}")