n = int(input())
ans = 0
for i in range(9):
    if n % (i+1) == 0:
        if n//(i+1) >= 1 and n//(i+1) <= 9:
            print('Yes')
            ans = 1
            break
if ans == 0:
    print('No')