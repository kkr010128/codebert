count = 0

def marge(A,left,mid,right):
    global count
    n1 = mid -left
    n2 = right -mid
    L = []
    R = []
    for i in range(left,n1+left):
        L.append(A[i])
    for i in range(mid,n2+mid):
        R.append(A[i])

    L.append(float("inf"))
    R.append(float("inf"))

    r_id,l_id = 0,0
    for k in range(left,right):
        count += 1
        if(L[l_id] <= R[r_id]):
            A[k] = L[l_id]
            l_id += 1
        else:
            A[k] = R[r_id]
            r_id += 1

def margeSort(A,left,right):
    if left+1 < right:
        mid = int((left+right)/2)
        margeSort(A,left,mid)
        margeSort(A,mid,right)
        marge(A,left,mid,right)


n = int(raw_input())
s = raw_input()
A = []
A = map(int,s.split())

margeSort(A,0,n)

A_str = map(str,A)
print(" ".join(list(A_str)))
print count