def mergeSort(arr):
	end = len(arr)
	mid = end//2
	if end == 1:
		return
	L = arr[:mid]
	R = arr[mid:]
	mergeSort(L)
	mergeSort(R)
	i = j = k = 0

	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < len(L):
		arr[k] = L[i]
		i += 1
		k += 1

	while j < len(R):
		arr[k] = R[j]
		j += 1
		k += 1

	return arr

if __name__ == '__main__':
	a = [8, 3, 5, 0, 49, 20, 84, 2, 12, 54, 13, 51, 67, 89]
	print(mergeSort(a))
