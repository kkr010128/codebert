n = int(input())
S = list(map(int, input().split()))
S = list(set(S))
q = int(input())
T = list(map(int, input().split()))
T = list(set(T))

C = 0
for i in range(len(S)):
    if S[i] in T:
        C += 1
print(C)
