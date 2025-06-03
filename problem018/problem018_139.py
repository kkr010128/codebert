if __name__=="__main__":
    a = list(input().split())
    b = []
    for i in range(len(a)):
        if a[i] == "+":
            y = b.pop()
            x = b.pop()
            z = x + y
            b.append(z)
        elif a[i] == "-":
            y = b.pop()
            x = b.pop()
            z = x - y
            b.append(z)
        elif a[i] == "*":
            y = b.pop()
            x = b.pop()
            z = x * y
            b.append(z)
        else:
            b.append(int(a[i]))
    print(b[0])