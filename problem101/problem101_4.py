def main():
    A,B,C = map(int,input().split())
    K = int(input())
    num = 0

    while (B <= A):
        num += 1
        if num <= K:
            B *= 2
        else:
            return ("No")

    while (C <= B):
        num += 1
        if num <= K:
            C *= 2
        else:
            return ('No')

    return('Yes')

print(main())
