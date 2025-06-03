import collections
N = int(input())
A = list(map(int,input().split()))
Cn_A = collections.Counter(A)
ans_list = [0]*len(Cn_A)
ans = 0
for i,j in enumerate(Cn_A.values()):
    ans+=j*(j-1)//2
for i in A:
    j = Cn_A[i]
    print(ans-(j*(j-1)//2)+((j-1)*(j-2)//2))
    
