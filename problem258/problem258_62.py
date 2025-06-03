n = int(input())

if n%2 == 1:
    print(0)
    exit()

n //= 2
ans = 0
now = 1
while True:
    tmp = n // (5**now)
    if tmp == 0:
        break
    ans += tmp
    now += 1

print(ans)