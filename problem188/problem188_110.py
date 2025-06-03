X, Y, A, B, C = map(int, input().split())
Ap = list(map(int, input().split()))
Bq = list(map(int, input().split()))
Cr = list(map(int, input().split()))

Ap.sort()
Bq.sort()

print(sum(sorted(Ap[A-X:] + Bq[B-Y:] + Cr)[C:]))