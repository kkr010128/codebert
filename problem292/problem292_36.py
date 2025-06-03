N,*D = map(int,open(0).read().split())
import itertools
print(sum(a * b for a,b in itertools.combinations(D,2)))