# saper-project

Przygotowanym przez nas projektem jest gra "Saper" realizowana w Pythonie. Celem gry jest odkrycie wszystkich pól na planszy, które nie ukrywają min, przy jednoczesnym oznaczaniu podejrzanych miejsc za pomocą flag. Zamiast działania w konsoli, gra uruchamia się w dedykowanym, czytelnym okienku graficznym zrealizowanym przy użyciu biblioteki Pygame, co zapewnia płynną i komfortową rozgrywkę za pomocą myszki.
Główne funkcjonalności które wprowadzimy do projektu:
- Podczas rozgrywki lewym przyciskiem myszy będziemy odkrywać pola na planszy, a prawym oznaczać flagi
- W menu będzie można wybrać 3 poziomy trudności, z czego każdy kolejny poziom zwiększa rozmiar planszy oraz ilość bomb, która się na niej znajduje
- Podczas rozgrywki na ekranie będzie widoczny zegar, który liczby czas w sekundach
- Jeśli osiągniemy rekord czasowy w danym poziomie trudności, wynik zapisze się i będzie widoczny w menu
- Podczas rozgrywki będzie również widoczny inny licznik - licznik pozostałych flag, które mamy do użycia

Wstępnie opisaliśmy jakie klasy będą znajdywać się w naszym projekcie (lub nie, jeżeli z jakiegoś pomysłu zrezygnujemy, albo zdecydujemy się go rozwiązać w inny sposób):
- Klasa pola: Przechowuje stan pojedynczego kwadraciku (czy jest miną, czy jest odkryty, oznaczony flagą, liczba sąsiadujących min)
- Klasa planszy: Tworzy dwuwymiarową macierz pól i obsługuje trzy różne rozmiary map
- Klasa rekordów: Odpowiada za całą logikę związaną z najlepszymi czasami, obsługuje odczyt i zapis rekordów do pliku zewnętrznego, sprawdza czy obecny czas gracza jest nowym rekordem, i przesyła te dane do wyświetlenia
- Klasa menu: Zarządza ekranem startowym, na którym gracz wybiera jeden z trzech rozmiarów map
- Klasa interfejsu graficznego: Odpowiada za wizualizację w Pygame, czyli rysowanie pól, min, flag, zegara, itp.
- Klasa wyjątków

Jak zaznaczyliśmy, jest to nasza wstępna koncepcja, zatem wraz z rozwojem projekty możemy uznać że klas należy zrobić więcej.
