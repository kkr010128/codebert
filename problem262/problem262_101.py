N=int(input())
X=[0]*N
for i in range(N):
 X[i]=[list(map(int,input().split())) for _ in [0]*int(input())]
print(max(['{:b}'.format(i).count('1')for i in range(2**N) if all([all([y[1]==i>>(y[0]-1)&1 for y in X[j]]) for j in range(N) if (i>>j&1)])]))