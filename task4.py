# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
from sympy.core.random import randint

N = int(input())
m = []
sum = 0
for i in range(N):
    m.append(randint(0, 1000))
    sum += m[-1]
sum /= len(m)
t1, t2 = sum - (sum * 0.3), sum + (sum * 0.3)
res = []
for i in m:
    res.append(i)
for i in range(len(m)):
    if(t1 > m[i] or t2 < m[i]):
        res.remove(m[i])
print(res)
