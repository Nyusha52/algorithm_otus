import random

from time_ import time_


@time_
def insertion_sort(lst):
    for i in range(1, len(lst)):
        paste_element = lst[i]
        while i > 0 and lst[i - 1] > paste_element:
            lst[i] = lst[i - 1]
            i = i - 1
        lst[i] = paste_element
    return lst


l1 = [random.randint(1, 100) for _ in range(10)]
l2 = [random.randint(1, 10 ** 2) for _ in range(10 ** 2)]
l3 = [random.randint(1, 10 ** 3) for _ in range(10 ** 3)]
l4 = [random.randint(1, 10 ** 4) for _ in range(10 ** 4)]
l5 = [random.randint(1, 10 ** 5) for _ in range(10 ** 5)]

# print(l1)
# print(insertion_sort(l1))
# insertion_sort(l2)
# insertion_sort(l3)
# insertion_sort(l4)
# insertion_sort(l5)

'''
[44, 18, 55, 12, 26, 36, 79, 86, 18, 54]
0:00:00
[12, 18, 18, 26, 36, 44, 54, 55, 79, 86]
0:00:00
0:00:00.037999
0:00:04.653017
0:08:45.377736
'''


def binary_search(paste_element, lst, low, high):
    while low <= high:
        mid = (low + high) // 2
        if paste_element > lst[mid]:
            low = mid+1
        else:
            high = mid - 1
    return low

    # так правильно и не заработало
    # if high <= low:
    #     if paste_element < lst[low]:
    #         return low + 1
    #     else:
    #         return low
    #     # return low
    # mid = (low + high) // 2
    # if paste_element > lst[mid]:
    #     return binary_search(paste_element, lst, low=mid+1, high=high)
    # else:
    #     return binary_search(paste_element, lst, low=low, high=mid-1)


@time_
def insertion_sort1(lst):
    for i in range(0, len(lst)):
        paste_element = lst[i]
        p = binary_search(paste_element=paste_element, lst=lst, low=0, high=i-1)
        for j in range(i,  p, -1):
            lst[j] = lst[j -1]
        lst[p] = paste_element
    return lst


print(l1)
print(insertion_sort1(l1))
insertion_sort1(l2)
insertion_sort1(l3)
insertion_sort1(l4)
insertion_sort1(l5)

'''
[95, 99, 61, 43, 4, 97, 24, 41, 84, 40]
0:00:00
[4, 24, 40, 41, 43, 61, 84, 95, 97, 99]
0:00:00
0:00:00.024000
0:00:02.071002
0:04:09.082448
'''