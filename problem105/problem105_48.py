n = int(input())
a = [int(s) for s in input().split()]
ans = 0
for i in range(len(a)):
    if i % 2 == 0 and a[i] % 2 == 1:
            ans += 1
print(ans)