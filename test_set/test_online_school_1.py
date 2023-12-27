"""Онлайн-школа BEEGEEK 1

При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует
не только профессиональные качества кандидата, но и его память.

Кандидату показывают ненадолго несколько различных чисел, а затем кандидат
должен их назвать. Причем неважно, в каком порядке он их вспоминает, и
повторяется он или нет, главное он должен назвать все числа, не добавляя лишних.

Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.

Формат входных данных
На вход программе подаются две строки с числами: в первой строке показанные
кандидату, а во второй ответы кандидата.

Формат выходных данных
Программа должна вывести YES, если кандидат прошел испытание и его
можно брать на работу и NO в противном случае."""


def memory_testing(numbers, answer):
    numbers = set(numbers.split())
    answer = set(answer.split())
    if numbers == answer:
        return 'YES'
    else:
        return 'NO'


def test_one_num_correct():
    numbers = '10'
    answer = '10'
    assert memory_testing(numbers, answer) == 'YES'


def test_one_num_incorrect():
    numbers = '8'
    answer = '9'
    assert memory_testing(numbers, answer) == 'NO'


def test_disorder_num():
    numbers = '1 2 3 4 5'
    answer = '2 5 4 3 1'
    assert memory_testing(numbers, answer) == 'YES'


def test_repetitive_num():
    numbers = '1 2 3 4 8 5'
    answer = '1 2 8 2 3 4 5 2 4 4'
    assert memory_testing(numbers, answer) == 'YES'


def test_missed_num():
    numbers = '14 64 34 34 34 34 87 100'
    answer = '100 14 64 34 100'
    assert memory_testing(numbers, answer) == 'NO'


def test_extra_num():
    numbers = '8 7'
    answer = '9 7 7 8'
    assert memory_testing(numbers, answer) == 'NO'


def test_negative_num_correct():
    numbers = '-2 47 -50 234 -594 5'
    answer = '5 234 -50 5 47 -2 -594'
    assert memory_testing(numbers, answer) == 'YES'


def test_negative_num_incorrect():
    numbers = '-2 47 -50 92 -9 234 -594 5'
    answer = '5 -596 234 92 -9 -50 5 47 -2 -594'
    assert memory_testing(numbers, answer) == 'NO'


def test_negative_positive_num():
    numbers = '-2'
    answer = '2'
    assert memory_testing(numbers, answer) == 'NO'


def test_positive_negative_num():
    numbers = '2'
    answer = '-2'
    assert memory_testing(numbers, answer) == 'NO'



