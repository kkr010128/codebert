string = list(map(str, input()))
ans =[]
for char in string:
    if char.islower():
        ans.append(char.upper())
    elif char.isupper():
        ans.append(char.lower())
    else:
        ans.append(char)
    print(ans[-1], end="")
print()

