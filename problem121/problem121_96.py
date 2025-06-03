def resolve():
    N = int(input())
    ans = ""
    while N > 0:
        rem = N % 26
        rem = 25 if rem == 0 else rem - 1
        ans = chr(ord("a")+rem) + ans
        N = (N-1) // 26
    print(ans)


if '__main__' == __name__:
    resolve()