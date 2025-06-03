def solve(n):
    if n % 2 == 1:
        return 0 
    div_2 = 0
    cur = 2
    while cur <= n:
        div_2 += (n // cur)
        cur = cur * 2
    div_5 = 0
    cur = 5
    while cur <= n:
        div_5 += (n // cur) // 2
        cur = cur * 5
    return min(div_2, div_5)

n = int(input())
print(solve(n))
