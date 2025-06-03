X,Y = map(int,input().split())

ans = "No"

for i in range(X+1):
    for j in range (X-i+1):
        if i*2 + j*4 == Y and i + j == X:
            ans = "Yes"
            break
        
print(ans)

