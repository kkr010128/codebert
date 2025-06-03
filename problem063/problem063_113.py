keys = ([chr(x) for x in range(ord('a'), ord('a') + 26)])
counts = {x:0 for x in keys}

while True:
    text = ''
    try:
        text = input()
    except EOFError:
        break

    for i in range(len(text)):
        target = text[i].lower()
        if 'a' <= target <= 'z':
            counts[target] += 1

for k in keys:
    print(k, counts[k], sep=' : ')