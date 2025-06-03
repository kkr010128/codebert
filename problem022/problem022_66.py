n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(j) for j in input().split()]

ans = 0


for i in range(q):
    key = T[i]
    for j in range(n):
        if key == S[j]:
            ans += 1
            break
        else:
            continue

print(ans)
