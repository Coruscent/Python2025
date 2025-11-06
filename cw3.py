#Zadanie 1.
#Napisz funkcję, która wylicza wartość wyrażenia:

#f(x) = (x² − 4) / (x − 2)

#Wykorzystaj try/except  do sytuacji gdy funkcja zwróci error
def calculate_zad1(x):
  """
  Oblicza wartość wyrażenia (x^2 - 4) / (x - 2).
  Obsługuje błąd ZeroDivisionError, jeśli x wynosi 2.

  Args:
    x: Wartość wejściowa.

  Returns:
    Obliczona wartość lub komunikat o błędzie, jeśli wystąpi dzielenie przez zero.
  """
  try:
    # Próba obliczenia wyrażenia
    result = (x**2 - 4) / (x - 2)
    return result
  except ZeroDivisionError:
    # Obsługa błędu dzielenia przez zero
    return "Błąd: Dzielenie przez zero jest niedozwolone (x nie może wynosić 2)."

# Przykłady użycia:
print(f"Dla x = 5: {calculate_zad1(5)}")
print(f"Dla x = 2: {calculate_zad1(2)}")
#Zadanie 2.
#Napisz funkcję, która przyjmuje dowolną liczbę argumentów i jako wynik zwraca ich średnią:

#a) arytmetyczną
#b) geometryczną
#Wywołanie funkcji averages(*args) powinno zwracać listę postaci: [arytmetyczna, geometryczna]
def averages(*args):
  """
  Zwraca średnia arytmetyczną oraz geometryczną
  """

    # Średnia arytmetyczna
  arytmetyczna = sum(args) / len(args)

    # Średnia geometryczna
    #Średnią geometryczną dla \(n\) dodatnich liczb \(a_{1},a_{2},...,a_{n}\) oblicza się,
  #mnożąc wszystkie te liczby przez siebie,
  #a następnie obliczając pierwiastek \(n\)-tego stopnia z otrzymanego iloczynu.
  iloczyn = 1
  for x in args:
      iloczyn *= x
  geometryczna = iloczyn ** (1 / len(args))

  return [f"Średnia arymetryczna:{arytmetyczna}", f"Średnia geometryczna:{geometryczna}"]
#Zadanie 3.
#Zmodyfikuj funkcję z zadania 2. tak, aby użytkownik ręcznie podawał liczby. Uwaga proces musi się kiedyś zakończyć.

def averages_zad3():#nie trzeba *arg, bo w input możemy dać dowolną iłość argumentów
    """
    Funkcja działa na bazie funkcji averages i zwraca średnie dla ręcznie podanych lizcb
    """
    averages_zad3_input = input("Podaj ręcznie liczby po przecinku (np. 1,1,1): ")
    try:
        lista_zad3 = [float(x.strip()) for x in averages_zad3_input.split(',')]
        #rozpakować listę z poprzednią funkcją averages
        return averages(*lista_zad3)
    except ValueError:
        return "Błąd: Wprowadzono nieprawidłowe dane. Upewnij się, że podajesz liczby oddzielone przecinkami."

print(averages_zad3())
#Zadanie 4.
#Z pliku 1E7A.fasta wczytaj do zmiennej hsa_seq sekwencję albuminy ludzkiej.
hsa_seq = ""
with open("1E7A.fasta", "r") as file:
  # Pomiń linię nagłówka
  next(file)
  # Wczytaj pozostałe linie i połącz je, usuwając znaki nowej linii
  for line in file:
    hsa_seq += line.strip()

print(hsa_seq) # Wyświetl sekwencje
#Zadanie 5.
#Ze zmiennej 1E7A.fasta utwórz słownik hsa_dict, gdzie klucze to odpowiednie oznaczenia aminokwasów, a wartości im odpowiadające to ilość ich wystąpień w sekwencji.
hsa_dict = {} # Tworzy pusty słownik o nazwie hsa_dict.
#Ten słownik będzie przechowywał aminokwasy jako klucze i ich liczby wystąpień jako wartości
for amino_acid in hsa_seq:
  # Rozpoczyna pętlę, która przechodzi przez każdy znak (aminokwas) w ciągu tekstowym hsa_seq.
  # W każdej iteracji, bieżący aminokwas jest przypisywany do zmiennej amino_acid.
  if amino_acid in hsa_dict:#Sprawdza,
  #czy bieżący aminokwas (amino\_acid) jest już kluczem w słowniku hsa_dict.
    hsa_dict[amino_acid] += 1 #Jeśli aminokwas jest już w słowniku,
    #zwiększa jego wartość (liczbę wystąpień) o 1.
  else: #Jeśli aminokwasu nie ma w słowniku.
    hsa_dict[amino_acid] = 1 #Dodaje ten aminokwas jako nowy klucz do
    # słownika hsa_dict i przypisuje mu wartość 1 (ponieważ jest to pierwsze wystąpienie tego aminokwasu).

print(hsa_dict)
#Zadanie 6.
#Zapisz do nowego pliku hsa_freq częstość wystąpięń aminokwasów w HSA. Plik powinien mieć postać:
#M 4
#A 5
#G 1
with open("hsa_freq.txt", "w") as file:
  for amino_acid, count in hsa_dict.items():
    file.write(f"{amino_acid} {count}\n")

print("Częstość występowania aminokwasów została zapisana do pliku hsa_freq.txt")
#Zadanie 7.
#Napisz funkcję, która przyjmuje jako argument x i zwraca wynik wyrażenia:

#f(x) = (sin(π x) + cos(x²)) / (x! + √|x| - e^(-x))
import math as mt
#factorial(n, /)
   #Find n!. #Raise a ValueError if x is negative or non-integral.
#sin(x, /)
   #Return the sine of x (measured in radians).
#cos(x, /)
       # Return the cosine of x (measured in radians).
def f(x):
    # obliczamy składniki wyrażenia
    licznik = mt.sin(mt.pi * x) + mt.cos(x ** 2)
    mianownik = mt.factorial(int(x)) + mt.sqrt(abs(x)) - mt.e ** (-x)

    # zabezpieczenie przed dzieleniem przez zero
    if mianownik == 0:
        return "Dzielenie przez zero"

    return licznik / mianownik


# Przykłady użycia:
print(f(5))
#Zadanie 8.
#Napisz minutnik, który przyjmuje od użytkownika czas podany w formacie [X,Y,Z], 
# gdzie X=liczba godzin, Y=liczba minut, Z=liczba sekund. Po upływie czasu funkcja powinna zwrócić coś postaci "czas minął".
import time

def minutnik(czas):
    # czas = [X, Y, Z]  [godziny, minuty, sekundy]
    godziny, minuty, sekundy = czas

    # przelicz wszystko na sekundy
    calkowity_czas = godziny * 3600 + minuty * 60 + sekundy

    print(f"Minutnik uruchomiony na {godziny}h {minuty}min {sekundy}s...")
    time.sleep(calkowity_czas)  # zatrzymuje działanie programu na podany czas

    print("Czas minął!")


#  Przykład użycia:
minutnik([0, 0, 5])  # minutnik na 5 sekund
#Zadanie 9*.
#Napisz funkcję `mini_ruletka()`, która symuluje prostą grę w ruletkę:

#Funkcja losuje liczbę całkowitą z przedziału 0–36 (kolory ruletki: czerwony/ czarny/ zielony).

#0 jest zawsze zielone.
#Liczby parzyste > 0 to czarne, nieparzyste > 0 to czerwone.
#Użytkownik podaję liczbę oraz stawkę zakładu

#Funkcja losuje wynik i zwraca:

#Wylosowaną liczbę i kolor,
#Informację, czy użytkownik wygrał (trafienie liczby lub koloru).
#Dodatkowo oblicza wygraną:

#Trafienie liczby: 35 * zakład
#Trafienie koloru (czarny/czerwony): 2 * zakład
#Nietrafiony: 0
import random

def mini_ruletka():
    # --- Użytkownik podaje swoje dane ---
    liczba_gracza = int(input("Podaj liczbę (0–36): "))
    stawka = float(input("Podaj stawkę zakładu (zł): "))

    # --- Losowanie wyniku ---
    wynik = random.randint(0, 36)

    # --- Ustalenie koloru wylosowanej liczby ---
    if wynik == 0:
        kolor_wyniku = "zielony"
    elif wynik % 2 == 0:
        kolor_wyniku = "czarny"
    else:
        kolor_wyniku = "czerwony"

    # --- Ustalenie koloru gracza ---
    if liczba_gracza == 0:
        kolor_gracza = "zielony"
    elif liczba_gracza % 2 == 0:
        kolor_gracza = "czarny"
    else:
        kolor_gracza = "czerwony"

    # --- Sprawdzenie wyniku i obliczenie wygranej ---
    if liczba_gracza == wynik:
        wygrana = 35 * stawka
        komunikat = "🎯 Trafiłeś dokładną liczbę!"
    elif kolor_gracza == kolor_wyniku and wynik != 0:
        wygrana = 2 * stawka
        komunikat = "🔴⚫ Trafiłeś kolor!"
    else:
        wygrana = 0
        komunikat = "❌ Niestety, przegrywasz."

    # --- Wynik gry ---
    print(f"\nWylosowana liczba: {wynik} ({kolor_wyniku})")
    print(f"Twoja liczba: {liczba_gracza} ({kolor_gracza})")
    print(komunikat)
    print(f"Twoja wygrana: {wygrana:.2f} zł")
    
mini_ruletka()