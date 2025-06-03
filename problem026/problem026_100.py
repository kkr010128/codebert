count = 0
def mergesort(A, left, right):
    if left + 1 < right:
        mid = (left + right)/2
        mergesort(A, left, mid)
        mergesort(A, mid, right)
        merge(A, left, mid, right)


def merge(A, left, mid, right):
    global count
    n1 = mid -left
    n2 = right - mid
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[left + i])
    for i in range(0, n2):
        R.append(A[mid + i])
    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        




if __name__ == "__main__":
    num = int(raw_input())
    num_list = raw_input().strip().split()
    num_list = map(int, num_list)
    mergesort(num_list, 0, len(num_list))
    num_list = map(str, num_list)
    print " ".join(num_list)
    print count