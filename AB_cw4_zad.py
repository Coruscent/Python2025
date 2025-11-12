'''zadanie 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

zmodifikuj powyższą funkcję tak, aby sortowała listę w porządku malejącym.
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]: # Changed from > to < for descending order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
'''zadanie 2
ykorzystując moduł time sprawdź, które podejście iteracyjne czy rekurencyjne zwróci 
szybciej wartość dla 50 elementu ciągu fibbonaciego.
'''
#Rekurencja – funkcja wywołuje samą siebie; czytelna i elegancka, ale może używać dużo pamięci (stack).
#Iteracja – pętle (for/while) powtarzają operacje; zwykle bardziej wydajna pamięciowo, czasami mniej czytelna.
def fib_reccur(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_reccur(n - 1) + fib_reccur(n - 2)
#ciąg fibb iteracyjnie
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
import time
start_time=time.time()
fib_reccur(25)
end_time=time.time()
execution_time=end_time-start_time
print(f'Czas wykonania rekurencyjnie - Fibo: {end_time-start_time}s')
import time
start_time=time.time()
fib_iter(25)
end_time=time.time()
execution_time=end_time-start_time
print(f'Czas wykonania iteracyjnie - Fibo: {end_time-start_time}s')
'''zadanie 3
zdefiniuj funkcje ktora wylicza silnie podejscie iteracyjne i rekurencyjne.
Następnie wykorzystaj moduł time aby sprawdzić, które podejście jest szybsze dla np. 1000!
'''
def silnia_iter(n):
    if n < 0:
        return "Bląd - nie dajemy liczb ujemnych do silni."
    elif n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n + 1):
            product *= i
        return product
import time
start_time=time.time()
silnia_iter(100)
print(f"Iteracyjna silnia : {silnia_iter(100)}")
end_time=time.time()
execution_time=end_time-start_time
print(f'Czas wykonania iteracyjnie: {end_time-start_time}s')

def silnia_reccur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia_reccur(n - 1)
import time
start_time=time.time()
silnia_reccur(100)
print(f"Rekurencyjna silnia : {silnia_iter(100)}")
end_time=time.time()
execution_time=end_time-start_time
print(f'Czas wykonania rekurencyjnie: {end_time-start_time}s')
'''zadanie 4
nested_list = [1, [2, [3, 4], 5], 6]

def find_recursive(lst, target):
    for item in lst
        if type(item) == list
            result = find_recursive(item, target)
            if result != None
                return result
        elif item = target
            return item
    return None

print(find_recursive(nested_list 4))

jakie błędy występują w powyższym kodzie? Popraw je.
'''
nested_list = [1, [2, [3, 4], 5], 6]
#syntax errors
def find_recursive(lst, target): #dwa argumenty, zapisane przez przecinek
    for item in lst:
        if type(item) == list:# dwukropek
            result = find_recursive(item, target)
            if result != None: #dwukropek
                return result
        elif item == target:#dwukropek
            return item
    return None

print(find_recursive(nested_list, 4)) # dwa argumenty, dodano przecinek
'''zadanie 5
dla danej listy sekwencji zwróć listę zawierającą liczbę tymin 
dla każdej sekwencji (rozwiązanie 1/2 linijkowe). Przykładowo dla: ["ATTGC", "AGGC", "TTTGC"]
 powinieneś otrzymać [2,0,3]. Wykonaj to zadanie na 2 różne sposoby (map lub filter/lista składana)
'''
lista_seq= ["ATTGC", "AGGC", "TTTGC"]

#Sposob1:Lambda  z argumentem'seq', wykorzystuje metod  .count() dla 'seq'.
thymine_counts_map = list(map(lambda seq: seq.count("T"), lista_seq))
print(f'Liczba tymin metodą lambda {thymine_counts_map}')

# Sposob2:  list comprehension - lista składana
thymine_counts_comprehension = [seq.count("T") for seq in lista_seq]
print(f'Liczba tymin metodą list składanych {thymine_counts_comprehension}')
'''zadanie 6
list(map((lambda x: x**x, [1,2,3,4,5,6])))
przepisz powyższy kod na listę składana.
'''
# Korzystając z lambda:
original_list_zad6 = [1,2,3,4,5,6]
mapped_list_zad6 = list(map(lambda x: x**x, original_list_zad6))
print(f"Korzystając z map i lambda: {mapped_list_zad6}")

# Korzystając z list comprehension
list_comprehension_zad6 = [x**x for x in original_list_zad6]
print(f"Korzystając z list składanych: {list_comprehension_zad6}")
'''zadanie 7
Dany jest string, w którym znajdują się sekwencje nukleotydowe
. W 2 linijkach kodu, zapisz każdą sekwencję jako kolejny element listy i 
posortuj je wg liczby uracyli (od sekwencji zawierającej najwięcej, do tej najmniej).
s = "UGAGGUAGUAGGUUUUUUUUUU, UGAGGUAGUAGGUUGAUUUUUU, UGAGGUAGUAGGUUGUUUUUUU, UGAGGUAGUAGGUUGUGAUUUU, UGAGGUAGUAGGUUGUAUGGUU"
'''
s = "UGAGGUAGUAGGUUUUUUUUUU, UGAGGUAGUAGGUUGAUUUUUU, UGAGGUAGUAGGUUGUUUUUUU, UGAGGUAGUAGGUUGUGAUUUU, UGAGGUAGUAGGUUGUAUGGUU"

# Dzielimy ciąg znaków na listę sekwencji
sequences = s.split(', ')

# Sortujemy listę sekwencji według liczby uracyli ('U') w kolejności malejącej(Reverse=true,Domyślnym zachowaniem jest kolejność rosnąca.)
sequences.sort(key=lambda seq: seq.count('U'), reverse=True)

print(f'Posortowane malejąco sekwencję: {sequences}')