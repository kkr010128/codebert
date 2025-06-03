n = int(input())
ans = 0
deno = 10
if n % 2 == 1:
    pass
else:
    while n//deno > 0:
        ans += n//deno
        deno *= 5
print(ans)
