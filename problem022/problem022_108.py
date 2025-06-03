N = int(input())
S = [int(x) for x in input().split()]
T = int(input())
Q = [int(x) for x in input().split()]

c = set()

for s in S:
    for q in Q:
        if s == q:
            c.add(s)

print(len(c))
