#input
X, N = map(int, input().split())
p = list(map(int, input().split()))

if len(p) == 0 or X < min(p) or X > max(p):
    print(X)
    exit()

min = X
max = X
while True:
    if min not in p:
        print(min)
        break
    elif max not in p:
        print(max)
        break
    else:
        min -= 1
        max += 1
