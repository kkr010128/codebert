l = [int(x) for x in input().split()]
X, N = l[0], l[1]
p = [int(x) for x in input().split()]

delta = 0
while True:
    if not X - delta in p:
        print(X-delta)
        break
    if not X + delta in p:
        print(X + delta)
        break
    delta += 1