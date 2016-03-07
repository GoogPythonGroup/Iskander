# coding=utf-8

# массив состоящий из многих слов

d = "lorem ipsumally doloring loremlor ipsum dolor transformatically"
x = d.split()

# поиск для самого длинного слова в строке

print max(x)

# поиск для самого длинного слова в строке разделенного точкой запятой

t = "lore;psumally;doloring;loremlor;ipsum;dolor;transformsecond"
myVar = t.split(';')
print max(myVar)

# Написать программу самого короткого слова который выделяется знаком который пользователь вводит в интерактивном режиме

lorem = "Lorem ipsum dolor si! amet, consectetur adipisicing elit. Deleniti, inventore!"
symbol = raw_input('Введите символ по которому нужно разделить данный тест: ')
loremSplit = lorem.split(symbol)
print min(loremSplit)

# Написать программу которое находит введенное слово в строке которое также вводится пользователем в интерактивном режиме

spongeBob = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Placeat, neque."
userWord = raw_input("Введите слово которое нужно найти в тексте: ")
spongeBobCount = spongeBob.split()
result = "Всего таких слов в тексте: "
print(spongeBob.find(userWord))

# Посчитать количество слов в предложении которое вводит пользователь

test = raw_input("Введите свое предложение: ")
testCount = str(len(test.split()))
text = "количество введенных вами слов: "
print text + testCount

