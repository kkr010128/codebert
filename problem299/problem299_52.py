N = int(input())
l = list(map(int,input().split()))
ans = [i for i in range(len(l))]
for i in range(N):
  ans[l[i] - 1] = i + 1
print(*ans)