import sys

n = input()
a = [] 
flag = {}
for j in range(1, 14):
    flag[('S',j)] = 0
    flag[('H',j)] = 0
    flag[('C',j)] = 0
    flag[('D',j)] = 0

for i in range(n):
    temp = map(str, raw_input().split())
    a.append((temp[0],temp[1]))
    #print a[i][0]
    #print a[i][1]

card = ['S', 'H', 'C', 'D']
#print card

for egara in card:
    for i in range(n):
        if(a[i][0] == egara):
            for j in range(1,14):
                if(int(a[i][1]) == j):
                    flag[(egara, j)] = 1

for egara in card:
    for j in range(1,14):
        if(flag[(egara, j)] == 0):
            sys.stdout.write(egara)
            sys.stdout.write(' ')
            sys.stdout.write(str(j))
            print

exit(0)