a = []
while True:
    d = list(map(int, input().split()))
    if d == [0,0]:
        break
    d.sort()
    a.append(d)
for x in a:
    print('{} {}'.format(x[0],x[1]))