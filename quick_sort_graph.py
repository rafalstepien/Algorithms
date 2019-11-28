import random, time, statistics, math
from matplotlib import pyplot as plt
from plot_functions import get_time_per_input_size, plot_time_per_size


def plot_time_iterations_data(no_iterations, list_of_list_of_times): # y - lista czasów
    x = list(range(1, no_iterations+1))
    fig, ax = plt.subplots()
    names_to_legend = ['last', 'first', 'median', 'random']
    for index, times_list in enumerate(list_of_list_of_times):
        ax.plot(x, times_list, label=names_to_legend[index])
    ax.legend()
    plt.show()


def get_data(lista, start, stop, func, iterations):
    times = []
    for i in range(iterations):
        t1 = time.perf_counter()
        quick_sort(lista, start, stop, func)
        times.append(time.perf_counter() - t1)
    return times


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
    print('Script started...')

    input_size_list = [10, 20, 50, 100, 150, 200, 250, 300, 400, 500, 1000, 5000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
    functions = [partition_last, partition_first, partition_middle, partition_rand]


    time_per_size = get_time_per_input_size(input_size_list, functions, quick_sort=quick_sort)
    plot_time_per_size(time_per_size)









































































# def get_time_measurements(iterations):
#     print('\nTIME MEASUREMENTS\n')
#     print('-------------------------------------------------------------------------------------------------------------------')

#     data_last = get_data(sort_list1, low, high, partition_last, iterations)
#     data_first = get_data(sort_list2, low, high, partition_first, iterations)
#     data_random = get_data(sort_list3, low, high, partition_rand, iterations)
#     data_median = get_data(sort_list4, low, high, partition_middle, iterations)

#     # print('*** LAST ***')
#     # print(data_last)
#     # print('MEAN TIME: ', statistics.mean(data_last))
#     # print('\n')

#     # print('*** FIRST ***')
#     # print(data_first)
#     # print('MEAN TIME: ', statistics.mean(data_first))
#     # print('\n')

#     # print('*** RAND ***')
#     # print(data_random)
#     # print('MEAN TIME: ', statistics.mean(data_random))
#     # print('\n')

#     # print('*** MEDIAN ***')
#     # print(data_median)
#     # print('MEAN TIME: ', statistics.mean(data_median))
#     # print('\n')



# def normalize_data(list_of_data):
#     normalized = [math.log10(number + 1) for number in list_of_data]
#     return normalized