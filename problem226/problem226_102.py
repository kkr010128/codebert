def main():
    H, N = map(int, input().split(' '))
    A = input().split(' ')
    total = 0
    for i in A:
        total += int(i)
    if total >= H:
        print('Yes')
    else:
        print('No')
main()
