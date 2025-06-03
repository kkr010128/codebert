a = {x:0 for x in range(ord('a'), ord('z') + 1)}

while True:
    try:
        text = input()
        for x in text:
            if ord('a') <= ord(x) <= ord('z') or ord('A') <= ord(x) <= ord('Z'):
                a[ord(x.lower())] += 1
    except EOFError:
        break

for x in range(ord('a'), ord('z') + 1):
    print(chr(x), ':', a[x])