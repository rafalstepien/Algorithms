import random, time, statistics, math, pprint
from matplotlib import pyplot as plt
import quick_sort

def get_times(lst, number_of_rep=10):
	times = [[], [], [], []] # last, rand, first, middle
	for x in range(number_of_rep):
		for index, fun in enumerate([quick_sort.partition_last, quick_sort.partition_rand, quick_sort.partition_first, quick_sort.partition_middle]):
			t1 = time.perf_counter()
			quick_sort.quick_sort(lst, 0, len(lst) - 1, fun)
			t1 = time.perf_counter() - t1
			times[index].append(t1)
	return zip(*times)
	#zip_obj = zip(*times)  # zip_obj[0] -> wyniki z pierwszego powtórzenia dla kolejno last, rand, first, middle

def plot_times_data_len():
	for length in list(range(1000, 21_000, 1000)):
		lst = random.sample(range(1000000), length)
		times = get_times(lst)
		fig, ax = plt.subplots()
		names_to_legend = ['last', 'first', 'median', 'random']
		for index, time_tuple in enumerate(times):
			for time in time_tuple:
				ax.plot(length, time, label=names_to_legend[index])
	ax.legend()
	plt.show()


plot_times_data_len()