x, y = [int(i) for i in input().split()]
date = [[int(i) for i in input().split()]for i in range(1,x+1)]
date2 =[int(input())for i in range(1,y+1)]
date3 =[]
for a in range(0,x):
    for b in range(0,y,):
        date3 += [date2[b]*date[a][b]]
for d in range(0,len(date3),y):
    print(sum(date3[d:d+y]))