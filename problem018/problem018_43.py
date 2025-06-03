def Cal(sym,n1,n2):
    n1 = int(n1)
    n2 = int(n2)
    if sym == '+':
        ans = n1 + n2
    elif sym == '-':
        ans = n1 - n2
    else:
        ans = n1 * n2
        
    return ans

stack = []

for item in raw_input().split():
    if item.isdigit():
        stack.append(item)
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        sym = item
        ans = Cal(sym,n1,n2)
        stack.append(ans)

Ans = stack.pop()

print Ans