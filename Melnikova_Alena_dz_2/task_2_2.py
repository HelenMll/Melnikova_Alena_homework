start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
proof = id(start_list)

for items_order, items in enumerate(start_list):
    if items.isdigit() == True:  # вычленяем целые числа
        start_list[items_order] = f' "{int(items):02d}" '  # заменяем полностью элемент списка
    elif items[0] == '+' and items[1:].isdigit() == True:  # вычленяем числа с +
        start_list[items_order] = f' "{int(items):+03d}" '
    elif items[0] == '-' and items[1:].isdigit() == True:  # вычленяем числа с -
        start_list[items_order] = f' "{int(items):-03d}" '
    print(start_list[items_order], end=' ')

if id(start_list) == proof:
    print('\n', 'Список не был изменен.')
