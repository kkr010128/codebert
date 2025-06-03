N = int(input())
S = []
T = []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
X = input()

time = None
for s, t in zip(S, T):
    if s == X:
        time = 0
    elif time is not None:
        time += t
    else:
        continue

print(time)
