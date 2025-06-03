i = raw_input().strip().split()

l = [int(i[0]),int(i[1]),int(i[2])]
tmp = 0

for j in range(3):
    for k in range(3):
        if l[k] > l[j]:
            tmp = l[j]
            l[j] = l[k]
            l[k] = tmp

print str(l[0])+" "+str(l[1])+" "+str(l[2])