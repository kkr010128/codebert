n, x, t = map(int, input().split(' '))

count = int(n / x)
if(n % x != 0):
    count += 1

print(count * t)