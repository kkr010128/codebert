stack = input().split()
temp  =  []
num=0
for loop in stack:
    a = loop
    if a is "+":
        num = temp.pop() + temp.pop()
        temp.append(num)
    elif a is "-":
        b=temp.pop()
        c=temp.pop()
        num = c-b
        temp.append(num)
    elif a is "*":
        num = temp.pop() * temp.pop()
        temp.append(num)
    else:
        temp .append(int(a))

print(temp[0])