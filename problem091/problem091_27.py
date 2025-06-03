N = int(input())
L = [int(x) for x in input().split()]
L.sort()
cnt = 0

for i in range(len(L) - 2):
    for j in range(i+1, len(L)-1):
        for k in range(j+1, len(L)):
            a = L[i]
            b = L[j]
            c = L[k]
            p = a + b > c
            s = a != b
            t = b != c
            if p and s and t:
                cnt += 1
print(cnt)