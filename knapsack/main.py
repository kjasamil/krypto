# piękny wzorzec na interfejs zrobiony w paincie masz w obrazku gui.png

# Do kluczy musisz zrobić dwie sekcje:
# 1. sekcja na klucz publiczny. Jedno pole tekstowe nazwane 'a'' (a prim)
# 2. sekcja na klucz prywatny. Trzy pola tekstowe, jedno nazwane 'a', drugie nazwane M, trzecie nazwane W
# miejsce na wpisanie a i a` powinno być największe
# wraz z uruchomieniem programu tworzysz obiekt klasy Knapsack
# robisz coś w podobie DESX, umożliwiamy szyfrowanie z okna i z pliku binarnie
# jeżeli szyfrujemy/deszyfrujemy tekst to do metody encrypt/decrypt podajemy stringa z flagą isText = True
# w przeciwnym wypadku odczytujemy binarnie zawartość pliku i podajemy ją do tych metod z flagą isText = False
# czyli tak jak było to w DESX
# pamiętaj aby zaszyfrowany plik zapisać BINARNIE

# dodatkowa modyfikacja względem przykładowego programu to dodanie przycisku do generowania klucza publicznego
# pobierasz z pól tekstowych z sekcji klucza prywatnego a, M i W i podajesz je do metody generate_public_key()
# zwróci ci klucz publiczny w postaci stringa, który musisz wpisać do pola tekstowego z a'

# ma być też przycisk do generowania kluczy, po generowaniu kluczy aktualizujemy wszystkie pola w obu sekcjach

# przed próbą szyfrowania/deszyfrowania musisz zawsze wywołać metodę set_keys na obiekcie Knapsack w podany sposób:
# [nazwa_obiektu].set_keys(a, a_prim, m_val, w_val)
# jako argumenty podajesz stringi odczytane z odpowiednich pól tekstowych, kolejno a, a', M, W
# robisz to w bloku try, fajnie jak skorzystasz z funkcji z wyskakującym okienkiem do informowania o błędzie jak w DESX

# napisz metody do zapisywania/odczytywania kluczy z pliku z podziałem na publiczne i prywatne
# czyli tak właściwie powinny być 4 przyciski - zapisz klucz publiczny, odczytaj klucz publiczny, zapis klucz prywatny,
# odczytaj klucz prywatny, miejsce na nazwę pliku powinno być jedno
# zapisujesz klucz publiczny po prostu zapisując string z a' do pliku
# zapisujesz klucz prywatny wg podanego wzoru
# string z a
# string z M
# string z W
# wszystkie stringi w osobnych liniach, czyli dostajesz 3 linie

# w przypadku szyfrowania/deszyfrowania plików również ma być modyfikacja
# zamiast przycisków do zapisywania/odczytywania plików z tekstem jawnym/szyfrogramem wstaw po prostu pola tekstowe
# z których będą dopiero pobierane nazwy plików przy szyfrowaniu/deszyfrowaniu jak w DESX, czyli coś jak w DESX,
# tylko bez przycisków, ale zostawiamy oczywiście nazwy pól
