_, s, _, t = [[*map(int, o.split())] for o in open(0)]
print(sum(i in s for i in t))
