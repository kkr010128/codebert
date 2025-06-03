# input
N, M = map(int, input().split())

# process
ans = []

t = 1
for _ in range(M//2):
    ans.append((t, M-t+1))
    t += 1

t = M+1
for _ in range(-(-M//2)):
    ans.append((t, M*3+2-t))
    t += 1

# output
[print(a, b) for a, b in ans]
