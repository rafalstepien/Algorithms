import random, time
from matplotlib import pyplot as plt

def get_time_per_input_size(input_size_list, functions, quick_sort):
    time_per_size_per_function = {}
    for func in functions:
        print('Getting time data for {} function'.format(func.__name__))
        time_per_size_per_function[func.__name__] = [[], []]
        for input_size in input_size_list:
            print('\t >getting time data for {} input length'.format(input_size))
            delta_time_mean = 0
            for x in range(50):
                example_list = random.sample(range(1_000_000_000), input_size)
                t1 = time.perf_counter()
                quick_sort(example_list, start=0, stop=len(example_list) - 1, fun=func)
                delta_time = time.perf_counter() - t1
                delta_time_mean += delta_time
            time_per_size_per_function[func.__name__][0].append(input_size)#, delta_time_mean/100])
            time_per_size_per_function[func.__name__][1].append(delta_time_mean/100)
    return time_per_size_per_function

def plot_time_per_size(time_per_size):
    fig, ax = plt.subplots()
    names_to_legend = ['partition_last', 'partition_first', 'partition_middle', 'partition_rand']
    for index, name in enumerate(names_to_legend):
        print('Constructing {} plot...'.format(index))
        ax.plot(time_per_size[name][0], time_per_size[name][1], label=name)
    ax.legend()
    plt.show()