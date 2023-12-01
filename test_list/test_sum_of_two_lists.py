"""На вход программе подаются две строки текста, содержащие целые числа.
Из данных строк формируются списки чисел L и M. Напишите программу,
которая создает третий список, элементами которого являются суммы
соответствующих элементов списков L и M.
Далее программа должна вывести каждый элемент полученного списка на одной строке
через 1 пробел."""

"""Примечание. Количество чисел в обеих строках одинаковое."""


def sum_of_two_list(list1, list2):
    list1 = [int(i) for i in list1.split()]
    list2 = [int(i) for i in list2.split()]
    result = []
    for i in range(len(list1)):
        result.append(str(list1[i] + list2[i]))
    return ' '.join(result)


def test_positive_num():
    l = '3 1 4'
    m = '1 5 9'
    assert sum_of_two_list(l, m) == '4 6 13'


def test_identical_num_in_list():
    l = '1 1 1 1 1 1'
    m = '9 9 9 9 9 9'
    assert sum_of_two_list(l, m) == '10 10 10 10 10 10'


def test_negative_num():
    l = '-1 5 -9 4'
    m = '1 -5 9 -4'
    assert sum_of_two_list(l, m) == '0 0 0 0'


def test_large_num():
    l = ('563847 735634 -873453 83475348 23473249 23473 '
         '37432 7474 56656565 -78787878')
    m = ('545454 28374823 723482 827423 234782349 '
         '283423 2734234 74234 47474 474748')
    assert sum_of_two_list(l, m) == ('1109301 29110457 -149971 84302771 258255598 306896 '
                                     '2771666 81708 56704039 -78313130')


def test_empty_lists():
    l = ''
    m = ''
    assert sum_of_two_list(l, m) == ''
