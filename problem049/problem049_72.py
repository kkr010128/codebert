import sys
a = []
while True:
    x = map(int, raw_input().split())
    if x[0] == 0 and x[1] == 0:
        break
    a.append(x)
for i in range(len(a)):
    for j in range(a[i][0]):
        for k in range(a[i][1]):
            sys.stdout.write('#')
        print ''
    print ''