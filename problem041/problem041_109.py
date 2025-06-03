i = raw_input().strip().split()

W = int(i[0])
H = int(i[1])
x = int(i[2])
y = int(i[3])
r = int(i[4])

flag = True

if x-r < 0 or x+r > W:
    flag = False
elif y-r < 0 or y+r > H:
    flag = False

if flag:
    print "Yes"
else:
    print "No"