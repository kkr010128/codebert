N = int(input())
S, T = input().split()
answer = []

for s, t in zip(S, T):
    answer.append(s)
    answer.append(t)

print(*answer, sep='')