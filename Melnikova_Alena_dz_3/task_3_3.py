from random import shuffle
from random import choice

def get_jokes(doubles, num):

    """Функция для шуток"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if doubles == 'yes':
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for nouns, adverbs, adjectives in zip(nouns, adverbs, adjectives):
            print(f'{nouns} {adverbs} {adjectives}')
    elif doubles == 'no':
        num = int(num)
        while num > 0:
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            num -= 1
    else:
        print('Некорректный ввод')

print('Запретить повторять слова шутки? yes/no\nЕсли нет, то сколько шуток необходимо?')
get_jokes(input(), input())
