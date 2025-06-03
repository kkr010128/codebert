def main() :
    lst = input().split()
    stack = []
    for i in lst :
        if i == "+" :
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)

        elif i == "-" :
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)

        elif i == "*" :
            x = stack.pop()
            y = stack.pop()
            stack.append(x * y)

        else :
            stack.append(int(i))

    print(stack.pop())


if __name__ == "__main__" :
    main()