n = int(input())
s = list(map(int, input()))
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            p = 0
            while p < len(s) and s[p] != i: p += 1
            p += 1
            while p < len(s) and s[p] != j: p += 1
            p += 1
            while p < len(s) and s[p] != k: p += 1
            if p < len(s):
                ans += 1
print(ans)