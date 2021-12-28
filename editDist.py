import pprint
input = open('1.txt', 'r')
N = input.readline().strip()
M = input.readline().strip()

lN = len(N)
lM = len(M)
# print(N)
# print(M)

D = [[0] * (lN+1) for i in range(lM+1)]

D[0] = [i for i in range(lN+1)]
for j in range(lM+1):
    D[j][0] = j

for i in range(1,lM+1):
    for j in range(1,lN+1):
        # print(i, M[i-1])
        # print(j, N[j-1])
        c = 0 if N[j-1] == M[i-1] else 1
        D[i][j] = min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+c)
        # D[i][j] = 9
        # pprint.pprint(D)
        # print()

# pprint.pprint(D)
print(D[lM][lN])