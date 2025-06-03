n = int(input())
ans = 0
d = 10
if n%2==1:
    print(0)
    import sys
    sys.exit()
while True:
    ans += n//d
    d *= 5
    if d>n:
        break
print(ans)