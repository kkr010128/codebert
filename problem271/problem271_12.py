def resolve():
    N = int(input())
    S = list(input())
    ans = [chr(((ord(s)-65+N)%26)+65) for s in S]
    print("".join(ans))


if '__main__' == __name__:
    resolve()