s = input()
n = int(input())

for _ in range(n):
    orders = input().split()
    order = orders[0]
    a = int(orders[1])
    b = int(orders[2])
    if order == 'print':
        print(s[a:b + 1])
    elif order == 'reverse':
        s = s[:a] + ''.join(list(reversed(s[a:b+1]))) + s[b + 1:]
    elif order == 'replace':
        s = s[:a] + orders[-1] + s[b + 1:]
