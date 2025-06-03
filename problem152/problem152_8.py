import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())
s = []
for _ in range(n):
    s.append(input())

'''
N = sum([len(i) for i in s])
R = sum([i.count('(') for i in s])
if N % 2 == 1 or s.count('(') != N // 2:
    print('No')
    exit()
'''

bothleft = []
bothright = []
bothneutral = [0]
left = [0]
right = [0]

for i in s:
    lnum = 0
    now = 0
    for j in range(len(i)):
        if i[j] == '(':
            now -= 1
        else:
            now += 1
            lnum = max([lnum, now])

    rnum = 0
    now = 0
    for j in range(len(i) - 1, -1, -1):
        if i[j] == ')':
            now -= 1
        else:
            now += 1
            rnum = max([rnum, now])
    
    if lnum > 0:
        if rnum > 0:
            if lnum > rnum:
                bothleft.append((rnum, lnum - rnum))
            elif rnum > lnum:
                bothright.append((lnum, rnum - lnum))
            else:
                bothneutral.append(lnum)
        else:
            left.append(lnum)
    elif rnum > 0:
        right.append(rnum)

bothneutral = max(bothneutral)
bothleft.sort()
bothright.sort()

lsum = sum(left)
for i in range(len(bothleft)):
    if bothleft[i][0] > lsum:
        print('No')
        exit()
    lsum += bothleft[i][1]

if bothneutral > lsum:
    print('No')
    exit()

rsum = sum(right)
for i in range(len(bothright)):
    if bothright[i][0] > rsum:
        print('No')
        exit()
    rsum += bothright[i][1]

if lsum != rsum:
    print('No')
    exit()

print('Yes')