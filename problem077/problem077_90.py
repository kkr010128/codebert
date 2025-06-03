a, b, c, d = map(int,input().split(" "))

Ns = [a*c, a*d, b*c, b*d]
print(sorted(Ns)[-1])