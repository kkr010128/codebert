A,B,N=map(int,input().split())
if N<B:
    x=N
elif N==B:
    x=N-1
else:
    x=(N//B)*B-1
ans=(A*x/B)//1-A*(x//B)
print(int(ans))