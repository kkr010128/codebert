n = int(input())
S = list(map(int, input().split()))
S.append(0)
q = int(input())
T = list(map(int, input().split()))
N = 0
for t in T:
    i = 0
    S[n] = t
    while S[i] != t:
        i += 1
    if i != n:
        N += 1
print(N)
