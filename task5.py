# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
N = int(input())
if(N == 0):
    print(0)
    exit()
now = int(input())
m = []
m.append(now)
mxcnt = 1
mx = now
for i in range(N):
    now = int(input())
    m.append(now)
    if(mx == now):
        mxcnt += 1
    elif(mx < now):
        mxcnt = 1
        mx = now
print(mxcnt)
