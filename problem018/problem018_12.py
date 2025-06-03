def solve(l):
    e = l.pop()
    if e == '*':
        return solve(l) * solve(l)
    elif e == '+':
        return solve(l) + solve(l)
    elif e == '-':
        return - solve(l) + solve(l)
    else:
        return int(e)

formula = input().split()
print(solve(formula))