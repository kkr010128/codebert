n = int(input())
if n % 2 == 1:
    print(0)
    quit()
d = 10
ans = 0
while n >= d:
    ans += n // d
    d *= 5
print(ans)