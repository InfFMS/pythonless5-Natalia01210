# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint

N = int(input())
m = []
for i in range(N):
    m.append(randint(-1000, 1000))

def F1(m):
    a = []
    b = []
    for i in range(N):
        if (i < N / 2):
            a.append(m[i])
        else:
            b.append(m[i])
    res = a[::-1] + b[::-1]
    return res

def F2(m):
    n = N
    for i in range((N//2)//2):
        m[i], m[(n//2) - 1 - i] = m[(n//2) - 1 - i], m[i]
    for i in range(N//2, N//2 + N//2//2):
        m[i], m[n - (i - (n // 2)) - 1] = m[n - (i - (n // 2)) - 1], m[i]
    return m

#F1 и F2 - две разные функции, решающие одну и ту же задачу
