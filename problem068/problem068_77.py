p = input()
num = int(input())
for i in range(num):
    order = list(map(str,input().split()))
    a = int(order[1])
    b = int(order[2])
    if order[0] == 'print':
        print(p[a:b+1])
    elif order[0] == 'replace':
        rep = order[3]
        p = p[:a] + rep + p[b+1:]
    else:
        p = p[:a] + p[a:b+1][::-1] + p[b+1:]

