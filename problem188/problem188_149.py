X, Y, A, B, C = map(int, input().split())
L = []
P = list(map(int, input().split()))
P.sort(reverse=True)
L += P[:X]
Q = list(map(int, input().split()))
Q.sort(reverse=True)
L += Q[:Y]
L += list(map(int, input().split()))
L.sort(reverse=True)
print(sum(L[:X + Y]))
