"""Напишите программу для расшифровки секретного слова методом частотного анализа.

Формат входных данных
В первой строке задано зашифрованное слово. Во второй строке задано одно целое число
n – количество букв в словаре. В следующих n строках записано, сколько раз конкретная
буква алфавита встречается в этом слове – <буква>: <частота>.

Формат выходных данных
Программа должна вывести дешифрованное слово.

Примечание. Гарантируется, что частоты букв не повторяются."""


def secret_word(encr_word, letters):
    cnt_to_letter = {}
    for s in letters:
        a = s.split(':')
        letter = a[0]
        cnt = int(a[1])
        cnt_to_letter[cnt] = letter

    symbol_to_cnt = {}
    for symbol in set(encr_word):
        cnt = encr_word.count(symbol)
        symbol_to_cnt[symbol] = cnt

    decr_word = ''
    for symbol in encr_word:
        cnt = symbol_to_cnt[symbol]
        letter = cnt_to_letter.get(cnt, symbol)
        decr_word += letter

    return decr_word


def test_symbols():
    encr_word = "*!*!*?"
    letters = ['а: 3', 'н: 2', 'с: 1']
    assert secret_word(encr_word, letters) == "ананас"


def test_three_letters():
    encr_word = "pop"
    letters = ['д: 2', 'е: 1']
    assert secret_word(encr_word, letters) == "дед"


def test_six_letters():
    encr_word = "zpwzpz"
    letters = ['б: 3', 'а: 2', 'о: 1']
    assert secret_word(encr_word, letters) == "баобаб"


def test_digits():
    encr_word = "121292"
    letters = ['п: 2', 'а: 3', 'х: 1']
    assert secret_word(encr_word, letters) == "папаха"


def test_one_letter():
    encr_word = "*"
    letters = ['д: 1']
    assert secret_word(encr_word, letters) == "д"


def test_no_letter():
    encr_word = "*!*!*?"
    letters = ['н: 2', 'с: 1']
    assert secret_word(encr_word, letters) == "*н*н*с"


def test_no_one_letter():
    encr_word = "*!*!*?"
    letters = []
    assert secret_word(encr_word, letters) == "*!*!*?"


def test_identical_letter():
    encr_word = "*а*а*?"
    letters = ['а: 3', 'н: 2', 'с: 1']
    assert secret_word(encr_word, letters) == "ананас"
