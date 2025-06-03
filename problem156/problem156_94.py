import sys
x = int(input())
box = [a**5 for a in range(0,200)]
for i in range(200):
    for j in range(200):
        if box[i] - box[j] == x:
            print(i,j)
            sys.exit()
for k in range(200):
    for l in range(200):
        if (-1)*box[k] + box[l] == x:
            print(-(k),-(l))
            sys.exit()
for s in range(200):
    for t in range(200):
        if box[s] + box[t] == x:
            print(s,-(t))
            sys.exit()
