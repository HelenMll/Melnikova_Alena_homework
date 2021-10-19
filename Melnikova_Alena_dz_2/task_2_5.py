start_list = [86.42, 7.981, 98.36, 8.72, 59, 6, 1.65, 283.76, 534, 607, 63.46, 51, 72, 8.049, 236.1, 50.3275, 91, 75.2, 374, 63.70]
proof = id(start_list)

# Часть А

price_list = []

for price in start_list:
    price = str(price)
    splitted = price.split('.')
    if len(splitted) == 1:
        price_list.append(f'{int(splitted[0]):02d} руб. 00 коп.')
    else:
        price_list.append(f'{int(splitted[0]):02d} руб. {int(splitted[1]):02d} коп.')
stroke = ', '.join(price_list)
print('\nСписок цен:')
print(stroke)

# Часть В

start_list.sort()
print('\nСписок цен по возрастанию:')
print(start_list)
if proof == id(start_list):
    print('*id списка соответствует изначальному')

# Часть С

new_list = list(reversed(start_list))
print('\nСписок цен по убыванию:')
print(new_list)
if proof != id(new_list):
    print('*id списка не соответствует изначальному')

# Часть D

print('\n5 самых дорогих товаров:')
print(new_list[:5])