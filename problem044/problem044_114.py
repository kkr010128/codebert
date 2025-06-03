num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])
ans = 0
for i in range(a,b+1):
    if c % i == 0:
        ans += 1
print(ans)