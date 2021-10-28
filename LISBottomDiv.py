input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys


n = int(input.readline())
A = list(map(int, input.readline().split()))

D = [1] * n
for i in range(n):
    for j in range(i):
        if A[i] % A[j] == 0 and D[j]+1 > D[i]:
            D[i] = D[j] + 1
ans = 0
for i in range(n):
    ans = max(ans, D[i])
print(ans)
