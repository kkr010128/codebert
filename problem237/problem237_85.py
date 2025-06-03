n = int(input())
xl = []
for _ in range(n):
    x, l = map(int,input().split())
    xl.append((x-l, x+l, x, l))
xl.sort()

count = n
flag = 0
for i in range(n-1):
    if flag == 1: # this machine was removed.
        flag = 0
    else:
        left, right, x, l = xl[i]
    if xl[i+1][0] < right: # overlap
        if xl[i+1][1] <= right: # i includes i+1
            count -= 1 # remove i
        else:
            flag = 1
            count -= 1 # remove i+1

print(count)