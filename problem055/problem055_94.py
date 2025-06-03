import sys
n = int(raw_input())

building_a = [[0 for j in range(11)] for i in range(4)]
building_b = [[0 for j in range(11)] for i in range(4)]
building_c = [[0 for j in range(11)] for i in range(4)]
building_d = [[0 for j in range(11)] for i in range(4)]

for i in range(n):
    b, f, r, v = map(int, raw_input().split())
    if b == 1:
        building_a[f][r] += v
    elif b == 2:
        building_b[f][r] += v
    elif b == 3:
        building_c[f][r] += v
    elif b == 4:
        building_d[f][r] += v
        
for i in range(1, 4):
    print "",
    for j in range(1, 11):
        print building_a[i][j],
    print 
for i in range(20):
    sys.stdout.write("#")
print

for i in range(1, 4):
    print "",
    for j in range(1, 11):
        print building_b[i][j],
    print 
for i in range(20):
    sys.stdout.write ("#")
print

for i in range(1, 4):
    print "",
    for j in range(1, 11):
        print building_c[i][j],
    print 
for i in range(20):
    sys.stdout.write("#")
print

for i in range(1, 4):
    print "",
    for j in range(1, 11):
        print building_d[i][j],
    print