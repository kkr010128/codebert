def showrooms(building,floor,rooms):
    for x in xrange(0,floor):
        for y in xrange(0,rooms):
            if y==0:
                print "",
                print building[x][y],
            elif y ==rooms-1:
                print building[x][y]
            else:
                print building[x][y],
FLOOR = 3
ROOMS = 10
n = input()
building1 = [[0 for i in range(ROOMS)] for j in range(FLOOR)]
building2 = [[0 for i in range(ROOMS)] for j in range(FLOOR)]
building3 = [[0 for i in range(ROOMS)] for j in range(FLOOR)]
building4 = [[0 for i in range(ROOMS)] for j in range(FLOOR)]
# for x in xrange(0,n):
for x in xrange(0,n):
    b,f,r,v = map(int,raw_input().split())
    f=f-1
    r=r-1
    if b==1:
        building1[f][r] += v
    elif b==2:
        building2[f][r] += v
    elif b==3:
        building3[f][r] += v
    elif b==4:
        building4[f][r] += v
    else:
        print "your input is invalid format."
        break
showrooms(building1,FLOOR,ROOMS)
print "####################"
showrooms(building2,FLOOR,ROOMS)
print "####################"
showrooms(building3,FLOOR,ROOMS)
print "####################"
showrooms(building4,FLOOR,ROOMS)