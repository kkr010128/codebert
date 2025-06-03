N = int(raw_input())
count = 0

A_str = raw_input().split()
A = map(int, A_str)

def merge(left, right):
    global count
    sorted_list = []
    l_index = 0
    r_index = 0

    while l_index < len(left) and r_index < len(right):
        count += 1
        if left[l_index] <= right[r_index]:
            sorted_list.append(left[l_index])
            l_index += 1
        else:
            sorted_list.append(right[r_index])
            r_index += 1

    if len(left) != l_index:
        sorted_list.extend(left[l_index:])
        count += len(left[l_index:])
    if len(right) != r_index:
        sorted_list.extend(right[r_index:])
        count += len(right[r_index:])

    return sorted_list 

def mergeSort(A):
    
    if len(A) <= 1:
        return A

    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return list(merge(left, right))

print ' '.join(map(str, mergeSort(A)))
print count