X, Y, A, B, C = map(int, input().split())
Ap = list(map(int, input().split()))
Bq = list(map(int, input().split()))
Cr = list(map(int, input().split()))

Ap.sort(reverse = True)
Bq.sort(reverse = True)

L = sorted(Ap[:X] + Bq[:Y] + Cr, reverse = True)

print(sum(L[:X+Y]))