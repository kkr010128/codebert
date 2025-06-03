N = int(input())

D = []
for _ in range(N):
        D.append([int(x) for x in input().split()])

count = 0
for i in range(N):
        if(D[i][0] == D[i][1]):
                count +=1
                if(count == 3):
                        break
        else:
                count = 0

if(count == 3):
        print('Yes')
else:
        print('No')