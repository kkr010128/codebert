import math

def merge(a,l,m,r):
    global cnt
    L = a[l:m]+[math.inf]
    R = a[m:r]+[math.inf]
    i = 0
    j = 0
    for k in range(l,r):
        cnt+=1
        if L[i]<=R[j]:
            a[k] = L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
def mergeSort(a,l,r):
    if l+1<r:
        m = (l+r)//2
        mergeSort(a,l,m)
        mergeSort(a,m,r)
        merge(a,l,m,r)
n = int(input())
a = list(map(int, input().split()))
cnt = 0

mergeSort(a,0,n)
print(*a)
print(cnt)
