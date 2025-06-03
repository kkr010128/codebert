r,c = map(int,input().split())
num=[]
r_sum =[]
for i in range(r):
    num.append([int(i) for i in input().split()])
for i in range(r):
    line_sum = 0
    for j in range(c):
        line_sum += num[i][j]
    num[i].append(line_sum)
for i in range(c+1):
    row_sum = 0
    for j in range(r):
        row_sum += num[j][i]
    r_sum.append(row_sum)
num.append(r_sum)
for i in range(len(num)):
    print(' '.join(str(i) for i in num[i]))
