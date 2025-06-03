S = input()
T = input()

s = len(S)
t = len(T)
m = 10 ** 4

for i in range(s - t + 1):
    c = 0
    for j in range(t):
        if S[i + j] != T[j]:
            c += 1
    if c < m:
        m = c
print(m)