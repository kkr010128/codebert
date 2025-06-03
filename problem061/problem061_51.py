def backoutput(y):
    if y.isupper():
        return y.lower()
    elif y.islower():
        return y.upper()
    else:
        return y

first_input = list(map(backoutput, input()))
print(*first_input, sep='')

