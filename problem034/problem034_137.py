apex = ((1,2,3),
        (1,4,2),
        (1,5,4),
        (1,3,5),

        (2,1,4),
        (2,3,1),
        (2,6,3),
        (2,4,6),

        (3,1,2),
        (3,5,1),
        (3,6,5),
        (3,2,6),

        (4,1,5),
        (4,2,1),
        (4,6,2),
        (4,5,6),

        (5,3,6),
        (5,1,3),
        (5,4,1),
        (5,6,4),

        (6,3,2),
        (6,5,3),
        (6,4,5),
        (6,2,4)
        )

dice = {}
label = []
label[:] = map(int,input().split())
#print('label: {}'.format(label))

for i in range(0,6):
    dice[label[i]] = i+1
#print('dice: {}'.format(dice))


q = int(input())

for _ in range(0,q):
    numbers = []
    numbers[:] = map(int,input().split())
    right = 0
    for t in apex:
        if (t[0] == dice[numbers[0]] and t[1] == dice[numbers[1]]):
            right = t[2]
            #print('{} {} {}'.format(t[0],t[1],t[2]))
            break
    for key, n in dice.items():
        if (n == right):
            print(key)
            break

