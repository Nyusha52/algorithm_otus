import random
from time_ import time_

@time_
def shell_sort(lst):
    n = len(lst)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

l1 = [random.randint(1, 100) for _ in range(10)]
l2 = [random.randint(1, 10 ** 2) for _ in range(10 ** 2)]
l3 = [random.randint(1, 10 ** 3) for _ in range(10 ** 3)]
l4 = [random.randint(1, 10 ** 4) for _ in range(10 ** 4)]
l5 = [random.randint(1, 10 ** 5) for _ in range(10 ** 5)]
l6 = [random.randint(1, 10 ** 6) for _ in range(10 ** 6)]

print(l1)
print(shell_sort(l1))
shell_sort(l2)
shell_sort(l3)
shell_sort(l4)
shell_sort(l5)
shell_sort(l6)
