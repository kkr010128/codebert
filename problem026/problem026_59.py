def merge(a,left,mid,right):
    count=0
    L=a[left:mid]+[float("inf")]
    R=a[mid:right]+[float("inf")]
    i,j=0,0
    for k in range(left,right):
        count+=1
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
    return count

def mergeSort(a,left,right):
    if left+1<right:
        mid=(left+right)//2
        countl=mergeSort(a,left,mid)
        countr=mergeSort(a,mid,right)
        return merge(a,left,mid,right)+countl+countr
    return 0



n=int(input())
a=list(map(int,input().split()))
ans=mergeSort(a,0,n)
print(" ".join(map(str,a)))
print(ans)
