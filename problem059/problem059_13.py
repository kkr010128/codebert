r,c = list(map(int,input().split()))
sum_li = [0]*(c+1)
for i in range(r):
    line = list(map(int, input().split()))
    line += [sum(line)]
    print(' '.join(list(map(str,line))))
    sum_li = [x+y for (x,y) in zip(sum_li,line)]
print(' '.join(list(map(str,sum_li))))