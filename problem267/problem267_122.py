n = int(input())
lst = list(input())
cnt = 0
Num = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            s = [str(i),str(j),str(k)]
            Num.append(s)

for num in Num:
    flag1 = False
    flag2 = False
    memo1 = 0
    memo2 = 0
    for x in range(n-2):
        if num[0] == lst[x]:
            flag1 = True
            memo1 = x
            break
    if flag1:
        for y in range(memo1+1,n-1):
            if num[1] == lst[y]:
                flag2 = True
                memo2 = y
                break
        if flag2:
            for z in range(memo2+1,n):
                if num[2] == lst[z]:
                    cnt += 1
                    break
print(cnt)