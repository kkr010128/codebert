def cmb(n):
    if n < 2:
        return 0
    else:
        return (n*(n-1)/2)

N = int(input())
A = list(map(int,input().split()))

num_dict = {i:0 for i in range(1,N+1)}
for i in range(N):
    num_dict[A[i]] += 1

S = 0
for i in range(1,N+1):
    S += cmb(num_dict[i])

for i in range(N):
    tmp = 0
    S_dif = cmb(num_dict[A[i]]-1) - cmb(num_dict[A[i]])
    tmp = S + S_dif
    print(int(tmp))