# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого
# из чисел в интервале от 1 до 100

numbers = []
x = 1

while x <= 100:  # создаем список из 100 чисел
    numbers.append(x)
    x += 1

for counter in numbers:
    if 11 <= numbers[counter - 1] <= 19:  # создаем исключение для чисел от 11 до 19
        print(numbers[counter - 1], 'процентов')
    else:
        y = str(numbers[counter - 1])  # переводим текущее число в строку
        pointer = int(y[-1])  # считываем последний символ
        if pointer == 1:
            print(y, 'процент')
        elif pointer == 2 or pointer == 3 or pointer == 4:
            print(y, 'процента')
        else:
            print(y, 'процентов')
