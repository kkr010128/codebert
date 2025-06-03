def mergeSort(num_list, left, right):
	if left + 1 < right:
		mid = (left + right) / 2
		mergeSort(num_list, left, mid)
		mergeSort(num_list, mid, right)
		merge(num_list, left, mid, right)

def merge(num_list, left, mid, right):
	global count 
	L = list(num_list[left:mid])
	L.append(float("inf"))
	R = list(num_list[mid:right])
	R.append(float("inf"))
	i, j = 0, 0
	for k in range(left, right):
		if L[i] <= R[j]:
			num_list[k] = L[i]
			i += 1
			count += 1
		else:
			num_list[k] = R[j]
			j += 1
			count += 1

count = 0
n = int(raw_input())
a = raw_input()
l = []
l = a.split(" ")
for i in range(len(l)):
	l[i] = int(l[i])
mergeSort(l, 0, n)

print " ".join(map(str, l)) 
print count