from sys import stdin
freq = {}
for line in stdin:
    string = line.lower()

    for i in string:
        if i.isalpha():
            freq[i] = freq.get(i, 0) + 1

for char in range(ord('a'), ord('z')+1):
    char = chr(char)
    print('%s : %d' % (char, freq.get(char, 0)))
