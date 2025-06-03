n=int(input())
data=[[int(num)for num in input().split(' ')] for i in range(n)]
state=[[[0 for i in range(10)]for j in range(3)]for k in range(4)] 
for datum in data:
    state[datum[0]-1][datum[1]-1][datum[2]-1]+=datum[3]
for i in range(4):
    for j in range(3):
        s=""
        for k in range(10):
            s+=' '+str(state[i][j][k])
        print(s)
    if i!=3:
        print("####################")