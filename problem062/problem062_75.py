ans = ''
while True:
    s = int(input())
    if s == 0:
        break
    else:
        x = 0
        while s != 0:
            x += s % 10
            s = s // 10
        ans += str(x) + '\n'
if ans != '':
    print(ans[:-1])
