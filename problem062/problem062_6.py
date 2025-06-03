result = []
while 1:
    n = int(input())
    if n == 0:
        break
    ans = 0
    for i in range(1,1001):
        ans += n // pow(10,1000-i)
        n = n % pow(10,1000-i)
    result.append(ans)

for i in range(len(result)):
    print(result[i])

