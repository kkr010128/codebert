(X1,X2,Y1,Y2)=list(map(int,input().split()))
ans=X2*Y2
ans=max(ans,X1*Y1)
ans=max(ans,X1*Y2)
ans=max(ans,X2*Y1)
print (ans)