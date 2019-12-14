import random
import time


def partition(lst, start, stop):
    pivot_index = stop
    pivot_value = lst[pivot_index]

    for i in range(start, stop):
        if lst[i] < pivot_value:
            lst[i], lst[start] = lst[start], lst[i]
            start += 1

    lst[stop], lst[start] = lst[start], lst[stop]
    return start


def quick_sort(lst, start, stop, fun):
    if start < stop:
        border = fun(lst, start, stop)
        quick_sort(lst, start, border - 1, fun)
        quick_sort(lst, border + 1, stop, fun)


def partition_last(lst, start, stop):
    lst[stop], lst[stop] = lst[stop], lst[stop]
    return partition(lst, start, stop)


def partition_rand(lst, start, stop):
    rand_pivot = random.randint(start, stop)
    lst[stop], lst[rand_pivot] = lst[rand_pivot], lst[stop]
    return partition(lst, start, stop)


def partition_first(lst, start, stop):
    lst[stop], lst[start] = lst[start], lst[stop]
    return partition(lst, start, stop)


def partition_middle(lst, start, stop):
    med = (len(lst)) // 2
    lst[stop], lst[med] = lst[med], lst[stop]
    return partition(lst, start, stop)


if __name__ == '__main__':
    sort_list = random.sample(range(100000000), 20000)
    lenght = len(sort_list)
    random.shuffle(sort_list)
    low = 0
    high = len(sort_list) - 1

    t1 = time.perf_counter()
    sort_list1 = sort_list[:]
    quick_sort(sort_list1, low, high, partition_last)
    t2 = time.perf_counter()
    print("Sorted list of size by Last {} in {}".format(lenght, t2 - t1))

    t1 = time.perf_counter()
    sort_list2 = sort_list[:]
    quick_sort(sort_list2, low, high, partition_first)
    t2 = time.perf_counter()
    print("Sorted list of size by First {} in {}".format(lenght, t2 - t1))

    t1 = time.perf_counter()
    sort_list3 = sort_list[:]
    quick_sort(sort_list3, low, high, partition_rand)
    t2 = time.perf_counter()
    print("Sorted list of size by Rand {} in {}".format(lenght, t2 - t1))

    t1 = time.perf_counter()
    sort_list4 = sort_list[:]
    quick_sort(sort_list4, low, high, partition_middle)
    t2 = time.perf_counter()
    print("Sorted list of size by Median {} in {}".format(lenght, t2 - t1))
