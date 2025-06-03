n = int(input())
rooms = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for rec in range(n):
    b, f, r, v = map(int, input().split())
    rooms[b-1][f-1][r-1] += v
    
for i, b in enumerate(rooms):
    for f in b:
        print("",*f)
    if i != 3:
        print("####################")