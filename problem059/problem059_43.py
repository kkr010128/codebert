import sys

l = []
for i in sys.stdin:
    l.append(i.split())

for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        l[i][j] = int(l[i][j])

for i in range(1,len(l)):
    l[i].append(sum(l[i]))

result = []
for i in range(0,l[0][1]+1):
    count = 0
    for j in range(1,l[0][0]+1):
        count += l[j][i]
    result.append(count)
l.append(result)

for i in range(1,len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j],end='')
        if j < len(l[i]) - 1:
            print(" ",end='')
    print()
