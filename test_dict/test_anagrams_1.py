"""Анаграмма – слово (словосочетание), образованное путём перестановки
букв, составляющих другое слово (или словосочетание). Например,
английские слова evil и live – это анаграммы.

На вход программе подаются два слова.
Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае."""


def anagrams(word_1, word_2):
    dic_word_1 = {}
    dic_word_2 = {}
    for i in list(word_1):
        dic_word_1[i] = dic_word_1.get(i, 0) + 1
    for i in list(word_2):
        dic_word_2[i] = dic_word_2.get(i, 0) + 1
    if dic_word_1 == dic_word_2:
        return "YES"
    else:
        return "NO"


def test_anagram():
    assert anagrams("thing", "night") == "YES"


def test_not_anagram():
    assert anagrams("cat", "rat") == "NO"


def test_different_num_letters():
    assert anagrams("aaa", "aa") == "NO"


def test_repeating_letters_yes():
    assert anagrams("aaab", "baaa") == "YES"


def test_repeating_letters_no():
    assert anagrams("aaab", "baab") == "NO"
