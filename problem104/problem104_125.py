L, R, d = map(int, input().split())
count = 0
if ((L and R and d >=1) and (L and R and d <= 100) ):
    for L in range(L, R+1):
        if (L%d == 0):
            count +=1
    print(count)


