W=input()
count=0
while True:
    text=input()
    if text == 'END_OF_TEXT':
        break
    else:
        ls = list(map(str, text.split()))
    for s in ls:
        if s.lower() == W.lower():
            count += 1
print(count)