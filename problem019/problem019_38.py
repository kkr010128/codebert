N, Q = map(int, input().strip().split())

A = []
D = {}
for l in range(N):
    n, t = input().strip().split()
    A.append([n, int(t)])

T = 0
while A:
    l = A.pop(0)
    if l[1] > Q:
        l[1] -= Q
        T += Q
        A.append(l)
    else:
        T += l[1]
        print(l[0], T)