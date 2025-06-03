a = []
while True:
    num = int(input())
    if num == 0:
        break
    a.append(num)
i=1
for x in a:
    print('Case {}: {}'.format(i,x))
    i += 1