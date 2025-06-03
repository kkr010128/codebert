
n = int(input())
li = list(map(int,input().split()))

li.sort()

ans = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if li[i] != li[j] != li[k]:
                if li[i] + li[j] > li[k]:
                    ans += 1
print(ans)
