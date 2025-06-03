n = int(open(0).readline())

ans = 0
for i in range(1,n+1):
    count = n//i
    end = count*i
    ans += count * (i+end)//2
print(ans)