import calcs

print("Кредитний калькулятор")
while True:
    try:
        credit_sum = float(input('\nВведіть суму кредиту: '))
    except ValueError:
        print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз\n')
    else:
        if (credit_sum > 0):
            break

while True:
    try:
        total_months = int(input('\nВведіть термін кредиту в місяцях: '))
    except ValueError:
        print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз\n')
    else:
        if (total_months > 0):
            break

while True:
    try:
        interest = float(input('\nВведіть відсоток, під який берете кредит: '))
    except ValueError:
        print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз\n')
    else:
        if (interest > 0):
            break

while True:
    try:
        credit_type = int(input('\nВведіть 0 для диференційованих платежів, 1 для ануїтентних: '))
    except ValueError:
        print('Помилка! Ви ввели некоректні дані. Спробуйте ще раз\n')
    else:
        if (credit_type in (0,1)):
            break

if (credit_type == 0):
    result, credit_costs = creditcalc.def_credit(credit_sum, total_months, interest)
else:
    result, credit_costs = creditcalc.anu_credit(credit_sum, total_months, interest)

info = result[0]

print(' | ' + '-' * 9 + ' | ' + '-' * 20 + ' | ' + '-' * 20 + ' | ' + '-' * 20 + ' | ' + '-' * 20 + ' | ')
print(' | ' + "{:^9}".format("Період") + ' | ' + "{:^20}".format("Залишок по кредиту") + ' | ' + "{:^20}".format("Погашення боргу") + ' | ' + "{:^20}".format("Погашення відсотків") + ' | ' + "{:^20}".format("Щомісячний платіж") + ' | ')
print(' | ' + '_' * 9 + ' | ' + '_' * 20 + ' | ' + '_' * 20 + ' | ' + '_' * 20 + ' | ' + '_' * 20 + ' | ')

for id, item in enumerate(info):
    print(' | ' + "{:^9}".format(id + 1) + ' | ' + "{:^20,.2f}".format(round(item[0], 2)) + ' | ' + "{:^20,.2f}".format(round(item[1], 2)) + ' | ' + "{:^20,.2f}".format(round(item[2], 2)) + ' | ' + "{:^20,.2f}".format(round(item[3], 2)) + ' | ')

print("\nПереплата по відсотках за кредит - {:,.2f} грн".format(result[1]))
print("Всього виплат по кредиту - {:,.2f} грн".format(credit_costs))

input()
