if __name__ == "__main__":
    stack =[]
    ope = {"+": lambda a, b: b + a, "-": lambda a, b: b - a, "*": lambda a, b: b * a}
    for x in input().split():
        if x in ope:
            stack.append(ope[x](stack.pop(),stack.pop()))
        else:
            stack.append(int(x))
    print(stack[-1])