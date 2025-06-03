n = int(input())
a = [int(i)-1 for i in input().split()]
ans = 0
for i in range(n):
    if a[i] != (i - ans):
        ans += 1
print(ans if ans != n else -1)