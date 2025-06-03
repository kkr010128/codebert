a,b,c,d=map(int,input().split())
x=[]*4
x.append(a*c)
x.append(b*c)
x.append(a*d)
x.append(b*d)
x.sort()
print(x[-1])