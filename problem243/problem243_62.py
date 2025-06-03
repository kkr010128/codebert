N = int(input())
S = [""] * N
T = [0] * N
for i in range(N):
    s, t = input().split()
    S[i] = s
    T[i] = int(t)
X = input()

t = 0
for i in range(N):
    t += T[i]
    if S[i] == X:
        break
print(sum(T) - t)
