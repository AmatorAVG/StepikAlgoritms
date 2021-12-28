input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys

# input = sys.stdin //расскомментировать при сдаче задачи в системе


W, n = map(int, input.readline().split())
print(W, n)
w = list(map(int, input.readline().split()))
print(w)

F = [0] * (W + 1)
F[0] = 1
Prev = [0] * (W + 1)
for i in range(len(w)):
    for k in range(W, w[i] - 1, -1):
        if F[k - w[i]] == 1:
            F[k] = 1
            Prev[k] = w[i]
i = W
while F[i] == 0:
    i -= 1

print(i)
