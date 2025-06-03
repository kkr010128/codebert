inp = [i for i in input().split()]
n = int(input())
array = [[i for i in input().split()] for i in range(n)]
for i2 in range(n):
    fuck =""
    for i in range(1,33):
        if (i<=20 and i%5==0) or i==22 or i==27 or i==28:
            s = "N"
        else:
            s = "E"
        if s == "E":
            a = []
            a.append(inp[3])
            a.append(inp[1])
            a.append(inp[0])
            a.append(inp[5])
            a.append(inp[4])
            a.append(inp[2])
            inp = a
            if inp[0] == array[i2][0] and inp[1] == array[i2][1] and inp[2] != fuck:
                print(inp[2])
                fuck = inp[2]
        elif s == "N":
            a = []
            a.append(inp[1])
            a.append(inp[5])
            a.append(inp[2])
            a.append(inp[3])
            a.append(inp[0])
            a.append(inp[4])
            inp = a
            if inp[0] == array[i2][0] and inp[1] == array[i2][1] and inp[2] != fuck:
                print(inp[2])
                fuck = inp[2]