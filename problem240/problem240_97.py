n,m = map(int,input().split())
memo2 = [False for i in range(n)]
memo = [0 for i in range(n)]
count1,count2 = 0,0
for i in range(m):
    p,l = input().split()
    p = int(p)-1
    if memo2[p]:
        continue
    else:
        if l == 'WA':
            memo[p]+=1
        else:
            memo2[p] = True
            count2 += 1
            count1+=memo[p]
print(count2,count1)