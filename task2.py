def get_count_char(str_):
    letter_count = {}
    str_ = str_.lower()
    for i in range(len(str_)):
        if str_[i].isalpha():
            if not letter_count.keys().__contains__(str_[i]):
                letter_count[str_[i]] = 0
            letter_count[str_[i]] += 1

    return letter_count


def get_percent_char(letter_count):
    count_of_letters = 0
    letter_count_keys = letter_count.keys()
    letter_percent = {}
    for el in letter_count_keys:
        count_of_letters += letter_count[el]
    for el in letter_count_keys:
        letter_count[el] = (letter_count[el] / count_of_letters) * 100
    return letter_percent


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

list_of_words = main_str.split(' ')
list_of_words.sort()
sub_str = "".join(list_of_words)
print(get_count_char(main_str))
