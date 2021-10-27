# theasurus_adv
# Иван Сергеев, Инна Серова, Петр Алексеев, Илья Иванов, Анна Савельева

def theasurus(*args):
    employee_thea = {}
    ppl_list = str(*args).split(', ')
    for ppl in ppl_list:
        first_lit = str(ppl)[0]
        employee_thea[first_lit] = employee_thea.get(first_lit, []) + [ppl]
    print(employee_thea)

print('Пожалуйста, введите ФИО сотрудников через запятую:')
theasurus(input())
