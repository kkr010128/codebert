d=set()
for _ in[0]*int(input()):
 c,g=input().split()
 if'i'==c[0]:d|=set([g])
 else:print(['no','yes'][g in d])
