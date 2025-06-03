def main():
    a, b, c = map(int, input().split())
    tmp = c - a - b
    if tmp > 0 and 4*a*b < tmp*tmp:
        print('Yes')
    else:
        print('No')
main()
