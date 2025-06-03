n, m = map(int, input().split())
err = False
ans = list('*' * n)

for _ in range(m):
    si, ci = map(int, input().split())
    if ans[si - 1] == '*' or ans[si - 1] == str(ci):
        ans[si - 1] = str(ci)
    else:
        err = True

if ans[0] == '0' and n != 1:
    err = True

if ans[0] == '*':
    if n == 1:
        ans[0] = '0'
    else:
        ans[0] = '1'

if err:
    print(-1)
else:
    print(''.join(ai if ai != '*' else '0' for ai in ans))
