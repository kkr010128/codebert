a, b, c = map(int, input().split())
divisors = []
i = 1
while(i * i < c):
    if(c % i == 0):
        divisors.append(i)
        divisors.append(c // i)
    i += 1
if(i * i == c):
    divisors.append(i)
ans = 0
for i in range(len(divisors)):
    if(a <= divisors[i] <= b):
        ans += 1
print(ans)