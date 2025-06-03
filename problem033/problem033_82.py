a, b, c, d, e, f = map(int, input().split())
S = list(input())
i = 0
number1 = a
number2 = b
number3 = c
number4 = d
number5 = e
number6 = f

while i < len(S) :
    if S[i] == "N" :
        number1 = b
        number2 = f
        number3 = c
        number4 = d
        number5 = a
        number6 = e
    elif S[i] == "S" :
        number1 = e
        number2 = a
        number3 = c
        number4 = d
        number5 = f
        number6 = b
    elif S[i] == "E" :
        number1 = d
        number2 = b
        number3 = a
        number4 = f
        number5 = e
        number6 = c
    elif S[i] == "W" :
        number1 = c
        number2 = b
        number3 = f
        number4 = a
        number5 = e
        number6 = d
    a = number1
    b = number2
    c = number3
    d = number4
    e = number5
    f = number6
    i = i + 1
print(number1)
