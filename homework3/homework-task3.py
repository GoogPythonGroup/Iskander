# coding=utf-8
# 3. Напишите функцию, которая разбивает введённую строку на слова и выводит
#  по очереди само словo тире ее длина.

def myFunction(x):
    t = x.split()
    for y in t:
        print y + "-" + str(len(y))

x = raw_input('Введите строку ')
myFunction(x)
