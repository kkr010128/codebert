import sys

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = []
    R = []
    for i in range(n1):
        L.append(A[left+i])
    for i in range(n2):
        R.append(A[mid+i])
    L.append("INFTY")
    R.append("INFTY")
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        global c
        c += 1


def mergeSort(A, left, right):
    if left+1 < right:
        mid = (left + right) / 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    N = int(lines[0])
    nums = [int(n) for n in lines[1].split(" ")]
    c = 0
    mergeSort(nums, 0, N)
    print " ".join(map(str, nums))
    print c