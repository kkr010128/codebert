import sys
d={}
for e in sys.stdin.readlines()[1:]:
 c,g=e.split()
 if'i'==c[0]:d[g]=0
 else:print(['no','yes'][g in d])
