# C - Go to School 
N = int(input())
A = list(map(int,input().split()))
A = [(i+1,A[i]) for i in range(N)]
A.sort(key=lambda x:x[1])
A = [str(a[0]) for a in A]
print(' '.join(A))