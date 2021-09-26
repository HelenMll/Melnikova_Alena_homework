#
# Задача 1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#
# Запрашиваем значение duration

duration = int(input('Введите число:'))

# Исходим из того, что 1 минута = 60 секундам,
# 1 час = 3600 секундам
# 24 часа = 86400 секундам

if duration < 60:
    print('Итог:', duration, 'сек')
elif 60 <= duration < 3600:
    minutes = duration // 60
    sec = duration % 60
    print('Итог:', minutes, 'мин', sec, 'сек')
elif 3600 <= duration < 86400:
    hour = duration // 3600
    other = duration % 3600
    minutes = other // 60
    sec = other % 60
    print('Итог:', hour, 'час', minutes, 'мин', sec, 'сек')
else:
    day = duration // 86400
    time = duration % 86400
    hour = time // 3600
    other = time % 3600
    minutes = other // 60
    sec = other % 60
    print('Итог:', day, 'дн', hour, 'час', minutes, 'мин', sec, 'сек')

