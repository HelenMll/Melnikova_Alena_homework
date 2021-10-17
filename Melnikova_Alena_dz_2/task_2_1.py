a = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
b = ['15 * 3', '15 / 3', '15 // 2', '15 ** 2']
for digit_order, results in enumerate(a):
    if type(results) == int:
        print('Тип результата выражения', b[digit_order], '- целое число.')
    else:
        print('Тип результата выражения', b[digit_order], 'не является целым числом.')
