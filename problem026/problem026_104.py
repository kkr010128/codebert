count = 0 

def merge(data, left, mid, right):
    global count
    n1 = mid - left
    n2 = right - mid 
    L = []
    R = []
    for i in range(n1):
        L.append(data[left+i])
    for i in range(n2):
        R.append(data[mid+i])
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0 
    j = 0 
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1

def merge_sort(data, left, right):
    if left + 1 < right:
        mid = (left + right) / 2 
        merge_sort(data, left, mid)
        merge_sort(data, mid, right)
        merge(data, left, mid, right)

def main():
    num = raw_input()
    num_list = raw_input().split()
    num_list = map(int, num_list)
    merge_sort(num_list, 0, len(num_list))
    num_list =  map(str, num_list)
    print " ".join(num_list)
    print count

if __name__ == '__main__':
    main()