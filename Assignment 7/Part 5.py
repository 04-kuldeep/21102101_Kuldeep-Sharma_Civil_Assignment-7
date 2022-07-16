def merge(lst, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = lst[l + i]

	for j in range(0, n2):
		R[j] = lst[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			lst[k] = L[i]
			i += 1
		else:
			lst[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		lst[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		lst[k] = R[j]
		j += 1
		k += 1

def mergeSort(lst, l, r):
	if l < r:

		m = l+(r-l)//2

		mergeSort(lst, l, m)
		mergeSort(lst, m+1, r)
		merge(lst, l, m, r)

def binary_search(lst, x):
	low = 0
	high = len(lst) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		if lst[mid] < x:
			low = mid + 1
		elif lst[mid] > x:
			high = mid - 1

		else:
			return mid

	return -1

lst=eval(input("Enter a list with duplicates numbers"))
n = len(lst)
print("Given array is")
for i in range(n):
	print("%d" % lst[i],end=" ")

mergeSort(lst, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % lst[i],end=" ")

x = int(input("\nEnter the element to search :"))
result = binary_search(lst,x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
print("The number of occurence of",x,"is",lst.count(x))







