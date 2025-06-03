import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

solved = [False] * (n + 1)
wa = [0] * (n + 1)

for i in range(m):
    p_str, s = input().split()
    p = int(p_str)
    if s == "AC":
        solved[p] = True
    else:
        if not solved[p]:
            wa[p] += 1


ac = 0
pe = 0

for i in range(1, n+1):
    if solved[i]:
        ac += 1
        pe += wa[i]

print(ac, pe)