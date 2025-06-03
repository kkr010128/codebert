n = int(input())
numlist = []
i = 2
ans = 0

while i * i <= n + 1:
    count = 0
    while n % i == 0:
        count += 1
        n //= i
    i += 1
    if count != 0:
        numlist.append(count)
if n != 1:
    numlist.append(1)

while len(numlist) != 0:
    i = 1
    a = numlist.pop(0)
    while a - i >= 0:
        a -= i 
        i += 1
        ans += 1
print(ans)