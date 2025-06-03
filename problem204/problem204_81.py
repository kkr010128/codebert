s = input()
n = int(input())

rev = 0
sh = ''
for i in range(n):
    q = input().split()
    if q[0] == '1':
        rev = (rev + 1) % 2
    else:
        head = int(q[1]) % 2
        if head ^ rev:
            sh += q[2]
            # print('sh', sh)
        else:
            s += q[2]
            # print('s', s)
ans = sh[::-1] + s
print(ans[::-1]) if rev else print(ans)