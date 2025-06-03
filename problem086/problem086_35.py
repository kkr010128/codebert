n,x,t = map(int,input().split())
c = n//x
if n%x>0:
    c+=1
print(t*c)