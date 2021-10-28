input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys
import bisect
# input = sys.stdin //расскомментировать при сдаче задачи в системе


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = nums[len(nums) // 2]
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)

n, m = map(int, input.readline().split())
# print(n, m)

a = []
b = []

for i in range(n):
    ai, bi = map(int, input.readline().split())
    a.append(ai)
    b.append(bi)

# print(a, b)

asort = quicksort(a)
bsort = quicksort(b)
# print(asort, bsort)

k = list(map(int, input.readline().split()))

# print(k)

for x in k:
    N = bisect.bisect(asort, x)
    M = bisect.bisect_left(bsort, x)
    print(N - M, end=' ')

#     ai, bi =
#     a.append(ai)
#     b.append(bi)
