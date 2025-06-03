*abc, k = map(int, input().split())
n = [0] * 3
for i, v in enumerate(abc):
    if k >= v:
        n[i] = v
        k -= v
    else:
        n[i] = k
        break

print(n[0] + n[2] * -1)