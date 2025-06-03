n, k, c = map(int, input().split())
s = input()

dpl = [0 for i in range(n+1)]
dpr = [0 for i in range(n+1)]

for i in range(n):
    dpl[i+1] = (dpl[i] if s[i] == 'x' else
                dpl[i-c] + 1 if i-c >= 0 else
                1)

for i in range(n, 0, -1):
    dpr[i-1] = (dpr[i] if s[i-1] == 'x' else
                dpr[i+c] + 1 if i+c < n else
                1)

for i in range(1, n+1):
    if dpl[i-1] + dpr[i] < k:
        print(i)