# coding: utf-8

from random import randint

def imin(p, k, n):
    m = p[k]
    im = k
    for j in range(k+1,n):
        if p[j] < m:
            m = p[j]
            im = j
    return im

def selection_sort(x):
    n = len(x)
    for i in range(0, n-1):
        k = imin(x, i, n)
        if i != k: # prosta transpozycja 
            x[i], x[k] = x[k], x[i]


def right_bisect(a, x, d, g):
    while (g > d):
        s = (g+d) // 2
        if (x[s] >= a):
            g = s
        else:
            d = s+1
    return d;

def insertion_sort_l(x):
    n = len(x)
    for i in range(1, n):
        k = right_bisect(x[i], x, 0, i)
        if k != i: # pop / insert to więcej niż transpozycja; ile operacji elementarnych jest tu wykonywanych?
            x.insert(k, x.pop(i))

def cyclic(x, a, b):
    t = x[b]
    for i in range(b, a, -1):
        x[i] = x[i-1]
    x[a] = t

def insertion_sort_t(x):
    n = len(x)
    for i in range(1, n):
        k = right_bisect(x[i], x, 0, i)
        if k != i: # pop / insert to więcej niż transpozycja; ile operacji elementarnych jest tu wykonywanych?
            cyclic(x, k, i)


def quicksort(a, l, r):
    i = l
    j = r
    # strategia wyboru osi rozdziału
    x = a[(l+r) // 2]
    # x = a[l]
    while i <= j:
        while a[i] < x: i += 1
        while x < a[j]: j -= 1
        if i<=j:
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    # niezmienniki po zakończeniu pętli
    assert j < i
    assert (j < l) or (a[j] <= x)
    assert (i > r) or (x <= a[i])
    # koniec testu niezmienników
    if l < j: quicksort(a, l, j);
    if i < r: quicksort(a, i, r);

def quick_sort_h(a):
    quicksort(a, 0, len(a)-1)

def partition(lst, start, stop):
    pivot_index = stop
    pivot_value = lst[pivot_index]

    for i in range(start, stop):
        if lst[i] < pivot_value:
            lst[i], lst[start] = lst[start], lst[i]
            start += 1

    lst[stop], lst[start] = lst[start], lst[stop]
    return start

def _quick_sort(lst, start, stop, pivot_fun, licz):
    if start < stop:
        pivot = pivot_fun(start, stop)
        licz[0] += 1
        lst[stop], lst[pivot] = lst[pivot], lst[stop]
        border = partition(lst, start, stop)
        _quick_sort(lst, start, border - 1, pivot_fun, licz)
        _quick_sort(lst, border + 1, stop, pivot_fun, licz)


def pivot_first(start, stop):
    return start

def pivot_middle(start, stop):
    return (start + stop) // 2

def pivot_last(start, stop):
    return stop

def pivot_rand(start, stop):
    return randint(start, stop)

def qs_l(x):
    _quick_sort(x, 0, len(x)-1, pivot_first, [0])

def qs_m(x):
    _quick_sort(x, 0, len(x)-1, pivot_middle, [0])

def qs_l(x):
    _quick_sort(x, 0, len(x)-1, pivot_last, [0])

def qs_r(x):
    _quick_sort(x, 0, len(x)-1, pivot_rand, [0])

