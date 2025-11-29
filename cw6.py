
#Zadanie 1.
#Objaśnij podane wyrażenia regularne i podaj przykład wyrazu, który go spełnia.
#ab*c -> ac,abc, abbc; zero lub więcej wystąpień b
#ab+c -> abc, abbc, abbbbc; przynajmniej jedno występienie b
#ab?c -> ac, abc;  zero lub jedno wystąpienie b
#ab{3}c -> abbbc; dokładnie trzy wystąpienia b
#ab{2,8}c -> abbc, abbbc, abbbbbbbbc; od 2 do 8 wystąpień b
#a.*c -> ac, axc, a123c, abbbbc, abc; a, dowolny znak od zera razy,c
#a.+c -> axc, a1234c, abbbc, abc; a, dowolny znak jeden lub więcej razy,c
#a.?c -> ac, axc; a, dowolny znak zero lub jeden razy,c
#a.{3}c -> a123c, abcdc; a, dowolny znak dokładnie trzy razy,c
#a.{2,8}c -> a12c, a_b_c, a12345678c; a, dowolny znak  od 2 do 8 wystąpień, c
#a[bc]d -> abd, acd; a, dowolny znak z grupy [bc], d
#b[^a]d -> bbd, b1d; b, dowolny znak z wyjątkiem a, d
#^a[bc]d$ -> abd, acd; początek stringa, a, dowolny znak z grupy [bc], d, koniec stringa
#^a[^\s]+ -> abcde, a123_test, a-bc; początek stringa, a,  przynajmniej jedno występienie dowolnego znaku z grupy odwoływanej [^\s] ()

#Zadanie 2.
#Napisz wyrażenie regularne, które ujmuje wszystkie słowa w kolejnych wierszach
import re
wiersz1 = "mama, mem, mom"
wiersz2 = "ac, abc, abbc, abbbc"
wiersz3 = "tab, teb, teab, teaab"
print(f"wszystkie słowa w wierszu1:{re.findall(r"m[aeo]m.*", wiersz1 )}")
print(f"wszystkie słowa w wierszu2:{re.findall(r"ab*c*", wiersz2 )}")
print(f"wszystkie słowa w wierszu3:{re.findall(r"t[ae]a*b", wiersz3 )}")
#Zadanie 3.
#Napisz wyrażenie regularne będące odpowiednikiem metod # s.startwith(x),s.endwith(x) ,gdzie s, x -napisy.
s = "adabra kadabra"
print(f"Wyrażenie regularne w stringu {s} będące odpowiednikiem metodzie s.startwith(x):{re.findall(r"^adabra", s)}")
print(f"Wyrażenie regularne w stringu {s} będące odpowiednikiem metodzie s.endwith(x):{re.findall(r"kadabra$", s)}") 
#Zadanie 4.
#Wyznacz wszystkie daty (lata) z poniższego tekstu:
#Marie Sklodowska Curie (1867–1934) was the first person ever to receive two Nobel Prizes: the first in 1903 in physics, shared with Pierre Curie (her husband) and Henri Becquerel for the discovery of the phenomenon of radioactivity, and the second in 1911 in chemistry for the discovery of the radioactive elements polonium and radium.
zad4 = "Marie Sklodowska Curie (1867–1934) was the first person ever to receive two Nobel Prizes: the first in 1903 in physics, shared with Pierre Curie (her husband) and Henri Becquerel for the discovery of the phenomenon of radioactivity, and the second in 1911 in chemistry for the discovery of the radioactive elements polonium and radium."
print(f"Wszystkie daty (lata) z poniższego tekstu:{re.findall(r"(\d{4})", zad4 )}")
#Zadanie 5.
#Napisać wyrażenie regularne, które usuwa wszystkie małe litery z ciągu znaków. Przykładowe działanie tego wyrażenia na "ATTTGgccTaC" powinno zwrócić "ATTTGTC".
zad5 = "ATTTGgccTaC" # powinno zwrócić "ATTTGTC".
zad5_re = re.sub(r"[a-z]", "", zad5)
print(f"Ciąg znaków bez małych liter: {zad5_re}")
#Zadanie 6.
#Napisać wyrażenie regularne, które w zadanym tekście odszuka wszystkie adresy e-mail i zapisze je do listy.
zad6_text = "Genomed S. A., ul. Ponczowa 12, 02-971 Warszawa, tel: +48 22 644 60 19, tel: +48 22 644 60 25, fax: +48 22 644 60 25, email - sekretariat, księgowość: biuro@genomed.pl, email - zamówienia, współpraca, nauka: info@genomed.pl"
m = re.findall(r"(\w+)@(\w+\.\w+)", zad6_text)
#gdy używamy grup, findall zwraca krotki grup
# iteracja przez krotki
if m:
    print("Znalezione adresy e-mail:")
    for username, domain in m:
        print(f"{username}@{domain}")
else:
    print("Nie znaleziono adresów e-mail.")
    #Zadanie 7.
#wczytaj plik zad71_text.txt i wyciągnij wszystkie daty (format YYYY-MM-DD)
with open("zad71_text.txt", "w") as f_dummy:
    f_dummy.write("1763-02-10 roku Wielka Brytania, Francja i Hiszpania podpisały traktat paryski, kończący wojnę siedmioletnią w Ameryce, znaną również jako wojna francusko-indyjska. Na mocy traktatu Wielka Brytania uzyskała rozległe terytoria: całą Kanadę, wszystkie ziemie francuskie na wschód od Missisipi, Florydę, Grenadę, Saint Vincent, Dominikę i Tobago.\n")
    f_dummy.write("1773-05-10 roku brytyjski parlament uchwalił ustawę o herbacie, która przyznała Brytyjskiej Kompanii Wschodnioindyjskiej monopol na handel herbatą w koloniach amerykańskich.\n")
    f_dummy.write("Tralalelo tralala\n")

import re

dates_found = []
with open("zad71_text.txt", 'r') as f:
  for line in f:
    # Odzyskanie dat
    found_dates = re.findall(r"\d{4}-\d{2}-\d{2}", line)
    if found_dates:
        dates_found.extend(found_dates)

print(f"Znalezione daty: {dates_found}")
#zad8
#Napisz wyrażenie regularne, które wykryje daty w dowolnym sensownym formacie,  zamieni je wszystkie na DD-MM-YYYY.
import re

# The regular expression pattern to find dates in YYYY-MM-DD/MM.DD or DD-MM-YYYY/MM.YYYY formats
# Group 1: pierwsza liczba ((d{4} - rok, d{2} - dzień , d-digit)
# Group 2: separator (-, / or .)
# Group 3: 2 cyfry - miesiąc
# Group 4: ostatnia liczba (d{4} - rok, d{2} - dzień )
#Znak \2 zapewnia, że ​​oba separatory w dacie są identyczne.
date_pattern = re.compile(r"(\d{4}|\d{2})([-/., ])(\d{2})\2(\d{4}|\d{2})")

def format_date_to_ddmmyyyy(match):
    """
     funkcja zastępowania dla re.sub, umożliwiająca zmianę formatu dat.
Określa ona oryginalny format (RRRR-MM-DD lub DD-MM-RRRR)
i zwraca datę w formacie DD-MM-RRRR.
    """
    first_part = match.group(1) #  YYYY lub DD
    separator = match.group(2)
    month_part = match.group(3) # Zawsze MM
    last_part = match.group(4)  #  DD lub YYYY

    if len(first_part) == 4: #  YYYY-MM-DD format
        year = first_part
        day = last_part
    else: # DD-MM-YYYY format
        day = first_part
        year = last_part

    return f"{day}-{month_part}-{year}"

text_with_dates = """
10/02/1763  Wielka Brytania, Francja i Hiszpania podpisały traktat paryski, kończący wojnę siedmioletnią w Ameryce, znaną również jako wojna francusko-indyjska. Na mocy traktatu Wielka Brytania uzyskała rozległe terytoria: całą Kanadę, wszystkie ziemie francuskie na wschód od Missisipi, Florydę, Grenadę, Saint Vincent, Dominikę i Tobago.
1773.05.10  brytyjski parlament uchwalił ustawę o herbacie, która przyznała Brytyjskiej Kompanii Wschodnioindyjskiej monopol na handel herbatą w koloniach amerykańskich.
2024-11-25

2024/11/25

25/11/2024

25-11-2024

25.11.2024
"""

#Użycie re.sub z niestandardową funkcją zamiany
converted_text = date_pattern.sub(format_date_to_ddmmyyyy, text_with_dates)

print("Tekst wejściowy:")
print(text_with_dates)
print("\Twkst wyjściowy (DD-MM-YYYY format):")
print(converted_text)
