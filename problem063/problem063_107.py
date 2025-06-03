text = ''
while(True):
    try:
        text += input().lower()
    except:
        break

count = [0 for i in range(26)]
for c in text:
    if c < 'a'  or c > 'z':
        continue

    count[ord(c) - ord('a')] += 1

for i, c in enumerate(count):
    print('{0} : {1}'.format(chr(i + ord('a')), c))