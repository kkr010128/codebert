a, b, c, d = map(int, input().split())
if -(-c//b) > -(-a//d):
    print('No')
    exit()
print('Yes')
