A, B, C, K = map(int, input().split())

# KをA,B,Cの順に割り振る
a = min(A, K)
K -= a

b = min(B, K)
K -= b

c = min(C, K)

print(1 * a + -1 * c)
