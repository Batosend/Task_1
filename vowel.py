print("Для завершения работы отправьте =")
text = input("Введите текст: ")
while text != '=':
    text = text.lower()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    y = 0
    for n in range(len(text)):
        if text[n] == 'a':
            a += 1
        elif text[n] == 'e':
            e += 1
        elif text[n] == 'i':
            i += 1
        elif text[n] == 'o':
            o += 1
        elif text[n] == 'u':
            u += 1
        elif text[n] == 'y':
            y += 1
    print("В данном тексте a = " + str(a) + "; e = " + str(e) + "; i = " + str(i) + "; o = " + str(o) + "; u = " + str(
        u) + "; y = " + str(y))
    print("Для завершения работы отправьте =")
    text = input("Введите текст: ")
