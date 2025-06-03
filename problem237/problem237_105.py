n = int(input())
x = [0]*n
for i in range(n):
    x[i] = list(map(int,input().split()))
x.sort(key= lambda val : val[0])
i = 0
while 1:
    if i >= n - 1:
        break
    
    if x[i][0] + x[i][1] > x[i+1][0] - x[i+1][1]:
        if x[i][0] + x[i][1] > x[i+1][0] + x[i+1][1]:
            del x[i]
            n -= 1
        else:
            del x[i+1]
            n -= 1
    else:
        i += 1
print(len(x))
