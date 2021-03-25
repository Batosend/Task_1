print('Поддерживаемые операторы: +, -, *, /, %, **')
print('Вводи через пробел')
while True:
    inp = input(">> ")
    inp.split(' ')
    ar_len = len(inp)
    print(inp)
    if ar_len == 1 and inp.isdigit() is True:
        first_num = inp
    elif ar_len == 2 and inp[0].isdigit() is False:
        operator = inp[0]
        sec_num = inp[1]
        if inp[0] != '+' :
            print('Введи нормальное выражение')
        elif inp[0] != '-':
            print('Введи нормальное выражение')
        elif inp[0] != '*':
            print('Введи нормальное выражение')
        elif inp[0] != '/':
            print('Введи нормальное выражение')
        elif inp[0] != '%':
            print('Введи нормальное выражение')
        elif inp[0] != '**':
            print('Введи нормальное выражение')

    elif inp == "=":
        res = first_num + operator + sec_num
        res_n = eval(res)
        print(res_n)
        break
    else:
        print('Введи нормальное выражение')
