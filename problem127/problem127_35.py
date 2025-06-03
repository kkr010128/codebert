X,Y = map(int,input().split())
 
result = 'No'
for x in range(X+1):
    if (2*x + 4*(X-x)) == Y:
        result = 'Yes'
        break
print(result)