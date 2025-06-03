ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())

S, T = input().split()
A, B = rii()
U = input()
D = {S:A, T:B}
D[U] -= 1

print(D[S], D[T])