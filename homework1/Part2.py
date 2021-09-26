# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число
# «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

x = 1
odds = []  # создаем пустой список, который станет основой

while x < 1000:  # перебираем все числа до 1000, вычленяя нечетные
    y = x % 2
    if y == 0:
        x = x + 1
    else:
        odds.append(x)
        x = x + 1
print('Нечетные числа:')
print(odds)

massive = len(odds)  # задаем параметр, чтобы пройтись по каждому элементу списка
while massive > 0:
    x = odds[massive - 1] ** 3  # возводим элемент в 3ю степень
    odds.append(x)  # добавляем степень к списку
    del odds[massive - 1]  # удаляем число-основу
    massive = massive - 1  # повторяем все на пункт ниже, пока список не кончится
print('Кубы нечетных чисел:')
print(odds)

massive = len(odds)  # возвращаем значение по длине массива

while massive > 0:
    number = str(odds[massive - 1])  # превращаем элемент списка в строку
    mass_number = len(number)  # получаем длину строки
    pieces_sum = 0
    while mass_number > 0:  # проходим по каждому символу
        piece = int(number[mass_number - 1])  # возвращаем элемент числа к int
        pieces_sum = pieces_sum + piece  # суммируем каждый элемент числа между собой
        mass_number = mass_number - 1  # опускаемся на число ниже
    if pieces_sum % 7 == 0:  # если сумма чисел числа делется без остатка
        massive = massive - 1  # опускаемся ниже
    else:  # иначе
        del odds[massive - 1]  # удаляем число-основу
        massive = massive - 1  # опускаемся ниже
print('Числа, суммы элементов которых делятся на 7 без остатка:')
print(odds)

massive = len(odds)  # возвращаем значение по длине массива
end_sum1 = 0

while massive > 0:  # считаем сумму чисел в списке
    end_sum1 = end_sum1 + odds[massive - 1]
    massive = massive - 1

print('Сумма данных чисел:')
print(end_sum1)

massive = len(odds)  # возвращаем значение по длине массива

while massive > 0:
    q = odds[massive - 1] + 17  # прибавляем последовательно к каждому элементу 17
    odds.append(q)  # добавляем в список новое число
    del odds[massive - 1]   # удаляем старое
    massive = massive - 1   # опускаемся ниже
print('Числа, увеличенные на 17:')
print(odds)

massive = len(odds)  # возвращаем значение по длине списка

while massive > 0:
    number = str(odds[massive - 1])  # превращаем элемент списка в строку
    mass_number = len(number)  # получаем длину строки
    pieces_sum = 0
    while mass_number > 0:  # проходим по каждому символу
        piece = int(number[mass_number - 1])  # возвращаем элемент числа к int
        pieces_sum = pieces_sum + piece  # суммируем каждый элемент числа между собой
        mass_number = mass_number - 1  # опускаемся на число ниже
    if pieces_sum % 7 == 0:  # если сумма чисел числа делется без остатка
        massive = massive - 1  # опускаемся ниже
    else:  # иначе
        del odds[massive - 1]  # удаляем число-основу
        massive = massive - 1  # опускаемся ниже
print('Числа больше на 17, суммы элементов которых делятся на 7 без остатка:')
print(odds)

massive = len(odds)  # возвращаем значение по длине массива
end_sum1 = 0

while massive > 0:  # считаем сумму чисел в списке
    end_sum1 = end_sum1 + odds[massive - 1]
    massive = massive - 1

print('Сумма данных чисел:')
print(end_sum1)
