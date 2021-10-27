from random import shuffle
from random import choice

def get_jokes(num):

    """Функция для шуток"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if num == 'y':
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for nouns, adverbs, adjectives in zip(nouns, adverbs, adjectives):
            print(f'{nouns} {adverbs} {adjectives}')
    elif num == 'n':
        counter = 4
        while counter >= 0:
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            counter -= 1
    else:
        print('Некорректный ввод')

print('Запретить повторять слова шутки? y/n')
get_jokes(input())
