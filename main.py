
input = open('1.txt', 'r')  # расскомментировать решая задачу локально
import sys
# input = sys.stdin //расскомментировать при сдаче задачи в системе


def div_array(big_list, inv_count):
    length = len(big_list)//2
    l_ar = big_list[:length]
    r_ar = big_list[length:]
    print(l_ar)
    print(r_ar)
    if len(l_ar) > 1:
        l_ar, inv_count = div_array(l_ar, inv_count)
    if len(r_ar) > 1:
        r_ar, inv_count = div_array(r_ar, inv_count)
    return merge_sort(l_ar, r_ar, inv_count)


def merge_sort(l_ar, r_ar, inv_count):

    res = []
    l_ind = 0
    r_ind = 0
    len_l_ar = len(l_ar)
    len_r_ar = len(r_ar)

    for i in range(len_l_ar + len_r_ar):
        if r_ind == len_r_ar:
            res.append(l_ar[l_ind])
            l_ind += 1
        elif l_ind == len_l_ar:
            res.append(r_ar[r_ind])
            r_ind += 1
        elif l_ar[l_ind] < r_ar[r_ind]:
            res.append(l_ar[l_ind])
            l_ind += 1
        else:
            res.append(r_ar[r_ind])
            r_ind += 1
            inv_count += 1

    # if l_ar < r_ar:
    #     return [l_ar[0], r_ar[0]]
    # else:
    #     return [r_ar[0], l_ar[0]]
    # print(res)
    return res, inv_count


    # return l_ar, r_ar


n = int(input.readline())
col = list(map(int, input.readline().split()))
print(n)
print(col)
sort_ar, inv_count = div_array(col, 0)
print(sort_ar, inv_count)
