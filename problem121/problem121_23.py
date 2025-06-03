N = int(input())
ans = []
if N <= 26:
    print(chr(96 + N))
else:
    while N != 0:
        val = N % 26
        if val == 0:
            val = 26
            N = N //26 - 1
        else:
            N //= 26
        ans.append(chr(96 + val))
    ans.reverse()
    print(''.join(ans))
