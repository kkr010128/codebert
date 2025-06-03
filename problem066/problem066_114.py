while True:
    s = list(input())
    if s == ['-']:
        break
    for _ in range(int(input())):
        h = int(input())
        s = s[h:] + s[:h]
    for c in s:
        print(c, end='')
    print('')