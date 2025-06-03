X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P.sort()
Q.sort()
R.sort()
P = P[::-1]
Q = Q[::-1]
R = R[::-1]
D = P[:X] + Q[:Y] + R
D.sort()
D = D[::-1]
D = D[:X+Y]
ans = sum(D)
print(ans)