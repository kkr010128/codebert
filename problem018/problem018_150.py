def main():
    n = [x for x in input().split(' ')]
    s = []
    for i in n:
        if i == '+':
            a = s.pop()
            b = s.pop()
            s.append(a + b)
        elif i == '-':
            b = s.pop()
            a = s.pop()
            s.append(a - b)
        elif i == '*':
            a = s.pop()
            b = s.pop()
            s.append(a * b)
        else:
            s.append(int(i))
    print(s.pop())


if __name__ == '__main__':
    main()