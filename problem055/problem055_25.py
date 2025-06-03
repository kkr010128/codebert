n = int(input())
count = 0
room = [int(0) for i in range(4) for j in range(3) for k in range(10)]
while count < n:
    x = list(map(lambda k: int(k), input().split(" ")))
    room[(x[0]-1)*30+(x[1]-1)*10+(x[2]-1)] += x[3]
    count += 1
for i in range(4):
    if i != 0:
        print("####################")
    for j in range(3):
        for k in range(10):
            print(" %d" % room[30*i+10*j+k], end="")
        print("")