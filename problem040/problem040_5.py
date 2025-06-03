i=list(map(int,input().split()))
x=[[0,1],[0,2],[1,2]]

for a in range(3):
    if( i[ x[a][0] ] > i[ x[a][1] ]):
        swap=i[ x[a][0] ]
        i[ x[a][0] ]= i[ x[a][1] ]
        i[ x[a][1] ]=swap
        

print(i[0],end=' ')
print(i[1],end=' ')
print(i[2],end='\n')
