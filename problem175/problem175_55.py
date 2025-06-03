N = int(input())
S = input()

r = [0 for _ in range(N + 1)]
g = [0 for _ in range(N + 1)]
b = [0 for _ in range(N + 1)]

for i in reversed(range(N)):
    r[i] = r[i + 1]
    g[i] = g[i + 1]
    b[i] = b[i + 1]
    if S[i] == "R":
        r[i] += 1
    if S[i] == "G":
        g[i] += 1
    if S[i] == "B":
        b[i] += 1
        
ans = 0

for i in range(N):
    if S[i] == "R":
        for j in range(i + 1, N):
            if S[j] == "G":
                if 2 * j - i < N:
                    if S[2 * j - i] == "B":
                        ans += (b[j + 1] - 1)
                    else:
                        ans += b[j + 1]
                else:
                    ans += b[j + 1]
                    
for i in range(N):
    if S[i] == "R":
        for j in range(i + 1, N):
            if S[j] == "B":
                if 2 * j - i < N:
                    if S[2 * j - i] == "G":
                        ans += (g[j + 1] - 1)
                    else:
                        ans += g[j + 1]
                else:
                    ans += g[j + 1]
                    
for i in range(N):
    if S[i] == "B":
        for j in range(i + 1, N):
            if S[j] == "R":
                if 2 * j - i < N:
                    if S[2 * j - i] == "G":
                        ans += (g[j + 1] - 1)
                    else:
                        ans += g[j + 1]
                else:
                    ans += g[j + 1]
                    
for i in range(N):
    if S[i] == "B":
        for j in range(i + 1, N):
            if S[j] == "G":
                if 2 * j - i < N:
                    if S[2 * j - i] == "R":
                        ans += (r[j + 1] - 1)
                    else:
                        ans += r[j + 1]
                else:
                    ans += r[j + 1]
                    
for i in range(N):
    if S[i] == "G":
        for j in range(i + 1, N):
            if S[j] == "R":
                if 2 * j - i < N:
                    if S[2 * j - i] == "B":
                        ans += (b[j + 1] - 1)
                    else:
                        ans += b[j + 1]
                else:
                    ans += b[j + 1]
                    
for i in range(N):
    if S[i] == "G":
        for j in range(i + 1, N):
            if S[j] == "B":
                if 2 * j - i < N:
                    if S[2 * j - i] == "R":
                        ans += (r[j + 1] - 1)
                    else:
                        ans += r[j + 1]
                else:
                    ans += r[j + 1]
                    
print(ans)