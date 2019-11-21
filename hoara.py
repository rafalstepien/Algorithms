import random
from quick_sort import partition, partition_first, partition_median, partition_rand, partition_last


def select(lst, start, stop, k, fun):
    pivot_index = fun(lst, start, stop)
    if k == pivot_index:
        return lst[k]
    elif k < pivot_index:
        return select(lst, start, pivot_index - 1, k, fun)
    else:
        return select(lst, pivot_index + 1, stop, k, fun)


sort_list = [1, 9, 7, 2, 5, 8, 3, 6, 4]
low = 0
high = len(sort_list) - 1

print(select(sort_list, low, high, 4, partition_median))
