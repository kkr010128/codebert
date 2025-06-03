n = int(input())
a = list(map(int, input().split()))
mod = 1000000007
caps = [0, 0, 0]
ans = 1
for i in range(n):
    equal = []
    for j in range(3):
        if caps[j] == a[i]:
            equal.append(j)
    l = len(equal)
    if l == 0:
        ans = 0
        break
    ans = ans * l % mod
    caps[equal[0]] += 1
print(ans)