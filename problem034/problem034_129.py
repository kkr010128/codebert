dice = list(map(int,input().split()))

def move(x):
    if x == "N":
        d[0],d[1],d[2],d[3],d[4],d[5] = d[1],d[5],d[2],d[3],d[0],d[4]

    elif x == "W":
        d[0],d[1],d[2],d[3],d[4],d[5] = d[2],d[1],d[5],d[0],d[4],d[3]

    elif x == "E":
        d[0],d[1],d[2],d[3],d[4],d[5] = d[3],d[1],d[0],d[5],d[4],d[2]

    elif x == "S":
        d[0],d[1],d[2],d[3],d[4],d[5] = d[4],d[0],d[2],d[3],d[5],d[1]

q = int(input())

for i in range(q):
    a,b = map(int,input().split())
    d = dice

    if a == dice[1]:
        move("N")
    if a == dice[2]:
        move("W")
    if a == dice[3]:
        move("E")
    if a == dice[4]:
        move("N")
    if a == dice[5]:
        move("S")
        move("S")

    if b == d[1]:
        print(d[2])
    if b ==  d[2]:
        print(d[4])
    if b ==  d[3]:
        print(d[1])
    if b ==  d[4]:
        print(d[3])
