def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

n = int(input())
ans = n
divisor_num = divisor(n)

for i in divisor_num:
    j = n // i
    tmp = i + j - 2
    ans = min(ans, tmp)

print(ans)