n = int(input())
a = list(map(int, input().split()))
from collections import defaultdict
d = defaultdict(int)

ans=1
for num in a:
    if num==0:
        last_cnt=3
        tmp = last_cnt - d[num]
    else:
        last_cnt=d[num-1]
        tmp = last_cnt - d[num]

        if tmp == 0:
       #     tmp=1
            ans=0
    ans*=tmp
    ans%=1000000007
    d[num]+=1

print(ans)