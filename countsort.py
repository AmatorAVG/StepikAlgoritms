input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys

M = 10000
n = int(input.readline())
A = list(map(int, input.readline().split()))

# print(n)
# print(A)
B = [0] * M
AS = [0] * n
# print(B)
for j in range(n):
    B[A[j]-1] += 1

# print(B)
# B[0] = 0
for i in range(1, M):
    B[i] += B[i-1]
# print(B)

for j in range(n, 0, -1):

    AS[B[A[j-1]-1]-1] = A[j-1]
    B[A[j-1]-1] -= 1
print(*AS)