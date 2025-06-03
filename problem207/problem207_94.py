import sys
a = list(map(int,input().split()))
a += list(map(int,input().split()))
a += list(map(int,input().split()))

c = []
d = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

n = int(input())

for i in range(n):
    b = int(input())
    if b in a:
        c += [a.index(b)]


for i in range(8):
    flag = 0
    for j in range(3):
        if d[i][j] in c:
            flag +=1
            if flag ==3:
                print("Yes")
                sys.exit()

else:
    print("No")
