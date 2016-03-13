# coding=utf-8
# 1. Переписать первое задание использую генераторы списков

x = int(raw_input('Введите число от 0 до 9 '))
if x <= 3:
    q = raw_input('Введите строку ')
    w = int(raw_input('Сколько раз повторить '))
    for steps in range(w):
        print q
elif x <= 6:
    m = int(raw_input('В какую степень возвести ваше число? '))
    print x**m
elif x <= 9:
    for t in range(x, x+10, 1):
        print t
else:
    print 'Вы не правильно ввели'



