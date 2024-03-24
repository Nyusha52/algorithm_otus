import random

from time_ import time_


@time_
def bubble_sort(lst):
    sorted_index = len(lst)
    while True:
        number_of_swap = 0
        for i in range(0, sorted_index - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                number_of_swap += 1
        sorted_index -= 1
        if number_of_swap == 0:
            break
    return lst


l1 = [random.randint(1, 100) for _ in range(10)]
l2 = [random.randint(1, 10 ** 2) for _ in range(10 ** 2)]
l3 = [random.randint(1, 10 ** 3) for _ in range(10 ** 3)]
l4 = [random.randint(1, 10 ** 4) for _ in range(10 ** 4)]
l5 = [random.randint(1, 10 ** 5) for _ in range(10 ** 5)]

print(l1)
print(bubble_sort(l1))
bubble_sort(l2)
bubble_sort(l3)
bubble_sort(l4)
bubble_sort(l5)

'''
10 ** 2 - 0:00:00
10 ** 3 - 0:00:00.085993
10 ** 4 - 0:00:08.817013
10 ** 5 - 0:17:32.279573
'''
