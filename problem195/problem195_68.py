input1= []

try:
    while True:
        s = input()
        if s == '':
            break
        input1.append(s)

except EOFError:
    pass

for s in input1:

 list = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]

 print(list[int(s)-1])