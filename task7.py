# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
from random import randint

N = int(input())
m = []
for i in range(N):
    m.append(randint(-100, 100))
res = []
for i in m:
    if(i > 0):
        res.append(i)
for i in m:
    if(i <= 0):
        res.append(i)
print(res)