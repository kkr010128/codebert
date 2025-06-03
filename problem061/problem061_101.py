text = input()

result = ''
for i in range(len(text)):
    code = ord(text[i])
    if ord('A') <= code <= ord('Z'):
        result += chr(code + 32)
    elif ord('a') <= code <= ord('z'):
        result += chr(code - 32)
    else:
        result += chr(code)

print(result)