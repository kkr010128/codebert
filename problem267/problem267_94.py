N = int(input())
S = input()

ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            a = [i, j, k]
            l = 0
            for s in S:
                if l < 3  and a[l] == int(s):
                    l += 1
            if l == 3:
                ans += 1

print(ans)
