import sys
k1 = [[0 for i in xrange(10)] for j in xrange(3)]
k2 = [[0 for i in xrange(10)] for j in xrange(3)]
k3 = [[0 for i in xrange(10)] for j in xrange(3)]
k4 = [[0 for i in xrange(10)] for j in xrange(3)]
 
n = input()
for i in xrange(n):
    m = map(int,raw_input().split())
    if m[0] == 1:
     k1[m[1]-1][m[2]-1] = k1[m[1]-1][m[2]-1] + m[3] 
    elif m[0] == 2:
     k2[m[1]-1][m[2]-1] = k2[m[1]-1][m[2]-1] + m[3]         
    elif m[0] == 3:
     k3[m[1]-1][m[2]-1] = k3[m[1]-1][m[2]-1] + m[3]         
    elif m[0] == 4:
     k4[m[1]-1][m[2]-1] = k4[m[1]-1][m[2]-1] + m[3] 
 
 
for i in xrange(3):
    for j in xrange(10):
        x = ' ' + str(k1[i][j])
        sys.stdout.write(x)
    if j == 9:
        print ""
 
print"#"*20 
 
for i in xrange(3):
    for j in xrange(10):
        y = ' ' + str(k2[i][j])
        sys.stdout.write(y)
    if j == 9:
        print ""
 
print"#"*20        
 
for i in xrange(3):
    for j in xrange(10):
        z = ' ' + str(k3[i][j])
        sys.stdout.write(z)
    if j == 9:
        print ""
         
print"#"*20 
 
for i in xrange(3):
    for j in xrange(10):
        zz = ' ' + str(k4[i][j])
        sys.stdout.write(zz)
    if j == 9:
        print ""