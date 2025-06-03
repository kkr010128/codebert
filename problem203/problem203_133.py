A,B=map(int,input().split())
ans=-1
for i in range(10000):
     x=int(i*0.08)
     y=int(i*0.1)
     if A==x and B==y:
        ans=i
        break
print(ans)