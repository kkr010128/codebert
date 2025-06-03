N,D=map(int, input().split())
A = 0
for i in range(N):
    X,Y=map(int, input().split())
    if (D*D) >= (X*X)+(Y*Y):
        A +=1 
print(A)