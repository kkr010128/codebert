stack = [n for n in input().split(' ')]
ans = []
for n in stack:
    if n == '+':
        temp = ans[-1] + ans[len(ans)-2]
        ans.pop()
        ans[-1] = temp
    elif n == '-':
        temp =  ans[len(ans)-2] - ans[-1]
        ans.pop()
        ans[-1] = temp
    elif n == '*':
        temp = ans[len(ans)-2]  * ans[-1]
        ans.pop()
        ans[-1] = temp
    elif n == '/':
        temp = ans[len(ans)-2] / ans[-1]
        ans.pop()
        ans[-1] = temp
    else:
        ans.append(int(n))
print(ans[0])