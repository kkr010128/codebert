a1 = [[0 for i in range(10)] for j in range(3)]
a2 = [[0 for i in range(10)] for j in range(3)]
a3 = [[0 for i in range(10)] for j in range(3)]
a4 = [[0 for i in range(10)] for j in range(3)]

n = int(input())
for i in range(0,n):
    x = [int (z) for z in input().split(' ')]
    if x[0] == 1:
        a1[x[1]-1][x[2]-1] += x[3]
    elif x[0] == 2:
        a2[x[1]-1][x[2]-1] += x[3]
    elif x[0] == 3:
        a3[x[1]-1][x[2]-1] += x[3]
    elif x[0] == 4:
        a4[x[1]-1][x[2]-1] += x[3]

for t in range(0,3):
    for i in a1[t]:
        print(" %d" % i, end='')
    print('')
print("####################")
for t in range(0,3):
    for i in a2[t]:
        print(" %d" % i, end='')
    print('')
print("####################")
for t in range(0,3):
    for i in a3[t]:
        print(" %d" % i, end='')
    print('')
print("####################")
for t in range(0,3):
    for i in a4[t]:
        print(" %d" % i, end='')
    print('')