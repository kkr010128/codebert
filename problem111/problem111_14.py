# ABC 173 D

N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
ind=[(i+1)//2 for i in range(N-1)]
print(sum([A[i] for i in ind]))