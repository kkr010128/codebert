while(True):
    a, b = map(int, input().split())
    if(a == b == 0):
        break
    print('{} {}'.format(min(a, b), max(a, b)))

