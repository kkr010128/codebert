a,*b=[],
for z in[*open(0)][1:]:x,y=map(int,z.split());a+=x+y,;b+=x-y,
print(max(max(a)-min(a),max(b)-min(b)))