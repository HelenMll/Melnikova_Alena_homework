a = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
b = ['15 * 3', '15 / 3', '15 // 2', '15 ** 2']
for digit_order, results in enumerate(a):
    if type(results) == int:
        print('Тип результата выражения {} - целое число.'.format(b[digit_order]))
    else:
        print('Тип результата выражения {} не является целым числом.'.format(b[digit_order]))
