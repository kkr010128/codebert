s = input()
n = int(input())
ans = ''
i = 0
while i < n:
    order = list(map(str, input().split(' ')))
    if order[0] == 'print':
        ans += s[int(order[1]):int(order[2])+1] + '\n'
    elif order[0] == 'reverse':
        i1 = int(order[1])
        i2 = int(order[2])
        s0 = s[:i1]
        j = 0
        while j < (i2 - i1 + 1):
            s0 += s[i2 - j]
            j += 1
        s0 += s[i2+1:]
        s = s0
    else:
        i1 = int(order[1])
        i2 = int(order[2])
        s = s[:i1] + order[3] + s[i2+1:]
    i += 1
print(ans[:-1])
