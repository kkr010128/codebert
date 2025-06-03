
N = int(input())
a = list(map(int, input().split(" ")))

t = 1
for x in a:
    if x == t:
        t += 1
t -= 1

if t == 0:
    print(-1)
else:
    print(N-t)

