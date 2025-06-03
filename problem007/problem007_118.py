def main():
    """ ????????? """
    num = int(input().strip())
    F = []
    for n in range(num+1):
        if n < 2:
            F.append(1)
        else:
            F.append(F[n-1] + F[n-2])
    print (F[num])
if __name__ == '__main__':
    main()