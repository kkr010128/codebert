N = int(input())
A = [int(i) for i in input().split()]
ans = [0 for i in range(N)]
for i in A:
    ans[i-1] += 1
for i in ans:
    print(i)