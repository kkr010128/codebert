import collections
 
N,*S = open(0).read().split()
C = collections.Counter(S)
 
i = C.most_common()[0][1]
print(*sorted([k for k,v in C.most_common() if v == i]), sep='\n')