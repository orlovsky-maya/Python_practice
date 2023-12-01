"""На вход программе подается строка текста.
Напишите программу, которая выводит индекс второго вхождения буквы «f». 
Если буква «f» встречается только один раз, выведите число −1,
а если не встречается ни разу, выведите число −2."""
import pytest


def index_second_occurrence(text):
    c = text.count('f')
    if c < 2:
        return c - 2
    return text.replace('f', '1', 1).find('f')


@pytest.mark.smoke
def test_two_occur():
    assert index_second_occurrence('affective') == 2


@pytest.mark.smoke
def test_one_occur():
    assert index_second_occurrence('father') == -1


@pytest.mark.smoke
def test_no_occur():
    assert index_second_occurrence('python') == -2


@pytest.mark.smoke
def test_all_symbol_match():
    assert index_second_occurrence('ffffffffff') == 1


@pytest.mark.smoke
def test_only_last_symbol_match():
    assert index_second_occurrence('aaaaaaaaaaf') == -1


@pytest.mark.smoke
def test_two_last_symbol_match():
    assert index_second_occurrence('aaaaaaaaaaff') == 11


@pytest.mark.regression
def test_first_and_last_symbol_match():
    assert index_second_occurrence('faaaaaaaaaaf') == 11


@pytest.mark.regression
def test_alternated_symbol_match():
    assert index_second_occurrence('afafafafafaf') == 3


@pytest.mark.regression
def test_empty_string():
    assert index_second_occurrence('') == -2
