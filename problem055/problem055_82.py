# coding: utf-8

c1 = {1:[0]*10,2:[0]*10,3:[0]*10}
c2 = {1:[0]*10,2:[0]*10,3:[0]*10}
c3 = {1:[0]*10,2:[0]*10,3:[0]*10}
c4 = {1:[0]*10,2:[0]*10,3:[0]*10}

n = int(input())

for i in range(n):
    b,f,r,v = input().rstrip().split(" ")
    if int(b) == 1:
        c1[int(f)][int(r)-1] = c1[int(f)][int(r)-1] + int(v)
    elif int(b) == 2:
        c2[int(f)][int(r)-1] = c2[int(f)][int(r)-1] + int(v)
    elif int(b) == 3:
        c3[int(f)][int(r)-1] = c3[int(f)][int(r)-1] + int(v)
    else:
        c4[int(f)][int(r)-1] = c4[int(f)][int(r)-1] + int(v)


for i in (1,2,3):
    result = " " + str(c1[i][0])
    for j in range(1,10):
        result = result + " " + str(c1[i][j])
    print(result)
print("####################")
for i in (1,2,3):
    result = " " + str(c2[i][0])
    for j in range(1,10):
        result = result + " " + str(c2[i][j])
    print(result)
print("####################")
for i in (1,2,3):
    result = " " + str(c3[i][0])
    for j in range(1,10):
        result = result + " " + str(c3[i][j])
    print(result)
print("####################")
for i in (1,2,3):
    result = " " + str(c4[i][0])
    for j in range(1,10):
        result = result + " " + str(c4[i][j])
    print(result)