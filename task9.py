# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
from random import randint

N = int(input())
m = []
for i in range(N):
    m.append(randint(-100, 100))
res = []
for i in range(len(m)):
    if(m.index(m[i]) == i):
        res.append(m[i])
print(m)
print(res)