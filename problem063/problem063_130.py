from collections import Counter

counter = Counter()

while True:
    try:
        s = input()
        for c in s:
            counter[c.lower()] += 1

    except:
        break

for c in range(ord('a'), ord('z')+1):
    print('{} : {}'.format(chr(c), counter[chr(c)]))