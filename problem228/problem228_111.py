h = int(input())

ans = 1
while h > 0:
    h //= 2
    ans *= 2
print(ans-1)