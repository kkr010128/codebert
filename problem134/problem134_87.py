n = int(input())
ans = 1
l = list(map(int,input().split()))
if l.count(0) != 0 :
    print(0)
    exit()
for i in range(n) :
    ans *= l[i]
    if ans > 10**18 :
        print('-1')
        exit()
print(ans)