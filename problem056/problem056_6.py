n,m= map(int,input().split())
A_line =[]
row=[]

for i in range(n):
    line = [int(i) for i in input().split()]
    A_line.append(line)
for i in range(m):
    row += [int(i) for i in input().split()]
for i in range(n):
    c=0
    for j in range(m):
        c += A_line[i][j]*row[j]
    print(c)
