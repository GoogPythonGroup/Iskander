# coding=utf-8
# Написать функцию в которую можно передать сколько угодно значений и оно
# возводит каждое последующее число в степень предыдущего (первое значение
# возводим в степень один)

def myFunction(*args):
    for index, element in enumerate(args):
        if index > 0:
            x = element ** args[index-1]
            # if x == 0:
            #     x = x + 1
            print x
myFunction(2,3,4,0,7)
