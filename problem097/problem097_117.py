K = int(input())

ans = -1
num7 = 7

for i in range(1000000):
    if (num7 % K) == 0:
        ans = i+1
        break
    else:
        num7 = (num7*10+7)%K
        i+=1

print(ans)