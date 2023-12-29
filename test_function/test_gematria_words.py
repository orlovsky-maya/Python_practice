"""Гематрией слова называется сумма числовых значений входящих в него букв.

Для вычисления гематрии слова в этой задаче:

    переведём слово в верхний регистр;
    числовое значение буквы вычислим как код(буквы) - код(буквы A).

На вход программе подается натуральное число n, а затем n строк английских слов
в разных регистрах.

Напишите программу, которая выводит слова в начальном регистре
(каждое на отдельной строке) в порядке возрастания их гематрии.
Если гематрия слов совпадает, они выводятся в алфавитном (лексикографическом) порядке.

Формат входных данных
На вход программе подается натуральное число n, а затем n строк английских
слов в разных регистрах.

Формат выходных данных
Программа должна отсортировать слова в соответствии с условием задачи.

Примечание 1. Для получения кода символа воспользуйтесь встроенной функцией ord().

Примечание 2. Слова во входных данных могут повторяться.

Примечание 3. Пусть требуется вычислить гематрию слова BaSis.
Переводим его в верхний регистр BASIS.
Для каждого символа в слове находим его код с помощью встроенной функции ord():"""


def gematria(word):
    word = list(word.upper())
    value = sum(list(map(lambda letter: ord(letter) - ord('A'), word)))
    return value


def word_ordering(words):
    words = sorted(words.split())
    words = " ".join(sorted(words, key=gematria))
    return words


def test_gem_matches_low_case():
    words = 'basis after chief agenda'
    assert word_ordering(words) == 'agenda chief after basis'


def test_gem_matches_different_case():
    words = 'Basis afTEr CHief agenda'
    assert word_ordering(words) == 'CHief agenda Basis afTEr'


def test_gem_not_match_different_case():
    words = ('AGreement bAr baRely Barrelbarrier base baseball basIC '
             'basically basis basket')
    assert word_ordering(words) == ('bAr base basIC basis baseball basket baRely '
                                    'basically AGreement Barrelbarrier')


def test_gem_not_match_gem_low_case():
    words = 'afford mother again against age agency agenda'
    assert word_ordering(words) == ('age agenda again afford agency against '
                                    'mother')


def test_repeated_words():
    words = ('basis agree baseBAll chemicAL agenda bAr aFTer chicken Chef '
             'chemical chief CHIcken child baseball')
    assert word_ordering(words) == ('Chef bAr agenda chief agree child aFTer basis '
                                    'CHIcken baseBAll baseball chemicAL chemical '
                                    'chicken')