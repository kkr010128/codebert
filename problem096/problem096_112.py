N,D = map(int,input().split())
cnt = 0

for i in range(N):
    A = 0
    X,Y = map(int,input().split())
    A = X**2 + Y**2
    
    if A <= D**2:
        cnt += 1
        
print(cnt)