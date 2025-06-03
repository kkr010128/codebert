import itertools

n = input()
a = list(map(int, input().split()))
q = input()
 
aset = set()
for i in range(1, len(a) + 1):
    aset |= set(sum(combi) for combi in itertools.combinations(a, i))
 
for m in map(int, input().split()):
    print('yes' if m in aset else 'no')