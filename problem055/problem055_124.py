rooms = []
rooms.append([[0 for i in range(10)] for j in range(3)])
rooms.append([[0 for i in range(10)] for j in range(3)])
rooms.append([[0 for i in range(10)] for j in range(3)])
rooms.append([[0 for i in range(10)] for j in range(3)])

num = int(raw_input())
for i in range(num):
    b,f,r,v = map(int, raw_input().split())
    rooms[b-1][f-1][r-1] += v

for number, room in enumerate(rooms):
    for row in room:
        print " %d %d %d %d %d %d %d %d %d %d" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
    if len(rooms) - 1 > number:
        print('####################')