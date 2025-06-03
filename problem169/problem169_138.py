N = int(input())
A = [int(x) for x in input().split()]
cnt = [0 for x in range(N)]
for i in range(len(A)) :
    cnt[A[i]-1] += 1

for i in range(N) :
    print(cnt[i])