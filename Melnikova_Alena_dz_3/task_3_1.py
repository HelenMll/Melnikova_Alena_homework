en_rus_dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate_adv(word):
    if word.istitle() == True:
        print(en_rus_dictionary.get(word.lower(), 'Ошибка ввода').capitalize())
    else:
        print(en_rus_dictionary.get(word, 'Ошибка ввода'))

num_translate_adv(input())