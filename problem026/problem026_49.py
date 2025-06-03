def main():
    n = input()
    A = map(int,raw_input().split())

    c = mergeSort(A,0,n)

    for i in range(n-1):
        print A[i],
    print A[-1]
    print c

def merge(A,left,mid,right):
    n1 = mid - left
    n2 = right - mid
    L = [A[left+i] for i in range(n1)]
    L += [float("inf")]
    R = [A[mid+i] for i in range(n2)]
    R += [float("inf")]
    i = 0
    j = 0
    for k in range(left,right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return i+j

def mergeSort(A,left,right):
    if left+1 < right:
        mid = (left+right)/2
        k1 = mergeSort(A,left,mid)
        k2 = mergeSort(A,mid,right)
        k3 = merge(A,left,mid,right)
        return k1+k2+k3
    else:
        return 0


if __name__ == "__main__":
    main()