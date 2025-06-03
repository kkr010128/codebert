n = int(input())
a = list(map(int, input().split()))
ans = [0]*n
for i, a in enumerate(a):
     ans[a-1] += 1
print(*ans, sep="\n")