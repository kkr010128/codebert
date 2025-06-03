n = input().split()
array = []
for s in n:
    if s == "+" or s == "-" or s == "*":
        b = array.pop()
        a = array.pop()
        if   s == "+":
            array.append(a + b)
        elif s == "-":
            array.append(a - b)
        else:
            array.append(a * b)
    else:
        array.append(int(s))
print(array[0])