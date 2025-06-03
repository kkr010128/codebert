x,y,a,b,c=map(int,input().split())
*p,=sorted(map(int, input().split()))
*q,=sorted(map(int, input().split()))
*r,=map(int, input().split())

p=p[-x:]
q=q[-y:]
r=sorted(p+q+r)
print(sum(r[-x-y:]))