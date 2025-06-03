a = [int(v) for v in input().rstrip().split()]
r = 'bust' if sum(a) >= 22 else 'win'
print(r)
