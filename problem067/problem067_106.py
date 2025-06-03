poi = [0,0]
for mak in range(int(input())) :
    tem = input().split()
    if tem[0] == tem[1] :
        poi[0] += 1
        poi[1] += 1
    else :
        che = sorted(tem)

        if tem[0] != che[0] : poi[0] += 3
        else                : poi[1] += 3

print(poi[0],poi[1])