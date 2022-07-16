def remove(dupli):
	final_list = []
	for num in dupli:
		if num not in final_list:
			final_list.append(num)
	return final_list

def bubbleSort(rlst):
	n = len(rlst)
	for i in range(n):
		for j in range(0, n-i-1):
			if dupli[j] > dupli[j+1]:
				rlst[j], rlst[j+1] = rlst[j+1], rlst[j]

dupli =eval(input("Enter a list with duplicate numbers"))
rlst=remove(dupli)
print(rlst)

bubbleSort(rlst)

print("Sorted array is:")
for i in range(len(rlst)):
    print("%d" % rlst[i], end=" ")










