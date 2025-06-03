X, Y, A, B, C = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

red = sorted(P[:X])
gre = sorted(Q[:Y])
m = min((X+Y),C)
n = R[:m]
red.extend(gre)
red.extend(n)
red = sorted(red, reverse=True)

print(sum(red[:X+Y]))