a,b=1,0
for c in map(int,input()):a,b=min(a+10-c-1,b+c+1),min(a+10-c,b+c)
print(b)