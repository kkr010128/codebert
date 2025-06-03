a, b = map(int, input().split())

if a == b:
    print('a == b')
    exit()

print('a < b' if a < b else 'a > b')