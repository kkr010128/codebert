import copy
import random

D = list(map(int, input().split()))
q = int(input())

for x in range(q):
    y, z = map(int, input().split())
    while True:
        r = random.randint(0,3)
        if r == 0:
            Dt = copy.copy(D)
            temp = Dt[0]
            Dt[0] = Dt[4]
            Dt[4] = Dt[5]
            Dt[5] = Dt[1]
            Dt[1] = temp
        elif r== 1:
            Dt = copy.copy(D)
            temp = Dt[0]
            Dt[0] = Dt[2]
            Dt[2] = Dt[5]
            Dt[5] = Dt[3]
            Dt[3] = temp
        elif r== 2:
            Dt = copy.copy(D)
            temp = Dt[0]
            Dt[0] = Dt[3]
            Dt[3] = Dt[5]
            Dt[5] = Dt[2]
            Dt[2] = temp
        elif r == 3:
            Dt = copy.copy(D)
            temp = Dt[0]
            Dt[0] = Dt[1]
            Dt[1] = Dt[5]
            Dt[5] = Dt[4]
            Dt[4] = temp

        D = copy.copy(Dt)
        if Dt[0] == y and Dt[1] == z:
            print(Dt[2])
            break

