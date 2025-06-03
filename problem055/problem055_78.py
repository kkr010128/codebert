n = input()
arr = [map(int,raw_input().split()) for _ in range(n)]

tou = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for line in arr:
    b,f,r,v = line
    tou[b-1][f-1][r-1] = tou[b-1][f-1][r-1] + v

for i in range(4):
    for j in range(3):
        print ' '+' '.join(map(str,tou[i][j]))
    if i < 3 :
        print '#'*20