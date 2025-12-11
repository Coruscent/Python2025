#Zadanie 1.
#Rozbuduj klasę Wektor o następujące funkcję:
#odejmowanie wektorów

#iloczyn skalarny

#długość wektora

#iloczyn wektorowy
class Wektor:
    def __init__(self, x, y, z): # dopisano Z dla 3D wektora
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return f"Suma wektorów :{Wektor(self.x + other.x, self.y + other.y,self.z + other.z)}"

    def __sub__(self, other):
        return f"Różnica wektorów : {Wektor(self.x - other.x, self.y - other.y,self.z + other.z)}"

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y  and self.z == other.z

    def __repr__(self):
        return f"Wektor (x={self.x}, y={self.y},z={self.z})"

    def dot_product(self, other): #Iloczyn skalarny a*b = a1​b1​+a2​b2​+a3​b3​.
        return f"Iloczyn skalarny wektorów to : {(self.x * other.x + self.y * other.y + self.z * other.z)}"

    def magnitude(self):
        return f"Długość wektora to : {(self.x**2 + self.y**2 + self.z**2)**0.5}" #Długość (moduł) wektora(w(a,b) ->  sqrt(a^2+b^2))

    def cross_product_2d(self, other):#iloczyn wektorowy a x b = (a2​b3​−a3​b2​,a3​b1​−a1​b3​,a1​b2​−a2​b1​).
        return  f"Iloczyn wektorowy to : {self.x * other.y - self.y * other.x - self.z * other.y - self.y * other.z - self.z * other.x - self.x * other.z}"
wektor_a=Wektor(1,5,8)
wektor_b=Wektor(0,2,7)
print(wektor_a.dot_product(wektor_b))
print(Wektor.magnitude(wektor_a))
print(wektor_a.cross_product_2d(wektor_b))
print(wektor_a.__add__(wektor_b))
print(wektor_a.__sub__(wektor_b))
print(wektor_a.__eq__(wektor_b))

#Zadanie 2.
#Zdefiniuj klasę  Kolo  wraz z potrzebnymi metodami. Kolo jest określone przez podanie środka i promienia. Uwzględnić obsługę błędów
import math

class Punkt:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        # porównanie z innym objektem "punkt"
        if not isinstance(other, Punkt):
            return NotImplemented
        return self.x == other.x and self.y == other.y


class Kolo:

    """ Klasa reprezentujaca kola na plaszczyznie"""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("Promień koła nie może być ujemny.")

        self.pt = Punkt(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Kolo(x={self.pt.x}, y={self.pt.y}, radius={self.radius})"

    def __eq__(self, other):
        if not isinstance(other, Kolo):
            return NotImplemented
        return self.pt == other.pt and self.radius == other.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def move(self, a, b):
        # Przesuwa środek koła o wektor (a, b)
        self.pt.x += a
        self.pt.y += b
        return self # Zwraca zmodyfikowane koło dla płynności operacji

    def tangent(self, other): # sprawdza czy dwa kola są styczne
        if not isinstance(other, Kolo):
            raise TypeError("Argument 'other' musi być obiektem klasy Kolo.")

        # Oblicz odległość między środkami kół
        distance_centers = math.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)

        # Dwa koła są styczne, jeśli odległość między ich środkami jest równa sumie lub różnicy ich promieni
        return math.isclose(distance_centers, self.radius + other.radius) or \
               math.isclose(distance_centers, abs(self.radius - other.radius))
#Zadanie 3.
#Zdefiniuj klasę FunkcjaKwadratowa, która przechowuje funkcję kwadratową.
#Klasa powinna zaiwerać trzy zmienne: a, b, c, które są przypisywane w konstruktorze. Główną metodą powinna być rozwiaz(), która zwraca mmiejsca zerowe podanej funkcji (uwzględnić odpowiednie przypadki i obsługę błędów).
#  Zdefiniuj orócz metody rozwiaz() dwie inne wybrane metody, których można użyc przy funkcji kwadratowej.
import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        parts = []
        if self.a != 0:
            parts.append(f"{self.a}x²")
        if self.b != 0:
            parts.append(f"{'+' if self.b > 0 and parts else ''}{self.b}x")
        if self.c != 0:
            parts.append(f"{'+' if self.c > 0 and parts else ''}{self.c}")

        if not parts: # If a=b=c=0
            return "0"
        return "".join(parts)

    def rozwiaz(self):
        """Zwraca miejsca zerowe funkcji kwadratowej."""
        if self.a == 0:
            if self.b == 0:
                return "Równanie nie jest kwadratowe: Brak rozwiązań (0=c) lub nieskończenie wiele (0=0)."
            else:
                x = -self.c / self.b
                return f"Równanie nie jest kwadratowe (a=0): Jedno miejsce zerowe x = {x}"

        delta = self.b**2 - 4 * self.a * self.c

        if delta < 0:
            return "Brak miejsc zerowych w zbiorze liczb rzeczywistych."
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return f"Jedno podwójne miejsce zerowe: x = {x}"
        else:
            x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            return f"Dwa miejsca zerowe: x1 = {x1}, x2 = {x2}"

    def calculate_value(self, x):
        """Oblicza wartość funkcji dla danego x."""
        return self.a * (x**2) + self.b * x + self.c

    def get_vertex(self):
        """Zwraca współrzędne wierzchołka paraboli."""
        if self.a == 0:
            return "To nie jest parabola (a=0). Wierzchołek nie jest zdefiniowany."

        x_vertex = -self.b / (2 * self.a)
        y_vertex = self.calculate_value(x_vertex)
        return f"Wierzchołek paraboli: ({x_vertex}, {y_vertex})"
#Zadanie 4.
#Zdefiniuj klasę DNAseq, która będzie zawierała metody działające na sekwencjach nukleotydowych. Klasa ta powinna zawierać takie funkcjonalności jak:

#wyświetlanie sekwencji w formacie FASTA
#wyznaczanie sekwencji komplementarnej
#wyznaczanie sekwencji odwrotnie komplementarnej
#translację sekwencji na sewkencje aminokwasową (o ile to możliwe)
#sprawdzanie czy w sekwencji znajduje sie zadana podsekwencja
#dodawanie dwóch sekwencji (rozumiane jako konkatenacja) nazw i sekwencji
#zapisywanie sekwencji do pliku w formacie FASTA
codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_STOP', 'TAG':'_STOP',
        'TGC':'C', 'TGT':'C', 'TGA':'_STOP', 'TGG':'W'}
class DNAseq:

    def __init__(self, name, seq):
        self.name = name
        self.seq = seq.upper()

    def __repr__(self):
        return f">{self.name}\n{self.seq}"

    def __add__(self, other):
        new_name = self.name + "_" + other.name
        new_seq = self.seq + other.seq
        return DNAseq(new_name, new_seq)

    def __len__(self):
        return len(self.seq)

    def __getitem__(self, key):
        new_name = self.name + "_slice"
        return DNAseq(new_name, self.seq[key])

    def __eq__(self, other):
        return self.name == other.name and self.seq == other.seq

    def __contains__(self, value):
        return value in self.seq

    def komplementarna(self):
        comp = self.seq.translate(str.maketrans("ACGT", "TGCA"))
        return DNAseq(self.name + "_comp", comp)

    def odwrotnie_komplementarna(self):
        revcomp = self.seq.translate(str.maketrans("ACGT", "TGCA"))[::-1]
        return DNAseq(self.name + "_revcomp", revcomp)

    def zapisz(self):
        filename = self.name + ".fasta"
        with open(filename, "w") as f:
            f.write(repr(self))

    def sklad(self):
        return {
            "A": self.seq.count("A"),
            "C": self.seq.count("C"),
            "G": self.seq.count("G"),
            "T": self.seq.count("T")
        }
    # codon_lookup.py
    def translacja(self):
      start = seq.find('ATG')
      peptide = []
      i = start
      while i < len(seq)-2:
          codon = seq[i:i+3]
          a = codon_table[codon]
          if a == '*':
              break
          i += 3
          peptide.append(a)
      return ''.join(peptide)
    def doklej(self, x):
        return DNAseq(self.name + "_extended", self.seq + x.upper())
seq = "ATGAAGATATTGGACTATATTCCGGGAAATGCTTTTATGTATCTGA"

# Oczyszczanie sekwencji od innych znaków, pozostawianie tylko A, T, G, C
cleaned_seq = "".join([base for base in seq.upper() if base in ['A', 'T', 'G', 'C']])

dna_object = DNAseq("MySequence", cleaned_seq)
print(f"Sekwencja komplementarna:{dna_object.komplementarna()}")
print(f"Długość sekwencji wynosi : {dna_object.__len__()}")
print(dna_object.sklad())

print(dna_object.__repr__())

print(f"Aminokwasy {dna_object.translacja()}")

