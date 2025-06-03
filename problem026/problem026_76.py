ct=0
def merge(A,left,mid,right):
    global ct
    n1=mid-left
    n2=right-mid
    l=[A[left+i] for i in xrange(n1)]
    r=[A[mid+i] for i in xrange(n2)]
    l.append(float('inf'))
    r.append(float('inf'))
    i=0
    j=0
    for k in xrange(left,right):
        ct+=1
        if l[i]<=r[j]:
            A[k]=l[i]
            i=i+1
        else:
            A[k]=r[j]
            j=j+1

def mergesort(A,left,right):
    if left+1<right:
        mid=(left+right)/2
        mergesort(A,left,mid)
        mergesort(A,mid,right)
        merge(A,left,mid,right)
        
n=input()
s=map(int,raw_input().split())
mergesort(s,0,n)
i=0
s=map(str,s)
print(" ".join(s))
print(ct)