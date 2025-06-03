n = int(input())
buffer = []
i = 0
while i<n:
    b,f,r,v = map(int,input().split())
    buffer.append([b,f,r,v])
    i = i + 1

room = []
for h in range(15):
    if h == 3 or h == 7 or h == 11:
        room.append(['**']*10)
    else:
        room.append([0]*10)
            
for y in range(n):
    if buffer[y][0] == 1:
        room[buffer[y][1]-1][buffer[y][2]-1] = buffer[y][3] + room[buffer[y][1]-1][buffer[y][2]-1]
    elif buffer[y][0] == 2:
        room[buffer[y][1]-1+4][buffer[y][2]-1] = buffer[y][3] + room[buffer[y][1]-1+4][buffer[y][2]-1]
    elif buffer[y][0] == 3:
        room[buffer[y][1]-1+8][buffer[y][2]-1] = buffer[y][3] + room[buffer[y][1]-1+8][buffer[y][2]-1]
    elif buffer[y][0] == 4:
        room[buffer[y][1]-1+12][buffer[y][2]-1] = buffer[y][3] + room[buffer[y][1]-1+12][buffer[y][2]-1]
        
for x in range(15):
    if x == 3 or x == 7 or x == 11:
        print("####################")
    else:
        for y in range(10):
            print(" "+str(room[x][y]), end = "")   
        print()
 
