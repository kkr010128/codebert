m={"E":[3,1,0,5,4,2], "N":[1,5,2,3,0,4], "W":[2,1,5,0,4,3], "S":[4,0,2,3,5,1]}
d=map(int, raw_input().split())
nd=[0]*6
for x in raw_input():
    for j in range(6): nd[j]=d[m[x][j]]
    d=list(nd)
print d[0]