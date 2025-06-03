arguments = input().split()

array = []

for word in arguments:
    if word == '-':
        s1 = array.pop()
        s2 = array.pop()
        array.append(s2-s1)
    elif word == '*':
        s1 =array.pop()
        s2 = array.pop()
        array.append(s1*s2)
    elif word == '+':
        s1 = array.pop()
        s2 = array.pop()
        array.append(s1+s2)
    else:
        array.append(int(word))


print(array.pop())