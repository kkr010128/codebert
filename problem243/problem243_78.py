*p, = open(0).read().split()
print(sum(map(int, (p+[0])[p.index(p[-1])+3::2])))