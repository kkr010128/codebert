N = int(input())
L = [int(x) for x in input().split()]
cnt = 0

for i in range(len(L) - 2):
    for j in range(i+1, len(L)-1):
        for k in range(j+1, len(L)):
            a = L[i]
            b = L[j]
            c = L[k]
            p = a + b > c
            q = b + c > a
            r = c + a > b
            s = a != b
            t = b != c
            u = c != a
            if p and q and r and s and t and u:
                cnt += 1
print(cnt)