# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from random import randint

def F(a):
    a = str(a)
    for i in range(len(str(a)) - 1):
        if(a[i] != a[i+1]):
            return False
    return True

N = int(input())
m = []
for i in range(N):
    m.append(randint(10, 100000))
res = []
for i in m:
    if(F(i)):
        res.append(i)
print(res)