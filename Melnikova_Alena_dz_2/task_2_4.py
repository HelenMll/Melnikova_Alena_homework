start_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in start_list:
    employee = position.split(' ')
    print('Привет, {}!'.format(employee[-1].capitalize()))
