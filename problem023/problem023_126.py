d={}
for _ in[0]*int(input()):
 c,g=input().split()
 if'i'==c[0]:d[g]=0
 else:print(['no','yes'][g in d])
