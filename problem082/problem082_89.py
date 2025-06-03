S = input()
T = input()
ans = float('inf')

for i in range(len(S) - len(T) + 1):
    s = list(S[i:i + len(T)])
    t = list(T)
    count = 0
    for j in range(len(T)):
        if s[j] != t[j]:
            count += 1
    ans = min(ans, count)

print(ans)