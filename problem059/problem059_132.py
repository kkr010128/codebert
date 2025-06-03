import functools, operator
r,c = tuple(int(n) for n in input().split())
A = [[int(a) for a in input().split()] for i in range(r)]
for a in A:
    a.append(sum(a))
R = [functools.reduce(operator.add, x) for x in zip(*A)]
A.append(R)
for j in A:
    print(" ".join(map(str,j)))
