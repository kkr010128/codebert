input()
P1 = []
P2 = []
P3 = []
for a, b in zip(map(int, input().split()), map(int, input().split())):
    t = abs(a - b)
    P1.append(t)
    P2.append(t ** 2)
    P3.append(t ** 3)
print("{:f}".format(sum(P1)))
print(sum(P2) ** (1 / 2))
print(sum(P3) ** (1 / 3))
print("{:f}".format(max(P1)))
