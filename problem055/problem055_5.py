house = [[[0 for col in range(10)]for row in range(3)]for layer in range(4)]
n = int(raw_input())
for i in range(n):
    input_line = raw_input().split()
    house[int(input_line[0])-1][int(input_line[1])-1][int(input_line[2])-1] += int(input_line[3])
for i in range(0,4):
    if i != 0:
        print "#"*20
    for j in range(0,3):
        buf = ""
        for k in range(0,10):
                buf += " " + str(house[i][j][k])
        print buf