cnt = 0
def merge(L,R):
    global cnt
    A = []
    i = j = 0
    n = len(L)+len(R)
    L.append(float("inf"))
    R.append(float("inf"))
    for _ in range(n):
        cnt += 1
        if L[i] <= R[j]:
            A.append(L[i])
            i += 1
        else:
            A.append(R[j])
            j += 1
    return A

def mergeSort(A):
    if len(A)==1: return A
    m = len(A)//2
    return merge(mergeSort(A[:m]),mergeSort(A[m:])) 
    

if __name__=='__main__':
    n=int(input()) 
    A=list(map(int,input().split()))
    print(*mergeSort(A))
    print(cnt)