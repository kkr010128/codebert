def solve(n):
    ret = []
    while n > 26:
        if n % 26 == 0:
            ret = [26] + ret
            n = (n - 26) // 26
        else:
            ret = [n % 26] + ret
            n = n // 26
    ret = [n] + ret
    return ret

n = int(input())
ans = ''.join([chr(ord('a') + i - 1) for i in solve(n)])
print(ans)