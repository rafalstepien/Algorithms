#!/usr/bin/env python3

'''
    demonstracja qsort by K. Kotlarz & R. Stępień
    nieco podrasowana i oczyszczona stylistycznie
'''

import sorty

import random
import time
from matplotlib import pyplot


def is_ord(x):
    n = len(x)
    for i in range(1,n):
        if x[i-1] > x[i]:
            return False
    return True

if __name__ == '__main__':

  pivoty = (sorty.qs_l, sorty.qs_m, sorty.qs_l, sorty.qs_r, sorty.quick_sort_h, sorty.insertion_sort_l, sorty.insertion_sort_t, sorty.selection_sort)
  nazwy = ('quick (first)    ', 
           'quick (middle)   ', 
           'quick (last)     ', 
           'quick (random)   ', 
           'quick (Hoare)    ', 
           'insertion (list) ', 
           'insertion (table)', 
           'selection        ',
          )
  style ='+x*v<>^o'
  sizes = [ ]
  cases = [ ]
  results = [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]]

  nn = 20
  for i in range(nn):

    n = random.randint(10, 10000)
    lista = random.sample(range(100000000), n)

    print('{} / {}'.format(i, nn))
    print('długość\tmetoda            \tczas             \tl. wyw.')
    sizes.append(n)
    cases.append(i)
    for nazwa, fp, res in zip(nazwy, pivoty, results):

        t = time.perf_counter()
        list1 = lista[:]
        fp(list1)
        t = time.perf_counter() - t
        assert is_ord(list1)
        print("{}\t{}\t{}\t{}".format(n, nazwa, t, ''))
        res.append(t)

fig = pyplot.figure()
ax = fig.add_subplot(111)
fig.suptitle('Performance of sorting algorithms')
ax.set_xlabel('data length [ ]')
ax.set_ylabel('CPU time [sec]')
for data, label, styl in zip(results, nazwy, style):
    ax.plot(sizes, data, styl, label = label)
fig.legend()
fig.show()

fig = pyplot.figure()
ax = fig.add_subplot(111)
fig.suptitle('Performance of sorting algorithms')
ax.set_xlabel('case number [ ]')
ax.set_ylabel('CPU time [sec]')
for data, label, styl in zip(results, nazwy, style):
    ax.plot(cases, data, styl, label = label)
fig.legend()
fig.show()

pyplot.show()
