def main():
    s, t = map(str, input().split(' '))
    a, b = map(int, input().split())
    u = str(input())
    if u == s:
        print(str(a - 1) + ' ' + str(b))
    else:
        print(str(a) + ' ' + str(b - 1))
main()