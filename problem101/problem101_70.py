a,b,c=map(int,input().split())
K=int(input())

isCheck = None
for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            x = a*2**(i)
            y = b*2**(j)
            z = c*2**(k)
            if i+j+k <= K and x < y and y < z:
                isCheck = True

if isCheck:
    print("Yes")
else:
    print("No")
