N=int(input())
A=list(map(int,input().split()))

Subordinate=[[] for i in range(N)]
for i in range(len(A)):
    A_i=A[i]
    Subordinate[A_i-1].append(A_i)

for i in Subordinate:
    print(len(i))