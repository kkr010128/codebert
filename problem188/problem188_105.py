X, Y, A, B, C = map(int, input().split())
*p, = map(int, input().split())
*q, = map(int, input().split())
*r, = map(int, input().split())

p.sort(key=lambda x: -x)
q.sort(key=lambda x: -x)
p = p[:X]
q = q[:Y]

pqr = p+q+r
pqr.sort(key=lambda x: -x)
print(sum(pqr[:X+Y]))