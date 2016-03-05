# coding=utf-8
# Задание 1

x = int(raw_input('Введите число от 0 до 9 '))
if 1 <= x <= 3:
    s = raw_input('Введите строку ')
    n = int(raw_input('Сколько раз повторить '))
    print n * s
elif 4 <= x <=6:
    m = int(raw_input('В какую степень возвести ваше число? '))
    print x**m
elif 7 <= x <= 9:
    for c in range(10):
        x += 1
        print x
