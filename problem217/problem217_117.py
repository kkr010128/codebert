def main():
    N = int(input())
    l = list(map(int, input().split()))
    l2 = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l2.append(l[i])
    for i in range(len(l2)):
        if not l2[i] % 3 == 0 and not l2[i] % 5 == 0:
            print('DENIED')
            return
    print('APPROVED')

main()