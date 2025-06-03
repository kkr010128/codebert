import sys

l = []
for i in sys.stdin:
    l.append(i)

for i in range(0,len(l)):
    if int(l[i]) == 0:
        break
    count = 0
    for j in range(0,len(l[i])-1):
        count += int(l[i][j])
    print(count)
