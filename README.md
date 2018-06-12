# Jak uruchomić stronę:

## Zależności
- Python 3.6
- pip install aiohttp
- pip install cchardet
- pip install aiodns
- pip install aiohttp-jinja2

## Aby uruchomić 
- python main.py


# Cel
Celem zadania jest przetestowanie mechanizmów wyszukiwania przybliżonego w tekście oraz zaprojektowanie wyszukiwarki.

Przygotowanie
Na stronie

http://www.gutenberg.org/

znajduje się katalog e-booków. Są one dostępne między innymi w wersji txt i taka nam będzie potrzebna.

Wejdź do katalogu offline:

http://www.gutenberg.org/dirs/

W pliku tym znajduje się indeks wszystkich dostępnych książek. Znajdź tylko książki Polskich autorów. Np pod indeksem 28240 jest angieskie tłumaczenie Pana Tadeusza. Aby dotrzeć do pliku potrzebna jest ścieżka

http://www.gutenberg.org/files/28240/

Tam szukamy pliku tekstowego i wybieramy ten, który kodowany jest jako ASCII (zwykle będzie to xxxxx.txt czyli tu 28240.txt).

Utwórz ich własny katalog - plik, który pozwoli Ci dotrzeć do plików (utwórz go osobnym skryptem PHP na dysku swojego serwera).

Przejrzyj kilka książek. Znajdź charakterystyczne miejsca takie jak autor, tytuł, oraz miejsce, gdzie zaczyna się i kończy właściwy tekst książki. Zwróć uwagę na to, że tekst jest rozdzielony na linie.

Przestudiuj algorytmy wyszukiwania dokładnego i przybliżonego w tekście. Algorytmy wyszukiwania dokładnego bazują na wyrażeniach regularnych. Algorytmy wyszukiwania przybliżonego to: LCS, soundex, metaphone, similar_text, levenshtein.

Treść ćwiczenia
Zaprojektuj wyszukiwarkę internetową działającą dla projektu gutenberg w sposób dokładny i przybliżony.

Wykonanie
Formularz zawiera następujące pola:

pole tekstowe do wpisania frazy
lista rozwijalna, z której będziemy wybierać typ wyszukiwania (dokładne lub z użyciem jednego z algorytmów przybliżonych)
Przycisk wyślij
Wydruk rezultatów:
W postaci listy. W przypadku wyszukiwania dokładnego - w kolejności znalezienia, w przypadku wyszukiwania przybliżonego - 10 najlepszych wyników w kolejności malejącego podobieństwa.

Element listy wygląda następująco:

Autor i tytuł
Odsyłacz (adres URL)
Nr linii (w przypadku dopasowania dokładnego podajemy pierwsze wystąpienie, w przypadku przybliżonego - pierwsze najlepsze dla danego pliku)
3 Linie tekstu: poprzedzająca, linia ze znalezioną frazą, linia następna.
Dodatkowym atutem będzie zastosowanie technologii Ajax i JQuery - np zastosowanie tabelki jquery, pokazywanie paska postępu przeszukiwania.

Działanie wyszukiwarki:
Zakładamy, że program nie korzysta z bazy danych ani z indeksu słów.

Utworzyliśmy jednak listę adresów URL wszystkich plików z autorami i książkami , co usprawni nieco przetwarzanie.

Program przetwarza każdy plik linijka po linijce (przetwarzamy tylko tekst właściwy a nie nagłówek z informacjami o projekcie). W przypadku wyszukiwania dokładnego sprawdzamy wystąpienie wzorca. W przypadku wyszukiwania przybliżonego -  linijkę oraz frazę należy splitować na słowa i przetwarzać słowo po słowie. Wystąpienia fraz (url, nr linii, trafność) należy przechować w tablicy asocjacyjnej, co ułatwi sortowanie po trafności.

Dla wyświetlenia wyników należy ponownie otworzyć plik wg wypełnionej tablicy i odczytać autora oraz tytuł a także trzy odpowiednie linie tekstu.

Wersja uproszczona wyszukiwarki (na ocenę 4)
Wykonaj mechanizm wyszukiwania wpisanej frazy dla pojedynczego adresu URL zawierającego stronę HTML. Wymaga to przefiltrowania formatu HTML na plik tekstowy. Znaczniki łamiące linię (BR, DIV, P, LI, H1 itp) powinny być przekształcone na znak nowej linii.

Podobnie jak w wersji trudniejszej wybieramy rodzaj algorytmu szukającego.

Wyniki wyświetlamy w postaci

Nr linii (w przypadku dopasowania dokładnego podajemy pierwsze wystąpienie, w przypadku przybliżonego - pierwsze najlepsze dla danego pliku)
3 Linie tekstu: poprzedzająca, linia ze znalezioną frazą, linia następna.
