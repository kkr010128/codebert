x,k,d = list(map(int,input().split()))

x = abs(x)

m = x // d

if m >= k:
    ans = x - (d*k)

elif (k-m) % 2 == 0:
    ans = x - (d*m)

else:
    ans = x - (d*m) - d

print(abs(ans))