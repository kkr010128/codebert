n, k = map(int, input().split())
R, S, P = map(int, input().split())
t = input()
prev = {}

ans = 0
for i in range(k):
    if t[i] == 'r':
        ans += P
        prev[i] = 'p'
    elif t[i] == 's':
        ans += R
        prev[i] = 'r'
    elif t[i] == 'p':
        ans += S
        prev[i] = 's'

for i in range(k, n):
    a = i % k
    if t[i] == 'r':
        if prev[a] != 'p':
            ans += P
            prev[a] = 'p'
        else:
            if i + k < n and t[i + k] != 's':
                prev[a] = 'r'
            else:
                prev[a] = 's'
    elif t[i] == 's':
        if prev[a] != 'r':
            ans += R
            prev[a] = 'r'
        else:
            if i + k < n and t[i + k] != 'p':
                prev[a] = 's'
            else:
                prev[a] = 'p'
    elif t[i] == 'p':
        if prev[a] != 's':
            prev[a] = 's'
            ans += S
        else:
            if i + k < n and t[i + k] != 'r':
                prev[a] = 'p'
            else:
                prev[a] = 'r'
print(ans)