N, P = map(int, input().split())
S = [int(s) for s in input()]

if P == 2 or P == 5:
    print(sum(i for i, s in enumerate(S, 1) if s % P == 0))
    quit()

C = [0] * P
tens = 1
cur = 0
for s in reversed(S):
    cur = (cur + s * tens) % P
    C[cur] += 1
    tens = (tens * 10) % P

print(C[0] + sum(c * (c - 1) // 2 for c in C))