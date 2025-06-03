from sys import stdin

w = input()

n = 0
for line in stdin:
    line = line.rstrip()

    if 'END_OF_TEXT' == line:
        break

    n += len(list(filter(lambda x: w.lower() == x.lower(), line.split(' '))))

print(n)