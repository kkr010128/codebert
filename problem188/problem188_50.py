X, Y, A, B, C = map(int, input().split())
Ps = list(map(int, input().split()))
Qs = list(map(int, input().split()))
Rs = list(map(int, input().split()))

Ps.sort(reverse=True)
Qs.sort(reverse=True)

Al = Ps[:X] + Qs[:Y] +Rs
Al.sort(reverse=True)

print(sum(Al[:X+Y]))