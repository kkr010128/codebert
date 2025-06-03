N = int(input())
S = list(str(input()))

t = 0
for i in range(len(S)):
    if S[i] == 'C' and S[i-1] == 'B' and S[i-2] == 'A':
        t += 1
print(t)