inf = int(input())
i = 0
table = []
buil = [[[0]*10 for i in range(3)]for i in range(4)]

while(i < inf):
    b,f,r,v = map(int,input().split())
    b -=1
    f -=1
    r -=1
    buil[b][f][r] += v
    if buil[b][f][r] > 9: buil[b][f][r] = 9
    elif buil[b][f][r] < 0: buil[b][f][r] = 0
    i += 1

for i in range(4):
        if i != 0: print("#"*20)
        for j in range(3):
                for k in range(10):
                    print(" %d" %(buil[i][j][k]),end ="")
                print()

    
