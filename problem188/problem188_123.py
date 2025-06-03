X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
IronMan = sorted(p)
CaptainAmerica = sorted(q)
for i in range(X):
    r.append(IronMan.pop())
for i in range(Y):
    r.append(CaptainAmerica.pop())
SpiderMan = sorted(r)[::-1]
print(sum(SpiderMan[:X+Y]))
