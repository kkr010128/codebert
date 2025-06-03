#B
N, K = map(int,input().split())
P = list(map(int, input().split()))
P_sort=sorted(P)
P_sum=0
for i in range(K):
    P_sum+=P_sort[i]
print(P_sum)