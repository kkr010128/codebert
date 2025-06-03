all_text = []
while True:
    try:
        text = input().split()
        all_text.extend(text)
    except EOFError:
        break
text = ''.join(all_text)

count = [0]*32
for letter in text:
    i = ord(letter)
    if i < 64:
        continue
    else:
        i %= 32
    if i:
        count[i] += 1

for i in range(26):
    print(chr(i+ord('a')), ':', count[i+1])

