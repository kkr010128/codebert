def is_operator(ele):
    if ele == "+" or ele == "-" or ele == "*":
        return True
    else:
        return False

def calc_reverse_polish_notation(A):
    stack = []
    for i in A:
        if is_operator(i):
            a = stack.pop()
            b = stack.pop()
            ans = eval("{0} {1} {2}".format(b, i, a))
            stack.append(ans)
        else:
            stack.append(i)
    return stack.pop()

A = list(map(str,input().split()))

print(calc_reverse_polish_notation(A))
