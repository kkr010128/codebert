size = [int(i) for i in input().split()]
sheet =[ [0 for i in range(size[1])] for j in range(size[0])]
for gyou in range(size[0]):
    x = [int(i) for i in input().split()]
    sheet[gyou] = x
    sheet[gyou].append(sum(sheet[gyou]))

for gyou in range(size[0]):
    for retsu in range(size[1]+1):
        print(sheet[gyou][retsu],end="")
        if retsu != size[1]:
            print(" ",end="")
    print("")
for retsu in range(size[1]+1):
    sum2 = 0
    for gyou in range(size[0]):
        sum2 += sheet[gyou][retsu]
    print(sum2, end="")
    if retsu != size[1]:
        print(" ",end="")
print("")

