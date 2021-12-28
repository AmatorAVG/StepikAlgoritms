input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys

# input = sys.stdin //расскомментировать при сдаче задачи в системе

n = int(input.readline())
a = list(map(int, input.readline().split()))

d = [0] * n
d[0] = a[0]
if n == 1:
    print(d[0])
else:
    d[1] = max(0,d[0])+a[1]
    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2]) + a[i]
    print(d[n-1])
