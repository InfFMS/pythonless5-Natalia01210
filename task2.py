# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5
from random import randint

N = int(input())
m = []
for i in range(N):
    m.append(randint(0, 5))
print(m)
for i in range(1, len(m)):
    if(m[i] == m[i-1]):
        print('значение:' + str(m[i]) + ' индексы ' + str(i-1) + ' и ' + str(i))