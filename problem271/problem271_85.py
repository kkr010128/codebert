N = int(input())
S = list(input())
M = len(S)

A = [""]*M

for i in range(M):
    ref = 65 + (ord(S[i]) + N - 65) % 26
    A[i] = chr(ref)

ans = "".join(A)
print(ans)