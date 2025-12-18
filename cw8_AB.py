# Zadanie 1:
# Wyznacz wszystkie rozwiązania rówania a + b + c = a b c – 150 w zbiorze liczb naturalnych nie większych od 100.
#Ile jest takich rozwiązań?
# Podpowiedź: możesz sprawdzić wszystkie potencjalne rozwiązania za pomocą trzech pętli for.
solutions_count = 0
solutions = []

# Iteracja od 1 do 100
for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            # Równanie
            if a + b + c == (a * b * c) - 150:
                solutions_count += 1
                # Zapisywanie rozwiązań w krotkę(tuple), żeby ich rozróżniać.
                #Zapisywanie rozwiązań trypletami.
                solutions.append((a, b, c))

print(f"Znaleziono {solutions_count} rozwiązań dla a, b, w zbiorze liczb naturalnych nie większych od 100:")
for sol in solutions:
    print(sol)

#Zadanie2:
#Dysponujemy kwotą początkową 100 zł. Wchodzimy z nią do następującej gry: Rzucamy monetą
#jeżeli wypadnie orzeł, to połowa naszej kwoty ulega podwojeniu (a druga połowa zostaje bez zmian)
#jeżeli wypadnie reszka, to połowa naszej kwoty ulega zmniejszeniu o połowę (a druga połowa zostaje bez zmian)
#Rzucamy 21 razy monetą. Wykonaj 1000 takich symulacji i wyznacz medianę kwoty końcowej.

#Podpowiedź: Na początku zdefiniuj funkcję, która wykonuje jedną taką symulację (startujemy od 100 zł, 21 rzutów monetą -> i zwraca końcową kwotę); następnie wywołaj tę funkcję w pętli for 1000 razy każdorazowo zapisując do listy zwracany wynik.

import random
import statistics

def symuluj_gre(startowa_kwota=100, liczba_rzutow=21):
  """
  Symuluje jedną grę w monetę na zadaną liczbę rzutów i zwraca końcową kwotę.
  """
  kwota = startowa_kwota
  for _ in range(liczba_rzutow):
    moneta = random.randint(0, 1) # 0 dla orła, 1 dla reszki
    polowa_kwoty = kwota / 2

    if moneta == 0: # Orzeł: połowa kwoty się podwaja
      kwota = polowa_kwoty * 2 + polowa_kwoty #  (polowa * 2) + polowa
    else: # Reszka: połowa kwoty zmniejsza się o połowę
      kwota = (polowa_kwoty / 2) + polowa_kwoty #  kwota się zmniejsza o 1/4

  return kwota

# Wykonaj 1000 symulacji
wyniki_symulacji = []
for _ in range(1000):
  wyniki_symulacji.append(symuluj_gre(100, 21))

# Oblicz medianę końcowych kwot
mediana_kwoty = statistics.median(wyniki_symulacji)

print(f"Mediana końcowej kwoty po 1000 symulacji: {mediana_kwoty:.2f} zł")
#Zad4.Udekoruj choinkę. Formalnie, napisz kod w języku Python który wstawi na każdą warstwę losową liczbę ozdób w losowe miejsca. 
 #(np O, chociaż ten symbol też może być losowany z jakiegoś zbioru).
#n = 15 #liczba wartstw
#print(' '*n+'X')
#s = ' '*n+'+'
#for i in range(n):
#    print(s)    
#    s=s[1:]+'+'*2 
#print(' '*(n-1)+'||')
import random

n = 15 #liczba wartstw

decoration_symbols = ['*', 'O', '@', '#', '!', '$'] 

print(' ' * n + 'X')
s = [' '] * (2 * n + 1) # lista znaków
s[n] = '+'

for i in range(n): # i to numer warstwy od 0 do n-1
    current_width = 2 * i + 1 # Szerokość aktualnej warstwy (liczba '+')
    current_indent = n - i - 1 # Wcięcie dla aktualnej warstwy

    layer_str_list = [' '] * (2 * n + 1) # Nowa lista znaków
    for k in range(current_width):
        layer_str_list[current_indent + k] = '+' #+ dla warstwy określa choinkę

    # Losowa liczba ozdób (np. od 0 do połowy szerokości warstwy)
    num_decorations = random.randint(0, current_width // 2 + 1)

    for _ in range(num_decorations):
        # Losowe miejsce na ozdobę w obrębie plusów danej warstwy
        #pojawienie się znaków w granicach + z choinki
        decoration_pos = random.randint(0, current_width - 1)
        # random symbol
        symbol = random.choice(decoration_symbols)
        # Dodanie symbola na przypadkową wasrstwę choinki
        layer_str_list[current_indent + decoration_pos] = symbol

    print("".join(layer_str_list).rstrip())

print(' ' * (n - 1) + '||')

#Zadanie5: Napisz kod, który otwiera wszystkie pliki tekstowe (z rozszerzeniem .txt) w danym folderze.
#Pliki te z założenia zawierają informacje o ocenach kolejnych osób (oceny każdej osoby są w osobnym pliku, podane po przecinku w jednym wierszu). Wyznacz średnią ocen każdej z osób oraz średnią ocen całej grupy oraz wyświetl je na ekranie.
#przyklad

#Plik: Piotr.txt zawiera: 4,5,3,5
#Plik: Kamil.txt zawiera: 3,6,3,4

#dla takich pliów powinien na ekranie zostać wyświetlony napis: Srednia dla Piotr: 4.25, Kamil: 4; cała grupa: 4.125;
#W przypadku dłuższych rozwinięć dziesiętnych możesz zastosować metodę round z 2 miejscami po przecinku
import os

folder = r"C:\\grades_data" #ścieżka folderu z plikami txt: r"C:\etc\etc\grades_data"  \/ matters!! ONLY \ will work

if not os.path.isdir(folder):
    print(f"Błąd: folder '{folder}' nie istnieje.")
else:
    srednie_osob = {}
    wszystkie_oceny = []

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            name = filename.replace(".txt", "")
            path = os.path.join(folder, filename)
            
            try:
                with open(path, "r") as f:
                    line = f.readline().strip()
                    oceny = [float(x) for x in line.split(",")]
            except Exception as e:
                print(f"Błąd w pliku {filename}: {e}")
                continue
            
            srednia = sum(oceny) / len(oceny)
            srednie_osob[name] = round(srednia, 2)
            wszystkie_oceny.extend(oceny)

    if wszystkie_oceny:
        srednia_grupy = round(sum(wszystkie_oceny) / len(wszystkie_oceny), 2)

        for name, avg in srednie_osob.items():
            print(f"Srednia dla {name}: {avg}")

        print(f"Średnia dla całej grupy: {srednia_grupy}")
    else:
        print("Brak poprawnych danych do obliczeń.")