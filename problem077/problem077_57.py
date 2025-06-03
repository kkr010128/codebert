(X1,X2,Y1,Y2)=list(map(int,input().split()))
ans=max(X2*Y2,X1*Y1,X1*Y2,X2*Y1)
print (ans)