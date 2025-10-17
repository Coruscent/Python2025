'''
Zadanie 1.
Korzystając z instrukcji if/else wyznacz liczbę miejsc zerowych równania kwadratowego ax^2 + bx + c = 0.
Pamiętaj, że liczba miejsc zerowych zależy od wartości parametru Delta = b^2 − 4ac.

Jeżeli Delta > 0 — równanie ma dwa różne miejsca zerowe.
Jeżeli Delta = 0 — równanie ma jedno (podwójne) miejsce zerowe.
Jeżeli Delta < 0 — równanie nie ma miejsc zerowych w zbiorze liczb rzeczywistych.

W zadaniu zaimplementuj sprawdzenie wartości Delty przy użyciu if/else i wypisz odpowiedni komunikat.
'''
a = 3
b = 5
c = 2
Delta = b**2 - 4*a*c
if Delta > 0:
 print(f'równanie ma dwa różne miejsca zerowe.')
elif Delta == 0:
  print(f'równanie ma jedno (podwójne) miejsce zerowe.')
elif Delta < 0:
  print(f'równanie nie ma miejsc zerowych w zbiorze liczb rzeczywistych.')

print(Delta) #sprawdzamy jaka jest Delta


'''
Zadanie 2.
Korzystając z petli while zbuduj listę składającą się z x elementów, 
gdzie każdy następny element to suma dwóch poprzednich z uwzględnieniem, 
że pierwsze dwa elementy listy to [0,1]. 
Innymi słowy zakoduj pętle, która buduje ciąg Fibonacciego o zadanej długości.
'''
def fibonacci(x):
  fib_list = [0, 1]
  while len(fib_list) < x:
    next_fib = fib_list[-1] + fib_list[-2]
    while len(fib_list) < x:
      next_fib = fib_list[-1] + fib_list[-2]
      fib_list.append(next_fib)
    return fib_list

liczba_elementów_x = 10
fib_sequence = fibonacci(liczba_elementów_x)
print(fib_sequence)

'''
Zadanie 3. 
Korzystajac z petli for i wyrazen if/else podziel liste a = [1,7,10,11,23,156,211,458,19,6]
na dwie listy jedna zawierajaca liczby parzyste druga zawierajaca liczby nieparzyste
'''
a = [1, 7, 10, 11, 23, 156, 211, 458, 19, 6]
parzyste = []
nieparzyste = []

for elem in a: 
  if elem % 2 == 0: #dzielienie na 2 bez reszty
    parzyste.append(elem)
  else:
    nieparzyste.append(elem)

print("Liczby parzyste", parzyste)
print("Liczby nieparzyste:", nieparzyste)

'''
Zadanie 4.
Korzystajac z listy skladanej utworz liste pierwiastkow n kolejnych liczb naturalnych
'''
# Liczba do przerobienia (n)
n = 10

# Utworzymy listę, zaokrąglamy przez int(lizcba)+1
pierwiastki = [int((i**0.5)+1) for i in range(n + 1)]

print(pierwiastki)
'''
Zadanie 5.
Zdefiniuj funkcje prime_number ktora jako argument przyjmuje liczbe x i zwraca
czy dana przez uzytkownika liczba jest liczba pierwsza
'''
def prime_number(x):
  """

  Sprawdza czy x jest liczbą pierwszą.% zwraca reszte z dzielienia

  Args:
    x: argument.

  Returns:
    True - liczba pierwsza, False - co innego.
  """
  if x < 2:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

x = 4
if prime_number(x):
  print(f"{x} jest liczbą pierwszą.")
else:
  print(f"{x} nie jest liczbą pierwszą.")