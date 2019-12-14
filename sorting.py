tablica = [5, 2, 4, 6, 1, 3]

def insertion_sort(A):
	for j in range(1, len(A)):
		current = A[j]
		i = j - 1
		prev = A[i]
		while prev > current:
			prev, current = current, prev
	return A

print(insertion_sort(tablica))