i = 1
a = []
while True:
    x = input()
    if x == 0:
        break
    a.append(x)
for i in range(len(a)):
    print 'Case ' + str(i+1) + ': ' + str(a[i])