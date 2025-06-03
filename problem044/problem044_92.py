i = count = 0
a = b = c = ''


line = input()

while line[i] != ' ':
    a = a + line[i]
    i += 1

i += 1
while line[i] != ' ':
    b = b + line[i]
    i += 1

i += 1    
while i < len(line):
    c = c + line[i]
    i += 1
    
a = int(a)
b = int(b)
c = int(c)

while a <= b:
    if c%a == 0:
        count += 1
    a += 1

print(count)