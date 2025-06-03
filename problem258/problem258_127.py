n = int(input())
if n % 2: print(0); exit()
n //= 2
ans = 0

while n >= 5:
    n //= 5
    ans += n
print(ans)