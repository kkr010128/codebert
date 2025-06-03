x = int(input())
mo = 100
ans = 0
while mo < x:
    r = mo//100
    mo += r
    ans += 1
print(ans)