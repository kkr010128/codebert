s = []
while True:
    x = int(input())
    if x == 0:
        break
    s.append(x)
for (i,num) in enumerate(s):
    print('Case {0}: {1}'.format(i+1,num))
