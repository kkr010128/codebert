n=int(input())
l = [list(map(int,input().split())) for i in range(n)]
ans='No'
    
for i in range(n-2):

    if l[i][0]==l[i][1] and l[i+1][0]==l[i+1][1] and l[i+2][0]==l[i+2][1]:
        ans='Yes'
    
print(ans)