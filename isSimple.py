while True:
    inp = input(">> ")
    if inp.isdigit() is False:
        print('Введите число')
    else:
        num = int(inp)
        flag = False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    flag = True
                    break
        if flag:
            print(num, "не простое число")
        else:
            print(num, "простое число")


