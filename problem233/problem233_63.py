n = int(input())
p = list(map(int,input().split()))

maxp = 999999
cnt=0

for x in p:
    if maxp >= x:
        cnt += 1
        maxp = x

print(cnt)
