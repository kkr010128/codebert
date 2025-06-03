import math
y=int(input())
cnt=0
for i in range (1,y+1):
    for k in range(1,y+1):
        for j in range(1,y+1):
            a = [i,j,k]#リスト
            ans = a[0]
            for x in range(len(a)):
                ans = math.gcd(ans, a[x])
            cnt+=ans
print(cnt)