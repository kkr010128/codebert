
N = int(input().strip())

l = [chr(i) for i in range(97, 97+26)]

ans = ""
if N <= 26:
    ans = l[N-1]
else:
    for i in range(1,11):
        st = 0
        for k in range(i):
            st = st + 26**(k+1)
        nd = st + 26**(i+1)
        if st < N <= nd:
            N = N - st
            for j in range(i+1):
                r = N % 26
                N = N // 26
                if r != 0:
                    N += 1
                    ans = l[r-1] + ans
                if r == 0:
                    ans = "z" + ans
            break

print(ans)