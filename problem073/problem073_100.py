n = int(input())
ans = 0
for i in range(1,n):
    for j in range(1,n):
        if n <= i*j:
            break
        else:
            ans += 1
print(ans)