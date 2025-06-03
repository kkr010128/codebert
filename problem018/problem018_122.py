s=[]
p=s.pop
for e in input().split():
 s+=[e if e.isdigit() else str(eval(p(-2)+e+p()))]
print(*s)