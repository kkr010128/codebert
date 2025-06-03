n = int(input())

times_ls = [0] * (n+1)
for base in range(1,n+1):
    for j in range(1,n+1):
        if base * j <= n:
            times_ls[base * j] += 1
        else:
            break
ans = 0
for i in range(1,n+1):
    ans += i * times_ls[i]
print(ans)
    


