import sys
n = int(sys.stdin.readline()[:-1])
S = sorted(list(map(int, (sys.stdin.readline()[:-1]).split())))
q = int(sys.stdin.readline()[:-1])
T = sorted(list(map(int, (sys.stdin.readline()[:-1]).split())))

count = 0
for i in T:
    x = 0
    while x < len(S):
        if i == S[x]:
            count += 1
            S = S[x:]
            break
        x += 1

print(count)