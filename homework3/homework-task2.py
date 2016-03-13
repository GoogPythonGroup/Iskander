# coding=utf-8
# 2. Переписать задание из первого урока переведя все проверки в функции


x = int(raw_input('Введите число  от 0 до 9 '))

def multiply(x,y):
    print x*y

def involution(x,y):
    print x**y

def lastFunc(x):
    for t in range(x, x+10, 1):
        print t

if x <= 3:
    q = raw_input('Введите строку ')
    w = int(raw_input('Сколько раз повторить '))
    multiply(q,w)
elif x <= 6:
    m = int(raw_input('В какую степень возвести ваше число? '))
    involution(x,m)
elif x <= 9:
    lastFunc(x)
else:
    print 'Вы не правильно ввели'