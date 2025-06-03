def main():
    K = int(input())
    A,B = map(int,input().split())

    for i in range(A,B+1):
        if i%K == 0:
            return('OK')

    return('NG')

print(main())
