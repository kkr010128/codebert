n = int(input())

def count_ab(start, end):
    l = len(str(n))
    if start == 0:
        return 0
    if l == 1:
        if start == end:
            if n >= start:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        if start == end:
            cnt = 1
        else:
            cnt = 0
        if int(str(n)[0]) > start:
            for i in range(1, l):
                cnt += 10 ** i // 10
        if int(str(n)[0]) == start:
            for i in range(1, l - 1):
                cnt += 10 ** i //10
            cnt += int(str(n)[1:]) // 10
            if int(str(n)[-1]) >= end:
                cnt += 1
        if int(str(n)[0]) < start:
            for i in range(1, l - 1):
                cnt += 10 ** i //10
        return cnt

ans = 0
for i in range(10):
    for j in range(10):
        A = count_ab(i, j)
        B = count_ab(j, i)
        ans += A * B

print(ans)