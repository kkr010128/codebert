K = int(input())
tmp = 1
ans = -1

if K % 7 == 0:
    L = 9 * K // 7
else:
    L = 9 * K

for i in range(10 ** 7):
    tmp *= 10
    tmp = tmp % L
    if tmp == 1:
        ans = i + 1
        break
   
print(ans)