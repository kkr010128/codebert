a,b,c=map(int,input().split())
print(['No','Yes'][4*a*b<(c-a-b)**2 and a+b<c])